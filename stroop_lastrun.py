#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.3),
    on August 24, 2022, at 15:22
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.3')


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
psychopyVersion = '2022.2.3'
expName = 'scheduler'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'condition': '',
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
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Bmed\\Documents\\bmed_data_acq\\stroop_lastrun.py',
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
    size=[600, 400], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
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
# Run 'Begin Experiment' code from code_setup
from psychopy.hardware import keyboard
from psychopy import core
exp_condition = expInfo['condition'] 

p_port = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "parse_scheduler_row" ---

# --- Initialize components for Routine "acquisition_start_2" ---
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
p_port_x_send_6 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "wait_2" ---
text_10 = visual.TextStim(win=win, name='text_10',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
p_port_x_send_5 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "stroop_instructions" ---
stroop_instruct_text = visual.TextStim(win=win, name='stroop_instruct_text',
    text='Your instructions go here.\n\nDuring the trial, you will see a word in the center of the screen. Your job is to indicate the color that word is printed in by pressing the corresponding key.\n\nIf the color of the word is RED, press the R key.\nIf the color of the word is GREEN, press the G key.\nIf the color of the word is BLUE, press the B key.\n\nPress SPACE to begin the practice.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "stroop_practice" ---
stroop_practice_text = visual.TextStim(win=win, name='stroop_practice_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_stroop_prac = keyboard.Keyboard()

# --- Initialize components for Routine "stroop_feedback" ---
# Run 'Begin Experiment' code from code
msg = ""
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='Press SPACE to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "practice_end" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='You have finished the practice trials. If you have any questions, please ask your experimenter now. \n\nNext, you will begin the real trials. These will be exactly the same, except you will no longer receive feedback.\n\nWhen you are ready, press SPACE to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "stroop_trial" ---
trial_text = visual.TextStim(win=win, name='trial_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "math_practice" ---
# Run 'Begin Experiment' code from code_5
math_correct = 0
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(-.25, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Open Sans',
    pos=(.25, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
textbox_2 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -.25),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox_2',
     autoLog=True,
)

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

# --- Initialize components for Routine "begin_timer" ---

# --- Initialize components for Routine "math_trial" ---
# Run 'Begin Experiment' code from code_4
math_correct = 0
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(-.25, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(.25, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -.25),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)

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
setupComponents = [p_port]
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
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *p_port* updates
    if p_port.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        p_port.frameNStart = frameN  # exact frame index
        p_port.tStart = t  # local t and not account for scr refresh
        p_port.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(p_port, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('p_port.started', t)
        p_port.status = STARTED
        win.callOnFlip(p_port.setData, int(128))
    if p_port.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > p_port.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            p_port.tStop = t  # not accounting for scr refresh
            p_port.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('p_port.stopped', t)
            p_port.status = FINISHED
            win.callOnFlip(p_port.setData, int(129))
    
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
if p_port.status == STARTED:
    win.callOnFlip(p_port.setData, int(129))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block_scheduler.csv'),
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
    # Run 'Begin Routine' code from code_7
    if task_parameters:
        task_parameters = ast.literal_eval(task_parameters)
    # keep track of which components have finished
    parse_scheduler_rowComponents = []
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
        
        # --- Prepare to start Routine "acquisition_start_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_11
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        acquisition_start_2Components = [text_11, p_port_x_send_6]
        for thisComponent in acquisition_start_2Components:
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
        
        # --- Run Routine "acquisition_start_2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_11* updates
            if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_11.started')
                text_11.setAutoDraw(True)
            if text_11.status == STARTED:
                if bool(timer.getTime() <= 0):
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_11.stopped')
                    text_11.setAutoDraw(False)
            if text_11.status == STARTED:  # only update if drawing
                text_11.setText(str(round(timer.getTime(),2)) + '\n' + "Acquisition starting", log=False)
            # *p_port_x_send_6* updates
            if p_port_x_send_6.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                p_port_x_send_6.frameNStart = frameN  # exact frame index
                p_port_x_send_6.tStart = t  # local t and not account for scr refresh
                p_port_x_send_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_x_send_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_x_send_6.started', t)
                p_port_x_send_6.status = STARTED
                win.callOnFlip(p_port_x_send_6.setData, int(start_trigger))
            if p_port_x_send_6.status == STARTED:
                if bool(timer.getTime() <= 0):
                    # keep track of stop time/frame for later
                    p_port_x_send_6.tStop = t  # not accounting for scr refresh
                    p_port_x_send_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_x_send_6.stopped', t)
                    p_port_x_send_6.status = FINISHED
                    win.callOnFlip(p_port_x_send_6.setData, int(end_trigger))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in acquisition_start_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "acquisition_start_2" ---
        for thisComponent in acquisition_start_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if p_port_x_send_6.status == STARTED:
            win.callOnFlip(p_port_x_send_6.setData, int(end_trigger))
        # the Routine "acquisition_start_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='acq_start']) repeats of 'acq_start'
    
    
    # set up handler to look after randomisation of conditions etc
    wait = data.TrialHandler(nReps=sum([task_type=='wait']), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='wait')
    thisExp.addLoop(wait)  # add the loop to the experiment
    thisWait = wait.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWait.rgb)
    if thisWait != None:
        for paramName in thisWait:
            exec('{} = thisWait[paramName]'.format(paramName))
    
    for thisWait in wait:
        currentLoop = wait
        # abbreviate parameter names if possible (e.g. rgb = thisWait.rgb)
        if thisWait != None:
            for paramName in thisWait:
                exec('{} = thisWait[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "wait_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_9
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        wait_2Components = [text_10, p_port_x_send_5]
        for thisComponent in wait_2Components:
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
        
        # --- Run Routine "wait_2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_10* updates
            if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_10.started')
                text_10.setAutoDraw(True)
            if text_10.status == STARTED:
                if bool(timer.getTime() <= 0):
                    # keep track of stop time/frame for later
                    text_10.tStop = t  # not accounting for scr refresh
                    text_10.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_10.stopped')
                    text_10.setAutoDraw(False)
            if text_10.status == STARTED:  # only update if drawing
                text_10.setText(str(round(timer.getTime(),2)) + '\n' + "Waiting", log=False)
            # *p_port_x_send_5* updates
            if p_port_x_send_5.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                p_port_x_send_5.frameNStart = frameN  # exact frame index
                p_port_x_send_5.tStart = t  # local t and not account for scr refresh
                p_port_x_send_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_x_send_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_x_send_5.started', t)
                p_port_x_send_5.status = STARTED
                win.callOnFlip(p_port_x_send_5.setData, int(start_trigger))
            if p_port_x_send_5.status == STARTED:
                if bool(timer.getTime() <= 0):
                    # keep track of stop time/frame for later
                    p_port_x_send_5.tStop = t  # not accounting for scr refresh
                    p_port_x_send_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_x_send_5.stopped', t)
                    p_port_x_send_5.status = FINISHED
                    win.callOnFlip(p_port_x_send_5.setData, int(end_trigger))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wait_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wait_2" ---
        for thisComponent in wait_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if p_port_x_send_5.status == STARTED:
            win.callOnFlip(p_port_x_send_5.setData, int(end_trigger))
        # the Routine "wait_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='wait']) repeats of 'wait'
    
    
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
        
        # set up handler to look after randomisation of conditions etc
        stroop_trials_practice = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('stroop_stim.csv'),
            seed=None, name='stroop_trials_practice')
        thisExp.addLoop(stroop_trials_practice)  # add the loop to the experiment
        thisStroop_trials_practice = stroop_trials_practice.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisStroop_trials_practice.rgb)
        if thisStroop_trials_practice != None:
            for paramName in thisStroop_trials_practice:
                exec('{} = thisStroop_trials_practice[paramName]'.format(paramName))
        
        for thisStroop_trials_practice in stroop_trials_practice:
            currentLoop = stroop_trials_practice
            # abbreviate parameter names if possible (e.g. rgb = thisStroop_trials_practice.rgb)
            if thisStroop_trials_practice != None:
                for paramName in thisStroop_trials_practice:
                    exec('{} = thisStroop_trials_practice[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "stroop_practice" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_2
            if color == "red":
                corr_ans = "r"
            elif color == "green":
                corr_ans = "g"
            else:
                corr_ans = "b"
            stroop_practice_text.setColor(color, colorSpace='rgb')
            stroop_practice_text.setText(word)
            key_resp_stroop_prac.keys = []
            key_resp_stroop_prac.rt = []
            _key_resp_stroop_prac_allKeys = []
            # keep track of which components have finished
            stroop_practiceComponents = [stroop_practice_text, key_resp_stroop_prac]
            for thisComponent in stroop_practiceComponents:
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
            
            # --- Run Routine "stroop_practice" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *stroop_practice_text* updates
                if stroop_practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stroop_practice_text.frameNStart = frameN  # exact frame index
                    stroop_practice_text.tStart = t  # local t and not account for scr refresh
                    stroop_practice_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stroop_practice_text, 'tStartRefresh')  # time at next scr refresh
                    stroop_practice_text.setAutoDraw(True)
                
                # *key_resp_stroop_prac* updates
                waitOnFlip = False
                if key_resp_stroop_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_stroop_prac.frameNStart = frameN  # exact frame index
                    key_resp_stroop_prac.tStart = t  # local t and not account for scr refresh
                    key_resp_stroop_prac.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_stroop_prac, 'tStartRefresh')  # time at next scr refresh
                    key_resp_stroop_prac.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_stroop_prac.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_stroop_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_stroop_prac.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_stroop_prac.getKeys(keyList=['r','g','b'], waitRelease=False)
                    _key_resp_stroop_prac_allKeys.extend(theseKeys)
                    if len(_key_resp_stroop_prac_allKeys):
                        key_resp_stroop_prac.keys = _key_resp_stroop_prac_allKeys[-1].name  # just the last key pressed
                        key_resp_stroop_prac.rt = _key_resp_stroop_prac_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_stroop_prac.keys == str(corr_ans)) or (key_resp_stroop_prac.keys == corr_ans):
                            key_resp_stroop_prac.corr = 1
                        else:
                            key_resp_stroop_prac.corr = 0
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
                for thisComponent in stroop_practiceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stroop_practice" ---
            for thisComponent in stroop_practiceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_stroop_prac.keys in ['', [], None]:  # No response was made
                key_resp_stroop_prac.keys = None
                # was no response the correct answer?!
                if str(corr_ans).lower() == 'none':
                   key_resp_stroop_prac.corr = 1;  # correct non-response
                else:
                   key_resp_stroop_prac.corr = 0;  # failed to respond (incorrectly)
            # store data for stroop_trials_practice (TrialHandler)
            stroop_trials_practice.addData('key_resp_stroop_prac.keys',key_resp_stroop_prac.keys)
            stroop_trials_practice.addData('key_resp_stroop_prac.corr', key_resp_stroop_prac.corr)
            if key_resp_stroop_prac.keys != None:  # we had a response
                stroop_trials_practice.addData('key_resp_stroop_prac.rt', key_resp_stroop_prac.rt)
            # the Routine "stroop_practice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stroop_feedback" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code
            if key_resp_stroop_prac.corr == 1:
                msg = "Correct!"
            elif color == "red":
                msg = "That was incorrect. The color was red, so you should have pressed the R key."
            elif color == "green":
                msg = "That was incorrect. The color was green, so you should have pressed the G key."
            else:
                msg = "That was incorrect. The color was blue, so you should have pressed the B key."
            
            feedback_text.setText(msg)
            key_resp_4.keys = []
            key_resp_4.rt = []
            _key_resp_4_allKeys = []
            # keep track of which components have finished
            stroop_feedbackComponents = [feedback_text, text_5, key_resp_4]
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
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text* updates
                if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text.frameNStart = frameN  # exact frame index
                    feedback_text.tStart = t  # local t and not account for scr refresh
                    feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                    feedback_text.setAutoDraw(True)
                
                # *text_5* updates
                if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_5.frameNStart = frameN  # exact frame index
                    text_5.tStart = t  # local t and not account for scr refresh
                    text_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                    text_5.setAutoDraw(True)
                
                # *key_resp_4* updates
                waitOnFlip = False
                if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.tStart = t  # local t and not account for scr refresh
                    key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_4.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_4_allKeys.extend(theseKeys)
                    if len(_key_resp_4_allKeys):
                        key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                        key_resp_4.rt = _key_resp_4_allKeys[-1].rt
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
            # the Routine "stroop_feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'stroop_trials_practice'
        
        
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
        # Run 'End Routine' code from code_8
        timer = core.CountdownTimer(duration)
        # the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        stroop_trials = data.TrialHandler(nReps=10000.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('stroop_stim.csv'),
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
            if color == "red":
                corr_ans = "r"
            elif color == "green":
                corr_ans = "g"
            else:
                corr_ans = "b"
            trial_text.setColor(color, colorSpace='rgb')
            trial_text.setText(word)
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            # keep track of which components have finished
            stroop_trialComponents = [trial_text, key_resp]
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
                if timer.getTime() <= 0:
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
                
                # *key_resp* updates
                waitOnFlip = False
                if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp.frameNStart = frameN  # exact frame index
                    key_resp.tStart = t  # local t and not account for scr refresh
                    key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp.getKeys(keyList=['r','g','b'], waitRelease=False)
                    _key_resp_allKeys.extend(theseKeys)
                    if len(_key_resp_allKeys):
                        key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                        key_resp.rt = _key_resp_allKeys[-1].rt
                        # was this correct?
                        if (key_resp.keys == str(corr_ans)) or (key_resp.keys == corr_ans):
                            key_resp.corr = 1
                        else:
                            key_resp.corr = 0
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
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
                # was no response the correct answer?!
                if str(corr_ans).lower() == 'none':
                   key_resp.corr = 1;  # correct non-response
                else:
                   key_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for stroop_trials (TrialHandler)
            stroop_trials.addData('key_resp.keys',key_resp.keys)
            stroop_trials.addData('key_resp.corr', key_resp.corr)
            if key_resp.keys != None:  # we had a response
                stroop_trials.addData('key_resp.rt', key_resp.rt)
            # the Routine "stroop_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 10000.0 repeats of 'stroop_trials'
        
        thisExp.nextEntry()
        
    # completed sum([task_type=='stroop']) repeats of 'stroop'
    
    
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
        
        # set up handler to look after randomisation of conditions etc
        math_trials_practice = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('math_stim.csv'),
            seed=None, name='math_trials_practice')
        thisExp.addLoop(math_trials_practice)  # add the loop to the experiment
        thisMath_trials_practice = math_trials_practice.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMath_trials_practice.rgb)
        if thisMath_trials_practice != None:
            for paramName in thisMath_trials_practice:
                exec('{} = thisMath_trials_practice[paramName]'.format(paramName))
        
        for thisMath_trials_practice in math_trials_practice:
            currentLoop = math_trials_practice
            # abbreviate parameter names if possible (e.g. rgb = thisMath_trials_practice.rgb)
            if thisMath_trials_practice != None:
                for paramName in thisMath_trials_practice:
                    exec('{} = thisMath_trials_practice[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "math_practice" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_5
            num1 = randint(1,11)
            num2 = randint(1,11)
            
            if trial_sign == "addition":
                sign = "+"
                corr_ans_math = num1 + num2
            elif trial_sign == "subtraction":
                sign = "-"
                corr_ans_math = num1 - num2
            elif trial_sign == "division":
                sign = "/"
                corr_ans_math = num1 / num2
            else:
                sign = "x"
                corr_ans_math = num1 * num2
            math_kb = keyboard.Keyboard()
            response_rt = 0
            text_4.setText(num1)
            text_6.setText(num2)
            text_8.setText(sign)
            textbox_2.reset()
            # keep track of which components have finished
            math_practiceComponents = [text_4, text_6, text_8, textbox_2]
            for thisComponent in math_practiceComponents:
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
            
            # --- Run Routine "math_practice" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_5
                math_keys = math_kb.getKeys()
                valid_keys = ['1','2','3','4',
                '5','6','7','8','9','0','minus', 'return']
                for thisKey in math_keys:
                    if thisKey.name == 'escape':
                        core.quit()
                    if thisKey.name not in valid_keys:
                        textbox_2.text = ''
                    elif (textbox_2.text != '') and (thisKey.name == 'return'):
                        response_rt = thisKey.rt
                        continueRoutine = False
                
                # *text_4* updates
                if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(True)
                
                # *text_6* updates
                if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_6.frameNStart = frameN  # exact frame index
                    text_6.tStart = t  # local t and not account for scr refresh
                    text_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                    text_6.setAutoDraw(True)
                
                # *text_8* updates
                if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_8.frameNStart = frameN  # exact frame index
                    text_8.tStart = t  # local t and not account for scr refresh
                    text_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                    text_8.setAutoDraw(True)
                
                # *textbox_2* updates
                if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox_2.frameNStart = frameN  # exact frame index
                    textbox_2.tStart = t  # local t and not account for scr refresh
                    textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
                    textbox_2.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in math_practiceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "math_practice" ---
            for thisComponent in math_practiceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from code_5
            answer = int(textbox_2.text)
            
            print(f"Submitted: {answer}, {type(answer)}")
            print(f"Correct: {corr_ans_math}, {type(corr_ans_math)}")
            
            if int(answer) == int(corr_ans_math):
                math_correct = 1
            else:
                math_correct = 0
            
            thisExp.addData('corr_ans_math', corr_ans_math)
            thisExp.addData('math_correct', math_correct)
            thisExp.addData('response_rt', response_rt)
            math_trials_practice.addData('textbox_2.text',textbox_2.text)
            # the Routine "math_practice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "math_feedback" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_6
            if math_correct == 1:
                msg = "Correct!"
            else:
                msg = "That was incorrect. The correct answer was {}.".format(corr_ans_math)
            
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
            
        # completed 1.0 repeats of 'math_trials_practice'
        
        
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
        
        # set up handler to look after randomisation of conditions etc
        math_trials = data.TrialHandler(nReps=10000.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('math_stim.csv'),
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
            num1 = randint(1,11)
            num2 = randint(1,11)
            
            if trial_sign == "addition":
                sign = "+"
                corr_ans_math = num1 + num2
            elif trial_sign == "subtraction":
                sign = "-"
                corr_ans_math = num1 - num2
            elif trial_sign == "division":
                sign = "/"
                corr_ans_math = num1 / num2
            else:
                sign = "x"
                corr_ans_math = num1 * num2
            math_kb = keyboard.Keyboard()
            response_rt = 0
            text.setText(num1)
            text_2.setText(num2)
            text_3.setText(sign)
            textbox.reset()
            # keep track of which components have finished
            math_trialComponents = [text, text_2, text_3, textbox]
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
                math_keys = math_kb.getKeys()
                valid_keys = ['1','2','3','4',
                '5','6','7','8','9','0','minus', 'return']
                for thisKey in math_keys:
                    if thisKey.name == 'escape':
                        core.quit()
                    if thisKey.name not in valid_keys:
                        textbox.text = ''
                    elif (textbox.text != '') and (thisKey.name == 'return'):
                        response_rt = thisKey.rt
                        continueRoutine = False
                        
                if timer.getTime() <= 0:
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
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                
                # *text_3* updates
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    text_3.setAutoDraw(True)
                
                # *textbox* updates
                if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox.frameNStart = frameN  # exact frame index
                    textbox.tStart = t  # local t and not account for scr refresh
                    textbox.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                    textbox.setAutoDraw(True)
                
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
            answer = float(textbox.text)
            
            if answer == corr_ans_math:
                math_correct = 1
            else:
                math_correct = 0
            
            thisExp.addData('corr_ans_math', corr_ans_math)
            thisExp.addData('math_correct', math_correct)
            thisExp.addData('response_rt', response_rt)
            
            math_trials.addData('textbox.text',textbox.text)
            # the Routine "math_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 10000.0 repeats of 'math_trials'
        
        thisExp.nextEntry()
        
    # completed sum([task_type=='math']) repeats of 'math'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


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
