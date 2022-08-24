# Stroop Task
### PsychoPy v2022.2.3


### Experimental Flow
1. Instructions
2. Practice Stroop trials with feedback
	- The minimum number of practice trials is the number of rows in the stimuli.csv file. To increase the number of trials, you can change the the value nReps in the trials_practice loop. For example, if there are 9 rows of stimuli and nReps = 1, there will be 9 trials. If you change nReps to 2, there will be 18 (9 * 2) trials.
3. Experimental Stroop trials
	- The minimum number of experimental trials is the number of rows in the stimuli.csv file. To increase the number of trials, you can change the the value nReps in the trialsloop. For example, if there are 9 rows of stimuli and nReps = 1, there will be 9 trials. If you change nReps to 2, there will be 18 (9 * 2) trials.
4. Experiment end

### Files needed
1. stroop.psyexp
2. stimuli.csv
	- This file can be edited to edit the stimuli presented. The "word" column changes the stimuli text and the "color" column changes the stimuli color.