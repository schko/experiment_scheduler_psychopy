#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on February 01, 2023, at 14:05
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_7
import ast


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Scheduler'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'scheduler csv': 'block_scheduler.csv',
    'output folder': 'Results/',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'%s/%s_%s_%s' % (expInfo['output folder'], expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\shara\\Desktop\\bmed-experiment-main\\scheduler_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "setup" ---
# Run 'Begin Experiment' code from exp_monitor
import tkinter as tk       
import threading
import tkinter.font as tkFont
import tkinter.ttk as ttk
import asyncio
import websockets
from psychopy.hardware import keyboard
from psychopy import core
import pandas as pd

# create shared lock
current_selection = 0
force_end_routine = False
pause_routine = True
lock = threading.Lock()
timer = None

scheduler_csv_data = pd.read_csv(expInfo['scheduler csv'])
sched_header = list(scheduler_csv_data.columns)
sched_list = scheduler_csv_data.values.tolist()

class MainApplication(tk.Frame):              
    def __init__(self, parent, current_selection, pause_routine, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)   
        self.parent = parent
        #setting title
        parent.title("Experiment Scheduler")
        #setting window size
        self.started = False # turned on after start
        width=800
        height=500
        #width=1000
        #height=800
        self.width = width
        self.height = height
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, -screenwidth/2, (screenheight - height) / 2 + 40)
        #alignstr = '%dx%d+%d+%d' % (width, height, screenwidth/2, (screenheight - height) / 2)
        parent.geometry(alignstr)
        parent.resizable(width=False, height=False)
        
        self.selection = current_selection
        self.pause_routine = pause_routine
        self.countdown_params = None

        self.counter = tk.Label(self,font=(None, 15),bg= "gray90")
        self.counter.place(x=width//30,y=height//3.5,width=width//8.6,height=height//20)
        self.countdown(5,method='up',selection=current_selection)
        
        self.UpButton=tk.Button(self,state='disabled')
        self.UpButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.UpButton["font"] = ft
        self.UpButton["fg"] = "#000000"
        self.UpButton["justify"] = "center"
        self.UpButton["text"] = "Previous"
        self.UpButton.place(x=width//30,y=height//2.5,width=width//8.6,height=height//20)
        self.UpButton["command"] = self.UpButton_command

        self.DownButton=tk.Button(self,state='disabled')
        self.DownButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.DownButton["font"] = ft
        self.DownButton["fg"] = "#000000"
        self.DownButton["justify"] = "center"
        self.DownButton["text"] = "Next"
        self.DownButton.place(x=width//30,y=height//2.08,width=width//8.6,height=height//20)
        self.DownButton["command"] = self.DownButton_command

        self.StartButton=tk.Button(self)
        self.StartButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.StartButton["font"] = ft
        self.StartButton["fg"] = "#000000"
        self.StartButton["justify"] = "center"
        self.StartButton["text"] = "Start"
        self.StartButton.place(x=width//4.5,y=height//5.56,width=width//8.6,height=height//20)
        self.StartButton["command"] = self.StartButton_command

        self.PauseButton=tk.Button(self)
        self.PauseButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.PauseButton["font"] = ft
        self.PauseButton["fg"] = "#000000"
        self.PauseButton["justify"] = "center"
        self.PauseButton["text"] = "Pause"
        self.PauseButton.place(x=width//1.5,y=height//5.56,width=width//8.6,height=height//20)
        self.PauseButton["command"] = self.PauseButton_command
        
        self.tree = None
        self._setup_widgets()
        self._build_tree()
        
        
        self.tree.focus_set()
        self.children = self.tree.get_children()
        if self.children:
            self.tree.focus(self.children[self.selection])
            self.tree.selection_set(self.children[self.selection])

        thd_as = threading.Thread(target=self.run_asyncio_server)   # gui thread
        thd_as.daemon = True  # background thread will exit if main thread exits
        thd_as.start()  # start tk loop
    
    def countdown(self, count, selection, method='down',set_color=True):
        # ensure we need to continue counting
        if self.pause_routine:
            self.counter['text'] = 'PAUSED'
            return
        if selection != self.selection:
            return
        # change text in label        
        self.counter['text'] = "{:.2f}".format(count)
        if method=='down' and count > 0:
            if set_color:
                self.counter.config(fg="red")
            # call countdown again after 10ms
            self.parent.after(10, self.countdown, round(count-.01,2), selection, method,False)
        elif method=='up':
            if set_color:
                self.counter.config(fg="blue")
            # call countdown again after 10ms
            self.parent.after(10, self.countdown, round(count+.01,2), selection, method,False)
            
    def run_asyncio_server(self):
        async def handler(websocket, path):
            data = await websocket.recv()
            if data=='next':
                self.move_focus_down()
            elif data=='last':
                self.move_focus_up()
            reply = f"Data recieved bro as:  {data} selection {self.selection}!"
            await websocket.send(reply)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        start_server = websockets.serve(handler, "localhost", 8000)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        
    def move_focus_down(self):
        if len(self.children)-1 == self.selection: # reset
            return
        last_selection = self.selection
        self.selection += 1
        if self.children and len(self.children) > self.selection:
            self.tree.focus(self.children[self.selection])
            self.tree.selection_set(self.children[self.selection])
        
        this_child = self.tree.item(self.children[self.selection])["values"]
        method = 'up' if float(this_child[2]) == 0 else 'down'
        self.countdown_params = (float(this_child[2]), self.selection, method)
        self.countdown(float(this_child[2]),selection=self.selection,method=method)
        global current_selection, force_end_routine, pause_routine
        with lock:
            if last_selection != self.selection:
                force_end_routine = True
            current_selection = self.selection
            
    def move_focus_up(self):
        if self.selection == 0: # if we hit the start
            return
            
        last_selection = self.selection
        self.selection -= 1
        if self.children and self.selection >= 0:
            self.tree.focus(self.children[self.selection])
            self.tree.selection_set(self.children[self.selection])
        #if self.selection == -1: # reset
            # self.selection = len(self.children)-1
        this_child = self.tree.item(self.children[self.selection])["values"]
        method = 'up' if float(this_child[2]) == 0 else 'down'
        self.countdown_params = (float(this_child[2]), self.selection, method)
        self.countdown(float(this_child[2]),selection=self.selection,method=method)
        global current_selection, force_end_routine, pause_routine
        with lock:
            if last_selection != self.selection:
                force_end_routine = True
            current_selection = self.selection

    def _setup_widgets(self):
        s = """\click on header to sort by that column
            to change width of column drag boundary
            """
        # msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
        #    padding=(10, 2, 10, 6), text=s)
        #msg.pack(fill='x')
        container = ttk.Frame()
        # container.pack(fill='both', expand=True)
        container.place(x=self.width//4.6,y=self.height//3.57,width=self.width//1.4,height=self.height//1.5)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=sched_header, show="headings", selectmode='none')
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in sched_header:
            self.tree.heading(col, text=col.title())
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in sched_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(sched_header[ix],width=None)<col_w:
                    self.tree.column(sched_header[ix], width=col_w)

    def UpButton_command(self):
        if self.started:
            self.move_focus_up()


    def DownButton_command(self):
        if self.started:
            self.move_focus_down()


    def StartButton_command(self):
        if not self.started:
            self.started = True
            self.UpButton['state'] = 'normal'
            self.DownButton['state'] = 'normal'
            self.StartButton['state'] = 'disabled'
            this_child = self.tree.item(self.children[self.selection])["values"]
            method = 'up' if float(this_child[2]) == 0 else 'down'
            self.countdown_params = (float(this_child[2]), self.selection, method)
        global current_selection, force_end_routine, pause_routine
        with lock:
            if self.pause_routine:
                self.pause_routine = False
                self.PauseButton['state'] = 'normal'
                self.StartButton['state'] = 'disabled'
                self.countdown(self.countdown_params[0],selection=self.countdown_params[1],method=self.countdown_params[2])
            pause_routine = self.pause_routine


    def PauseButton_command(self):
        global current_selection, force_end_routine, pause_routine
        with lock:
            if not self.pause_routine:                
                self.pause_routine = True
                force_end_routine = True # this may be changed depending on preferred pause behavior
                self.StartButton['state'] = 'normal'
                self.PauseButton['state'] = 'disabled'
            pause_routine = self.pause_routine

def runtk(current_selection, pause_routine):  # runs in background thread
    root = tk.Tk()
    MainApplication(root, current_selection, pause_routine).pack(side="top", fill="both", expand=True)
    root.mainloop()

thd = threading.Thread(target=runtk, args=(current_selection,pause_routine,))   # gui thread
thd.daemon = True  # background thread will exit if main thread exits
thd.start()  # start tk loop
# Run 'Begin Experiment' code from exp_setup
from psychopy.hardware import keyboard
from psychopy import core
import time

presentation_time = 1 # seconds
presentation_time_floor = .5
math_num_dur = 1
equal_delay = .3
equal_dur = 1
math_answer_delay = .5
math_answer_dur = 1
start_math_difficulty = 1

math_num_dur + equal_delay + equal_dur + math_answer_delay 
setup_waiter = visual.TextStim(win=win, name='setup_waiter',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "parse_scheduler_row" ---
parse_waiter = visual.TextStim(win=win, name='parse_waiter',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "start_routine_trigger" ---

# --- Initialize components for Routine "acquisition_start" ---
acq_start_text = visual.TextStim(win=win, name='acq_start_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "end_routine_trigger" ---

# --- Initialize components for Routine "start_routine_trigger" ---

# --- Initialize components for Routine "acquisition_end" ---
acquisition_end_text = visual.TextStim(win=win, name='acquisition_end_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "end_routine_trigger" ---

# --- Initialize components for Routine "end_experiment" ---

# --- Initialize components for Routine "start_routine_trigger" ---

# --- Initialize components for Routine "wait" ---
wait_text = visual.TextStim(win=win, name='wait_text',
    text='Waiting for experimenter',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "end_routine_trigger" ---

# --- Initialize components for Routine "stroop_instructions" ---
stroop_instruct_text = visual.TextStim(win=win, name='stroop_instruct_text',
    text='Your instructions go here.\n\nDuring the trial, you will see a word in the center of the screen. Your job is to indicate the color that word is printed in by pressing the corresponding key.\n\nIf the color of the word is RED, press the R key.\nIf the color of the word is GREEN, press the G key.\nIf the color of the word is BLUE, press the B key.\n\nPress SPACE to begin the practice.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "begin_timer" ---

# --- Initialize components for Routine "start_routine_trigger" ---

# --- Initialize components for Routine "stroop_trial" ---
trial_text = visual.TextStim(win=win, name='trial_text',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
text_20 = visual.TextStim(win=win, name='text_20',
    text='',
    font='Times New Roman',
    pos=(0, -.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_stroop = keyboard.Keyboard()

# --- Initialize components for Routine "stroop_feedback" ---
# Run 'Begin Experiment' code from code_14
msg = ""
feedback_text_3 = visual.TextStim(win=win, name='feedback_text_3',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "end_routine_trigger" ---

# --- Initialize components for Routine "practice_end" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='You have finished the practice trials. If you have any questions, please ask your experimenter now. \n\nNext, you will begin the real trials. These will be exactly the same, except you will no longer receive feedback.\n\nWhen you are ready, press SPACE to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "begin_timer" ---

# --- Initialize components for Routine "start_routine_trigger" ---

# --- Initialize components for Routine "stroop_trial" ---
trial_text = visual.TextStim(win=win, name='trial_text',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
text_20 = visual.TextStim(win=win, name='text_20',
    text='',
    font='Times New Roman',
    pos=(0, -.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_stroop = keyboard.Keyboard()

# --- Initialize components for Routine "stroop_feedback" ---
# Run 'Begin Experiment' code from code_14
msg = ""
feedback_text_3 = visual.TextStim(win=win, name='feedback_text_3',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "end_routine_trigger" ---

# --- Initialize components for Routine "begin_timer" ---

# --- Initialize components for Routine "start_routine_trigger" ---

# --- Initialize components for Routine "math_trial" ---
# Run 'Begin Experiment' code from code_4
math_correct = 0
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(.1, .15), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(.1, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(-0.05, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='=',
    font='Open Sans',
    pos=(0,0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_math = keyboard.Keyboard()

# --- Initialize components for Routine "math_feedback" ---
# Run 'Begin Experiment' code from code_6
msg = ""
feedback_text_2 = visual.TextStim(win=win, name='feedback_text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='Press SPACE to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_8 = keyboard.Keyboard()

# --- Initialize components for Routine "end_routine_trigger" ---

# --- Initialize components for Routine "begin_timer" ---

# --- Initialize components for Routine "start_routine_trigger" ---

# --- Initialize components for Routine "math_trial" ---
# Run 'Begin Experiment' code from code_4
math_correct = 0
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(.1, .15), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(.1, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(-0.05, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='=',
    font='Open Sans',
    pos=(0,0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_math = keyboard.Keyboard()

# --- Initialize components for Routine "end_routine_trigger" ---

# --- Initialize components for Routine "increment_selection" ---

# --- Initialize components for Routine "end" ---
end_text = visual.TextStim(win=win, name='end_text',
    text='You have reached the end of the experiment. Thank you! \n\nPress SPACE to end.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "setup" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = [setup_waiter]
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setup" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from exp_monitor
    if not pause_routine:
        continueRoutine=False
    
    # *setup_waiter* updates
    if setup_waiter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setup_waiter.frameNStart = frameN  # exact frame index
        setup_waiter.tStart = t  # local t and not account for scr refresh
        setup_waiter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setup_waiter, 'tStartRefresh')  # time at next scr refresh
        setup_waiter.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setup" ---
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=999.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(expInfo['scheduler csv']),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "parse_scheduler_row" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    parse_scheduler_rowComponents = [parse_waiter]
    for thisComponent in parse_scheduler_rowComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "parse_scheduler_row" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_7
        if not pause_routine:
            continueRoutine=False
        
        # *parse_waiter* updates
        if parse_waiter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            parse_waiter.frameNStart = frameN  # exact frame index
            parse_waiter.tStart = t  # local t and not account for scr refresh
            parse_waiter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(parse_waiter, 'tStartRefresh')  # time at next scr refresh
            parse_waiter.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in parse_scheduler_rowComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "parse_scheduler_row" ---
    for thisComponent in parse_scheduler_rowComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_7
    force_end_routine = False
    
    for key,val in scheduler_csv_data.iloc[current_selection].items():
            exec(key + '=val')
            
    if str(task_parameters) != 'nan':
        task_parameters = ast.literal_eval(task_parameters)
    else:
        task_parameters = {}
    # the Routine "parse_scheduler_row" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    acq_start = data.TrialHandler(nReps=sum([task_type=='acq_start']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='acq_start')
    thisExp.addLoop(acq_start)  # add the loop to the experiment
    thisAcq_start = acq_start.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAcq_start.rgb)
    if thisAcq_start != None:
        for paramName in thisAcq_start:
            exec('{} = thisAcq_start[paramName]'.format(paramName))
    
    for thisAcq_start in acq_start:
        currentLoop = acq_start
        # abbreviate parameter names if possible (e.g. rgb = thisAcq_start.rgb)
        if thisAcq_start != None:
            for paramName in thisAcq_start:
                exec('{} = thisAcq_start[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "start_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start_routine_trigger" ---
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "acquisition_start" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_11
        timer = core.CountdownTimer(duration)
        
        # keep track of which components have finished
        acquisition_startComponents = [acq_start_text]
        for thisComponent in acquisition_startComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "acquisition_start" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_11
            if force_end_routine or timer.getTime() <= 0:
                continueRoutine=False
                acq_start.finished=True
            
            # *acq_start_text* updates
            if acq_start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                acq_start_text.frameNStart = frameN  # exact frame index
                acq_start_text.tStart = t  # local t and not account for scr refresh
                acq_start_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(acq_start_text, 'tStartRefresh')  # time at next scr refresh
                acq_start_text.setAutoDraw(True)
            if acq_start_text.status == STARTED:  # only update if drawing
                acq_start_text.setText(str(round(timer.getTime(),2)) + '\n' + "Acquisition starting", log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in acquisition_startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "acquisition_start" ---
        for thisComponent in acquisition_startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "acquisition_start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "end_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "end_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end_routine_trigger" ---
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='acq_start']) repeats of 'acq_start'
    
    
    # set up handler to look after randomisation of conditions etc
    acq_end = data.TrialHandler(nReps=sum([task_type=='acq_end']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='acq_end')
    thisExp.addLoop(acq_end)  # add the loop to the experiment
    thisAcq_end = acq_end.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAcq_end.rgb)
    if thisAcq_end != None:
        for paramName in thisAcq_end:
            exec('{} = thisAcq_end[paramName]'.format(paramName))
    
    for thisAcq_end in acq_end:
        currentLoop = acq_end
        # abbreviate parameter names if possible (e.g. rgb = thisAcq_end.rgb)
        if thisAcq_end != None:
            for paramName in thisAcq_end:
                exec('{} = thisAcq_end[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "start_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start_routine_trigger" ---
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "acquisition_end" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        timer = core.CountdownTimer(duration)
        
        # keep track of which components have finished
        acquisition_endComponents = [acquisition_end_text]
        for thisComponent in acquisition_endComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "acquisition_end" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            if force_end_routine or timer.getTime() <= 0:
                continueRoutine=False
                acq_end.finished=True
            
            # *acquisition_end_text* updates
            if acquisition_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                acquisition_end_text.frameNStart = frameN  # exact frame index
                acquisition_end_text.tStart = t  # local t and not account for scr refresh
                acquisition_end_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(acquisition_end_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'acquisition_end_text.started')
                acquisition_end_text.setAutoDraw(True)
            if acquisition_end_text.status == STARTED:
                if bool(timer.getTime() <= -.01):
                    # keep track of stop time/frame for later
                    acquisition_end_text.tStop = t  # not accounting for scr refresh
                    acquisition_end_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'acquisition_end_text.stopped')
                    acquisition_end_text.setAutoDraw(False)
            if acquisition_end_text.status == STARTED:  # only update if drawing
                acquisition_end_text.setText(str(round(timer.getTime(),2)) + '\n' + "Acquisition ending", log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in acquisition_endComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "acquisition_end" ---
        for thisComponent in acquisition_endComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "acquisition_end" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "end_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "end_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end_routine_trigger" ---
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "end_experiment" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_13
        core.quit()
        # keep track of which components have finished
        end_experimentComponents = []
        for thisComponent in end_experimentComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "end_experiment" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_experimentComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end_experiment" ---
        for thisComponent in end_experimentComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_experiment" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='acq_end']) repeats of 'acq_end'
    
    
    # set up handler to look after randomisation of conditions etc
    wait_block = data.TrialHandler(nReps=sum([task_type=='wait']), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='wait_block')
    thisExp.addLoop(wait_block)  # add the loop to the experiment
    thisWait_block = wait_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWait_block.rgb)
    if thisWait_block != None:
        for paramName in thisWait_block:
            exec('{} = thisWait_block[paramName]'.format(paramName))
    
    for thisWait_block in wait_block:
        currentLoop = wait_block
        # abbreviate parameter names if possible (e.g. rgb = thisWait_block.rgb)
        if thisWait_block != None:
            for paramName in thisWait_block:
                exec('{} = thisWait_block[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "start_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start_routine_trigger" ---
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "wait" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_9
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        waitComponents = [wait_text]
        for thisComponent in waitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wait" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_9
            if force_end_routine and duration==0:
                continueRoutine=False
                wait_block.finished=True
            elif duration > 0 and (force_end_routine or timer.getTime() <= 0):
                continueRoutine=False
                wait_block.finished=True
            
            # *wait_text* updates
            if wait_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait_text.frameNStart = frameN  # exact frame index
                wait_text.tStart = t  # local t and not account for scr refresh
                wait_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait_text, 'tStartRefresh')  # time at next scr refresh
                wait_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in waitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wait" ---
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "wait" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "end_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "end_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end_routine_trigger" ---
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='wait']) repeats of 'wait_block'
    
    
    # set up handler to look after randomisation of conditions etc
    stroop_practice_block = data.TrialHandler(nReps=sum([task_type=='stroop_practice']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='stroop_practice_block')
    thisExp.addLoop(stroop_practice_block)  # add the loop to the experiment
    thisStroop_practice_block = stroop_practice_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStroop_practice_block.rgb)
    if thisStroop_practice_block != None:
        for paramName in thisStroop_practice_block:
            exec('{} = thisStroop_practice_block[paramName]'.format(paramName))
    
    for thisStroop_practice_block in stroop_practice_block:
        currentLoop = stroop_practice_block
        # abbreviate parameter names if possible (e.g. rgb = thisStroop_practice_block.rgb)
        if thisStroop_practice_block != None:
            for paramName in thisStroop_practice_block:
                exec('{} = thisStroop_practice_block[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "stroop_instructions" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        stroop_instructionsComponents = [stroop_instruct_text, key_resp_2]
        for thisComponent in stroop_instructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stroop_instructions" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stroop_instruct_text* updates
            if stroop_instruct_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stroop_instruct_text.frameNStart = frameN  # exact frame index
                stroop_instruct_text.tStart = t  # local t and not account for scr refresh
                stroop_instruct_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop_instruct_text, 'tStartRefresh')  # time at next scr refresh
                stroop_instruct_text.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stroop_instructions" ---
        for thisComponent in stroop_instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "stroop_instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "begin_timer" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_10
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        begin_timerComponents = []
        for thisComponent in begin_timerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "begin_timer" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begin_timerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "begin_timer" ---
        for thisComponent in begin_timerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "begin_timer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "start_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start_routine_trigger" ---
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        stroop_practice_trials = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('routine_conditions/stroop_stim.csv'),
            seed=None, name='stroop_practice_trials')
        thisExp.addLoop(stroop_practice_trials)  # add the loop to the experiment
        thisStroop_practice_trial = stroop_practice_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisStroop_practice_trial.rgb)
        if thisStroop_practice_trial != None:
            for paramName in thisStroop_practice_trial:
                exec('{} = thisStroop_practice_trial[paramName]'.format(paramName))
        
        for thisStroop_practice_trial in stroop_practice_trials:
            currentLoop = stroop_practice_trials
            # abbreviate parameter names if possible (e.g. rgb = thisStroop_practice_trial.rgb)
            if thisStroop_practice_trial != None:
                for paramName in thisStroop_practice_trial:
                    exec('{} = thisStroop_practice_trial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "stroop_trial" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_3
            win.setColor('black') 
            if task_parameters['language'] == "english":
                word = english_word
                sound_file = sound_file_english
                key_maps = ["red", "yellow", "green", "blue"]
            elif task_parameters['language'] == "spanish":
                word = spanish_word
                sound_file = sound_file_spanish
                key_maps = ["rojo", "amarillo", "verde", "azul"]
            trial_text.setColor(color, colorSpace='rgb')
            trial_text.setText(word)
            sound_2.setSound(sound_file, secs=presentation_time, hamming=True)
            sound_2.setVolume(1.0, log=False)
            text_20.setText((f"{key_maps[0]}\t\t{key_maps[1]}\t\t{key_maps[2]}\t\t{key_maps[3]}"))
            key_resp_stroop.keys = []
            key_resp_stroop.rt = []
            _key_resp_stroop_allKeys = []
            # keep track of which components have finished
            stroop_trialComponents = [trial_text, sound_2, text_20, key_resp_stroop]
            for thisComponent in stroop_trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "stroop_trial" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_3
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    stroop_trials.finished=True
                
                # *trial_text* updates
                if trial_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    trial_text.frameNStart = frameN  # exact frame index
                    trial_text.tStart = t  # local t and not account for scr refresh
                    trial_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(trial_text, 'tStartRefresh')  # time at next scr refresh
                    trial_text.setAutoDraw(True)
                if trial_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > trial_text.tStartRefresh + presentation_time-frameTolerance:
                        # keep track of stop time/frame for later
                        trial_text.tStop = t  # not accounting for scr refresh
                        trial_text.frameNStop = frameN  # exact frame index
                        trial_text.setAutoDraw(False)
                # start/stop sound_2
                if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sound_2.frameNStart = frameN  # exact frame index
                    sound_2.tStart = t  # local t and not account for scr refresh
                    sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                    sound_2.play(when=win)  # sync with win flip
                if sound_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_2.tStartRefresh + presentation_time-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_2.tStop = t  # not accounting for scr refresh
                        sound_2.frameNStop = frameN  # exact frame index
                        sound_2.stop()
                
                # *text_20* updates
                if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_20.frameNStart = frameN  # exact frame index
                    text_20.tStart = t  # local t and not account for scr refresh
                    text_20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
                    text_20.setAutoDraw(True)
                if text_20.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_20.tStartRefresh + presentation_time-frameTolerance:
                        # keep track of stop time/frame for later
                        text_20.tStop = t  # not accounting for scr refresh
                        text_20.frameNStop = frameN  # exact frame index
                        text_20.setAutoDraw(False)
                
                # *key_resp_stroop* updates
                waitOnFlip = False
                if key_resp_stroop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_stroop.frameNStart = frameN  # exact frame index
                    key_resp_stroop.tStart = t  # local t and not account for scr refresh
                    key_resp_stroop.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_stroop, 'tStartRefresh')  # time at next scr refresh
                    key_resp_stroop.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_stroop.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_stroop.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_stroop.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_stroop.getKeys(keyList=['4','5','6', '7', 'num_4', 'num_5', 'num_6', 'num_add'], waitRelease=False)
                    _key_resp_stroop_allKeys.extend(theseKeys)
                    if len(_key_resp_stroop_allKeys):
                        key_resp_stroop.keys = _key_resp_stroop_allKeys[-1].name  # just the last key pressed
                        key_resp_stroop.rt = _key_resp_stroop_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_stroop.keys == str(corr_ans)) or (key_resp_stroop.keys == corr_ans):
                            key_resp_stroop.corr = 1
                        else:
                            key_resp_stroop.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stroop_trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stroop_trial" ---
            for thisComponent in stroop_trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from code_3
            if (presentation_time > presentation_time_floor) and (key_resp_stroop.corr == 1):
                presentation_time -= .1
            elif key_resp_stroop.corr == 1:
                presentation_time += .1
            sound_2.stop()  # ensure sound has stopped at end of routine
            # check responses
            if key_resp_stroop.keys in ['', [], None]:  # No response was made
                key_resp_stroop.keys = None
                # was no response the correct answer?!
                if str(corr_ans).lower() == 'none':
                   key_resp_stroop.corr = 1;  # correct non-response
                else:
                   key_resp_stroop.corr = 0;  # failed to respond (incorrectly)
            # store data for stroop_practice_trials (TrialHandler)
            stroop_practice_trials.addData('key_resp_stroop.keys',key_resp_stroop.keys)
            stroop_practice_trials.addData('key_resp_stroop.corr', key_resp_stroop.corr)
            if key_resp_stroop.keys != None:  # we had a response
                stroop_practice_trials.addData('key_resp_stroop.rt', key_resp_stroop.rt)
            # the Routine "stroop_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stroop_feedback" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_14
            if key_resp_stroop.corr == 1:
                msg = "correct"
            else:
                msg = f"incorrect"
                
            bg_colors = ["red", "blue", "green"]
            shuffle(bg_colors)
            win.setColor(bg_colors[0]) 
            feedback_text_3.setText(msg)
            # keep track of which components have finished
            stroop_feedbackComponents = [feedback_text_3]
            for thisComponent in stroop_feedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "stroop_feedback" ---
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_14
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    stroop_trials.finished=True
                
                # *feedback_text_3* updates
                if feedback_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_3.frameNStart = frameN  # exact frame index
                    feedback_text_3.tStart = t  # local t and not account for scr refresh
                    feedback_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_3, 'tStartRefresh')  # time at next scr refresh
                    feedback_text_3.setAutoDraw(True)
                if feedback_text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text_3.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text_3.tStop = t  # not accounting for scr refresh
                        feedback_text_3.frameNStop = frameN  # exact frame index
                        feedback_text_3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stroop_feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stroop_feedback" ---
            for thisComponent in stroop_feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from code_14
            win.setColor('black') 
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'stroop_practice_trials'
        
        
        # --- Prepare to start Routine "end_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "end_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end_routine_trigger" ---
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practice_end" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        practice_endComponents = [text_7, key_resp_5]
        for thisComponent in practice_endComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_end" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_7* updates
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                text_7.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_endComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_end" ---
        for thisComponent in practice_endComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='stroop_practice']) repeats of 'stroop_practice_block'
    
    
    # set up handler to look after randomisation of conditions etc
    stroop = data.TrialHandler(nReps=sum([task_type=='stroop']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='stroop')
    thisExp.addLoop(stroop)  # add the loop to the experiment
    thisStroop = stroop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStroop.rgb)
    if thisStroop != None:
        for paramName in thisStroop:
            exec('{} = thisStroop[paramName]'.format(paramName))
    
    for thisStroop in stroop:
        currentLoop = stroop
        # abbreviate parameter names if possible (e.g. rgb = thisStroop.rgb)
        if thisStroop != None:
            for paramName in thisStroop:
                exec('{} = thisStroop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "begin_timer" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_10
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        begin_timerComponents = []
        for thisComponent in begin_timerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "begin_timer" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begin_timerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "begin_timer" ---
        for thisComponent in begin_timerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "begin_timer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "start_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start_routine_trigger" ---
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        stroop_trials = data.TrialHandler(nReps=10000.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('routine_conditions/stroop_stim.csv'),
            seed=None, name='stroop_trials')
        thisExp.addLoop(stroop_trials)  # add the loop to the experiment
        thisStroop_trial = stroop_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisStroop_trial.rgb)
        if thisStroop_trial != None:
            for paramName in thisStroop_trial:
                exec('{} = thisStroop_trial[paramName]'.format(paramName))
        
        for thisStroop_trial in stroop_trials:
            currentLoop = stroop_trials
            # abbreviate parameter names if possible (e.g. rgb = thisStroop_trial.rgb)
            if thisStroop_trial != None:
                for paramName in thisStroop_trial:
                    exec('{} = thisStroop_trial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "stroop_trial" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_3
            win.setColor('black') 
            if task_parameters['language'] == "english":
                word = english_word
                sound_file = sound_file_english
                key_maps = ["red", "yellow", "green", "blue"]
            elif task_parameters['language'] == "spanish":
                word = spanish_word
                sound_file = sound_file_spanish
                key_maps = ["rojo", "amarillo", "verde", "azul"]
            trial_text.setColor(color, colorSpace='rgb')
            trial_text.setText(word)
            sound_2.setSound(sound_file, secs=presentation_time, hamming=True)
            sound_2.setVolume(1.0, log=False)
            text_20.setText((f"{key_maps[0]}\t\t{key_maps[1]}\t\t{key_maps[2]}\t\t{key_maps[3]}"))
            key_resp_stroop.keys = []
            key_resp_stroop.rt = []
            _key_resp_stroop_allKeys = []
            # keep track of which components have finished
            stroop_trialComponents = [trial_text, sound_2, text_20, key_resp_stroop]
            for thisComponent in stroop_trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "stroop_trial" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_3
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    stroop_trials.finished=True
                
                # *trial_text* updates
                if trial_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    trial_text.frameNStart = frameN  # exact frame index
                    trial_text.tStart = t  # local t and not account for scr refresh
                    trial_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(trial_text, 'tStartRefresh')  # time at next scr refresh
                    trial_text.setAutoDraw(True)
                if trial_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > trial_text.tStartRefresh + presentation_time-frameTolerance:
                        # keep track of stop time/frame for later
                        trial_text.tStop = t  # not accounting for scr refresh
                        trial_text.frameNStop = frameN  # exact frame index
                        trial_text.setAutoDraw(False)
                # start/stop sound_2
                if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sound_2.frameNStart = frameN  # exact frame index
                    sound_2.tStart = t  # local t and not account for scr refresh
                    sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                    sound_2.play(when=win)  # sync with win flip
                if sound_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_2.tStartRefresh + presentation_time-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_2.tStop = t  # not accounting for scr refresh
                        sound_2.frameNStop = frameN  # exact frame index
                        sound_2.stop()
                
                # *text_20* updates
                if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_20.frameNStart = frameN  # exact frame index
                    text_20.tStart = t  # local t and not account for scr refresh
                    text_20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
                    text_20.setAutoDraw(True)
                if text_20.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_20.tStartRefresh + presentation_time-frameTolerance:
                        # keep track of stop time/frame for later
                        text_20.tStop = t  # not accounting for scr refresh
                        text_20.frameNStop = frameN  # exact frame index
                        text_20.setAutoDraw(False)
                
                # *key_resp_stroop* updates
                waitOnFlip = False
                if key_resp_stroop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_stroop.frameNStart = frameN  # exact frame index
                    key_resp_stroop.tStart = t  # local t and not account for scr refresh
                    key_resp_stroop.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_stroop, 'tStartRefresh')  # time at next scr refresh
                    key_resp_stroop.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_stroop.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_stroop.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_stroop.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_stroop.getKeys(keyList=['4','5','6', '7', 'num_4', 'num_5', 'num_6', 'num_add'], waitRelease=False)
                    _key_resp_stroop_allKeys.extend(theseKeys)
                    if len(_key_resp_stroop_allKeys):
                        key_resp_stroop.keys = _key_resp_stroop_allKeys[-1].name  # just the last key pressed
                        key_resp_stroop.rt = _key_resp_stroop_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_stroop.keys == str(corr_ans)) or (key_resp_stroop.keys == corr_ans):
                            key_resp_stroop.corr = 1
                        else:
                            key_resp_stroop.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stroop_trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stroop_trial" ---
            for thisComponent in stroop_trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from code_3
            if (presentation_time > presentation_time_floor) and (key_resp_stroop.corr == 1):
                presentation_time -= .1
            elif key_resp_stroop.corr == 1:
                presentation_time += .1
            sound_2.stop()  # ensure sound has stopped at end of routine
            # check responses
            if key_resp_stroop.keys in ['', [], None]:  # No response was made
                key_resp_stroop.keys = None
                # was no response the correct answer?!
                if str(corr_ans).lower() == 'none':
                   key_resp_stroop.corr = 1;  # correct non-response
                else:
                   key_resp_stroop.corr = 0;  # failed to respond (incorrectly)
            # store data for stroop_trials (TrialHandler)
            stroop_trials.addData('key_resp_stroop.keys',key_resp_stroop.keys)
            stroop_trials.addData('key_resp_stroop.corr', key_resp_stroop.corr)
            if key_resp_stroop.keys != None:  # we had a response
                stroop_trials.addData('key_resp_stroop.rt', key_resp_stroop.rt)
            # the Routine "stroop_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stroop_feedback" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_14
            if key_resp_stroop.corr == 1:
                msg = "correct"
            else:
                msg = f"incorrect"
                
            bg_colors = ["red", "blue", "green"]
            shuffle(bg_colors)
            win.setColor(bg_colors[0]) 
            feedback_text_3.setText(msg)
            # keep track of which components have finished
            stroop_feedbackComponents = [feedback_text_3]
            for thisComponent in stroop_feedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "stroop_feedback" ---
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_14
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    stroop_trials.finished=True
                
                # *feedback_text_3* updates
                if feedback_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_3.frameNStart = frameN  # exact frame index
                    feedback_text_3.tStart = t  # local t and not account for scr refresh
                    feedback_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_3, 'tStartRefresh')  # time at next scr refresh
                    feedback_text_3.setAutoDraw(True)
                if feedback_text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text_3.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text_3.tStop = t  # not accounting for scr refresh
                        feedback_text_3.frameNStop = frameN  # exact frame index
                        feedback_text_3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stroop_feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stroop_feedback" ---
            for thisComponent in stroop_feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from code_14
            win.setColor('black') 
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 10000.0 repeats of 'stroop_trials'
        
        
        # --- Prepare to start Routine "end_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "end_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end_routine_trigger" ---
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='stroop']) repeats of 'stroop'
    
    
    # set up handler to look after randomisation of conditions etc
    math_practice_block = data.TrialHandler(nReps=sum([task_type=='math_practice']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='math_practice_block')
    thisExp.addLoop(math_practice_block)  # add the loop to the experiment
    thisMath_practice_block = math_practice_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMath_practice_block.rgb)
    if thisMath_practice_block != None:
        for paramName in thisMath_practice_block:
            exec('{} = thisMath_practice_block[paramName]'.format(paramName))
    
    for thisMath_practice_block in math_practice_block:
        currentLoop = math_practice_block
        # abbreviate parameter names if possible (e.g. rgb = thisMath_practice_block.rgb)
        if thisMath_practice_block != None:
            for paramName in thisMath_practice_block:
                exec('{} = thisMath_practice_block[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "begin_timer" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_10
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        begin_timerComponents = []
        for thisComponent in begin_timerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "begin_timer" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begin_timerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "begin_timer" ---
        for thisComponent in begin_timerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "begin_timer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "start_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start_routine_trigger" ---
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        math_practice_trials = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('routine_conditions/math_stim.csv'),
            seed=None, name='math_practice_trials')
        thisExp.addLoop(math_practice_trials)  # add the loop to the experiment
        thisMath_practice_trial = math_practice_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMath_practice_trial.rgb)
        if thisMath_practice_trial != None:
            for paramName in thisMath_practice_trial:
                exec('{} = thisMath_practice_trial[paramName]'.format(paramName))
        
        for thisMath_practice_trial in math_practice_trials:
            currentLoop = math_practice_trials
            # abbreviate parameter names if possible (e.g. rgb = thisMath_practice_trial.rgb)
            if thisMath_practice_trial != None:
                for paramName in thisMath_practice_trial:
                    exec('{} = thisMath_practice_trial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "math_trial" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_4
            win.setColor('black') 
            if start_math_difficulty == 1:
                num1 = randint(1,9)
                num2 = randint(1,9)
            elif start_math_difficulty == 2:
                num1 = randint(10,99)
                num2 = randint(1,9)
            elif start_math_difficulty == 3:
                num1 = randint(10,99)
                num2 = randint(10,99)
            elif start_math_difficulty == 4:
                num1 = randint(100,999)
                num2 = randint(10,99)
            elif start_math_difficulty == 5:
                num1 = randint(100,999)
                num2 = randint(100,999)
            
            if answer_condition == "same":
                corr_resp = "5"
                if trial_sign == "addition":
                    sign = "+"
                    answer = num1 + num2
                elif trial_sign == "subtraction":
                    sign = "-"
                    answer = num1 - num2
            elif answer_condition == "different":
                corr_resp = "6"
                if trial_sign == "addition":
                    sign = "+"
                    answer = num1 + randint(1,9) - num2 + randint(1,9)
                elif trial_sign == "subtraction":
                    sign = "-"
                    answer = num1 + randint(1,9) - num2 + randint(1,9)
            
            
            text.setText(num1)
            text_2.setText(num2)
            text_3.setText(sign)
            text_13.setText(answer)
            key_resp_math.keys = []
            key_resp_math.rt = []
            _key_resp_math_allKeys = []
            # keep track of which components have finished
            math_trialComponents = [text, text_2, text_3, text_15, text_13, key_resp_math]
            for thisComponent in math_trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "math_trial" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_4
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    math_trials.finished=True
                
                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    text.setAutoDraw(True)
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + math_num_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.frameNStop = frameN  # exact frame index
                        text.setAutoDraw(False)
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + math_num_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        text_2.setAutoDraw(False)
                
                # *text_3* updates
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    text_3.setAutoDraw(True)
                if text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_3.tStartRefresh + math_num_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_3.tStop = t  # not accounting for scr refresh
                        text_3.frameNStop = frameN  # exact frame index
                        text_3.setAutoDraw(False)
                
                # *text_15* updates
                if text_15.status == NOT_STARTED and tThisFlip >= (math_num_dur + equal_delay)-frameTolerance:
                    # keep track of start time/frame for later
                    text_15.frameNStart = frameN  # exact frame index
                    text_15.tStart = t  # local t and not account for scr refresh
                    text_15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
                    text_15.setAutoDraw(True)
                if text_15.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_15.tStartRefresh + equal_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_15.tStop = t  # not accounting for scr refresh
                        text_15.frameNStop = frameN  # exact frame index
                        text_15.setAutoDraw(False)
                
                # *text_13* updates
                if text_13.status == NOT_STARTED and tThisFlip >= (math_num_dur + equal_delay + equal_dur + math_answer_delay)-frameTolerance:
                    # keep track of start time/frame for later
                    text_13.frameNStart = frameN  # exact frame index
                    text_13.tStart = t  # local t and not account for scr refresh
                    text_13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
                    text_13.setAutoDraw(True)
                if text_13.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_13.tStartRefresh + math_answer_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_13.tStop = t  # not accounting for scr refresh
                        text_13.frameNStop = frameN  # exact frame index
                        text_13.setAutoDraw(False)
                
                # *key_resp_math* updates
                waitOnFlip = False
                if key_resp_math.status == NOT_STARTED and tThisFlip >= (math_num_dur + equal_delay + equal_dur + math_answer_delay)-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_math.frameNStart = frameN  # exact frame index
                    key_resp_math.tStart = t  # local t and not account for scr refresh
                    key_resp_math.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_math, 'tStartRefresh')  # time at next scr refresh
                    key_resp_math.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_math.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_math.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_math.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_math.getKeys(keyList=['5','6'], waitRelease=False)
                    _key_resp_math_allKeys.extend(theseKeys)
                    if len(_key_resp_math_allKeys):
                        key_resp_math.keys = _key_resp_math_allKeys[-1].name  # just the last key pressed
                        key_resp_math.rt = _key_resp_math_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_math.keys == str(corr_resp)) or (key_resp_math.keys == corr_resp):
                            key_resp_math.corr = 1
                        else:
                            key_resp_math.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in math_trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "math_trial" ---
            for thisComponent in math_trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from code_4
            if (key_resp_math.corr == 1) and (start_math_difficulty < 5):
                start_math_difficulty += 1
            elif (key_resp_math.corr == 0) and (start_math_difficulty > 1):
                start_math_difficulty -= 1
            # check responses
            if key_resp_math.keys in ['', [], None]:  # No response was made
                key_resp_math.keys = None
                # was no response the correct answer?!
                if str(corr_resp).lower() == 'none':
                   key_resp_math.corr = 1;  # correct non-response
                else:
                   key_resp_math.corr = 0;  # failed to respond (incorrectly)
            # store data for math_practice_trials (TrialHandler)
            math_practice_trials.addData('key_resp_math.keys',key_resp_math.keys)
            math_practice_trials.addData('key_resp_math.corr', key_resp_math.corr)
            if key_resp_math.keys != None:  # we had a response
                math_practice_trials.addData('key_resp_math.rt', key_resp_math.rt)
            # the Routine "math_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "math_feedback" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_6
            if math_correct == 1:
                msg = "Correct!"
            else:
                msg = "Incorrect."
            
            feedback_text_2.setText(msg)
            key_resp_8.keys = []
            key_resp_8.rt = []
            _key_resp_8_allKeys = []
            # keep track of which components have finished
            math_feedbackComponents = [feedback_text_2, text_9, key_resp_8]
            for thisComponent in math_feedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "math_feedback" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_6
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    math_practice_trials.finished=True
                
                # *feedback_text_2* updates
                if feedback_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_2.frameNStart = frameN  # exact frame index
                    feedback_text_2.tStart = t  # local t and not account for scr refresh
                    feedback_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_2, 'tStartRefresh')  # time at next scr refresh
                    feedback_text_2.setAutoDraw(True)
                
                # *text_9* updates
                if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_9.frameNStart = frameN  # exact frame index
                    text_9.tStart = t  # local t and not account for scr refresh
                    text_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                    text_9.setAutoDraw(True)
                
                # *key_resp_8* updates
                waitOnFlip = False
                if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_8.frameNStart = frameN  # exact frame index
                    key_resp_8.tStart = t  # local t and not account for scr refresh
                    key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                    key_resp_8.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_8.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_8_allKeys.extend(theseKeys)
                    if len(_key_resp_8_allKeys):
                        key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                        key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in math_feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "math_feedback" ---
            for thisComponent in math_feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "math_feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'math_practice_trials'
        
        
        # --- Prepare to start Routine "end_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "end_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end_routine_trigger" ---
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='math_practice']) repeats of 'math_practice_block'
    
    
    # set up handler to look after randomisation of conditions etc
    math = data.TrialHandler(nReps=sum([task_type=='math']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='math')
    thisExp.addLoop(math)  # add the loop to the experiment
    thisMath = math.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMath.rgb)
    if thisMath != None:
        for paramName in thisMath:
            exec('{} = thisMath[paramName]'.format(paramName))
    
    for thisMath in math:
        currentLoop = math
        # abbreviate parameter names if possible (e.g. rgb = thisMath.rgb)
        if thisMath != None:
            for paramName in thisMath:
                exec('{} = thisMath[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "begin_timer" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_10
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        begin_timerComponents = []
        for thisComponent in begin_timerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "begin_timer" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begin_timerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "begin_timer" ---
        for thisComponent in begin_timerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "begin_timer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "start_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start_routine_trigger" ---
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        math_trials = data.TrialHandler(nReps=10000.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('routine_conditions/math_stim.csv'),
            seed=None, name='math_trials')
        thisExp.addLoop(math_trials)  # add the loop to the experiment
        thisMath_trial = math_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMath_trial.rgb)
        if thisMath_trial != None:
            for paramName in thisMath_trial:
                exec('{} = thisMath_trial[paramName]'.format(paramName))
        
        for thisMath_trial in math_trials:
            currentLoop = math_trials
            # abbreviate parameter names if possible (e.g. rgb = thisMath_trial.rgb)
            if thisMath_trial != None:
                for paramName in thisMath_trial:
                    exec('{} = thisMath_trial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "math_trial" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_4
            win.setColor('black') 
            if start_math_difficulty == 1:
                num1 = randint(1,9)
                num2 = randint(1,9)
            elif start_math_difficulty == 2:
                num1 = randint(10,99)
                num2 = randint(1,9)
            elif start_math_difficulty == 3:
                num1 = randint(10,99)
                num2 = randint(10,99)
            elif start_math_difficulty == 4:
                num1 = randint(100,999)
                num2 = randint(10,99)
            elif start_math_difficulty == 5:
                num1 = randint(100,999)
                num2 = randint(100,999)
            
            if answer_condition == "same":
                corr_resp = "5"
                if trial_sign == "addition":
                    sign = "+"
                    answer = num1 + num2
                elif trial_sign == "subtraction":
                    sign = "-"
                    answer = num1 - num2
            elif answer_condition == "different":
                corr_resp = "6"
                if trial_sign == "addition":
                    sign = "+"
                    answer = num1 + randint(1,9) - num2 + randint(1,9)
                elif trial_sign == "subtraction":
                    sign = "-"
                    answer = num1 + randint(1,9) - num2 + randint(1,9)
            
            
            text.setText(num1)
            text_2.setText(num2)
            text_3.setText(sign)
            text_13.setText(answer)
            key_resp_math.keys = []
            key_resp_math.rt = []
            _key_resp_math_allKeys = []
            # keep track of which components have finished
            math_trialComponents = [text, text_2, text_3, text_15, text_13, key_resp_math]
            for thisComponent in math_trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "math_trial" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_4
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    math_trials.finished=True
                
                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    text.setAutoDraw(True)
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + math_num_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.frameNStop = frameN  # exact frame index
                        text.setAutoDraw(False)
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + math_num_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        text_2.setAutoDraw(False)
                
                # *text_3* updates
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    text_3.setAutoDraw(True)
                if text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_3.tStartRefresh + math_num_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_3.tStop = t  # not accounting for scr refresh
                        text_3.frameNStop = frameN  # exact frame index
                        text_3.setAutoDraw(False)
                
                # *text_15* updates
                if text_15.status == NOT_STARTED and tThisFlip >= (math_num_dur + equal_delay)-frameTolerance:
                    # keep track of start time/frame for later
                    text_15.frameNStart = frameN  # exact frame index
                    text_15.tStart = t  # local t and not account for scr refresh
                    text_15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
                    text_15.setAutoDraw(True)
                if text_15.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_15.tStartRefresh + equal_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_15.tStop = t  # not accounting for scr refresh
                        text_15.frameNStop = frameN  # exact frame index
                        text_15.setAutoDraw(False)
                
                # *text_13* updates
                if text_13.status == NOT_STARTED and tThisFlip >= (math_num_dur + equal_delay + equal_dur + math_answer_delay)-frameTolerance:
                    # keep track of start time/frame for later
                    text_13.frameNStart = frameN  # exact frame index
                    text_13.tStart = t  # local t and not account for scr refresh
                    text_13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
                    text_13.setAutoDraw(True)
                if text_13.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_13.tStartRefresh + math_answer_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        text_13.tStop = t  # not accounting for scr refresh
                        text_13.frameNStop = frameN  # exact frame index
                        text_13.setAutoDraw(False)
                
                # *key_resp_math* updates
                waitOnFlip = False
                if key_resp_math.status == NOT_STARTED and tThisFlip >= (math_num_dur + equal_delay + equal_dur + math_answer_delay)-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_math.frameNStart = frameN  # exact frame index
                    key_resp_math.tStart = t  # local t and not account for scr refresh
                    key_resp_math.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_math, 'tStartRefresh')  # time at next scr refresh
                    key_resp_math.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_math.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_math.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_math.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_math.getKeys(keyList=['5','6'], waitRelease=False)
                    _key_resp_math_allKeys.extend(theseKeys)
                    if len(_key_resp_math_allKeys):
                        key_resp_math.keys = _key_resp_math_allKeys[-1].name  # just the last key pressed
                        key_resp_math.rt = _key_resp_math_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_math.keys == str(corr_resp)) or (key_resp_math.keys == corr_resp):
                            key_resp_math.corr = 1
                        else:
                            key_resp_math.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in math_trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "math_trial" ---
            for thisComponent in math_trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from code_4
            if (key_resp_math.corr == 1) and (start_math_difficulty < 5):
                start_math_difficulty += 1
            elif (key_resp_math.corr == 0) and (start_math_difficulty > 1):
                start_math_difficulty -= 1
            # check responses
            if key_resp_math.keys in ['', [], None]:  # No response was made
                key_resp_math.keys = None
                # was no response the correct answer?!
                if str(corr_resp).lower() == 'none':
                   key_resp_math.corr = 1;  # correct non-response
                else:
                   key_resp_math.corr = 0;  # failed to respond (incorrectly)
            # store data for math_trials (TrialHandler)
            math_trials.addData('key_resp_math.keys',key_resp_math.keys)
            math_trials.addData('key_resp_math.corr', key_resp_math.corr)
            if key_resp_math.keys != None:  # we had a response
                math_trials.addData('key_resp_math.rt', key_resp_math.rt)
            # the Routine "math_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 10000.0 repeats of 'math_trials'
        
        
        # --- Prepare to start Routine "end_routine_trigger" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "end_routine_trigger" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end_routine_trigger" ---
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='math']) repeats of 'math'
    
    
    # --- Prepare to start Routine "increment_selection" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_12
    import asyncio
    import websockets
     
    async def increment():
        async with websockets.connect('ws://localhost:8000') as websocket:
            await websocket.send("next")
            response = await websocket.recv()
            print(response)
    if not force_end_routine and not pause_routine: # if user didn't give input
        asyncio.get_event_loop().run_until_complete(increment())
    # keep track of which components have finished
    increment_selectionComponents = []
    for thisComponent in increment_selectionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "increment_selection" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in increment_selectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "increment_selection" ---
    for thisComponent in increment_selectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "increment_selection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 999.0 repeats of 'trials'


# --- Prepare to start Routine "end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
endComponents = [end_text, key_resp_3]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
