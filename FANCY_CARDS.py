#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on Thu Jan  3 13:49:10 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'FANCY_CARDS'  # from the Builder filename that created this script
expInfo = {u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-0.5,-0.5,-0.5], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "selection"
selectionClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
# Sitmuli downloaded from:
# https://www.1001freedownloads.com/free-clipart/guyenne-classic-card-deck

# A variable to choose whether to use eye tracking or not.
# If it is left to False, mouse position will be used instead.
expInfo["Eye Tracker"] = False

# Defining the variable that will be used when controlling for gaze or mouse position.
# Here we give it an initial value from mouse position
dotPosition=mouse.getPos()

# Here we define a function to convert Tobii's normalized coordinates to pixels
# and change origin to center of screen, like PsychoPy does
def norm2pix(point, win):
    if not np.isnan(point[0]):
        x = point[0] * win.size[0]
        y = point[1] * win.size[1]
        xAdj = x - (win.size[0] / 2)
        yAdj = (y * -1) + (win.size[1] / 2)
        return (xAdj, yAdj)
    else:
        return (np.nan, np.nan)

# If eye tracker is to be used, we need to prepare a few things
if expInfo['Eye Tracker']:
    # import tobii pro module
    import tobii_research as tr
    # turn off mouse visibility
    mouse.setVisible(0)
    # find eye trackers
    found_eyetrackers = []
    while len(found_eyetrackers) == 0:
        found_eyetrackers = tr.find_all_eyetrackers()
    # select first eye tracker
    my_eyetracker = found_eyetrackers[0]
    # create list in which we append gaze data
    gaze_list = []
    # create callback to get gaze data
    def gaze_data_callback(gaze_data):
        # append timestamp and gazePointLeft at callback
        gaze_list.append([gaze_data['system_time_stamp'],gaze_data['left_gaze_point_on_display_area']]) # left eye only
CARD1 = visual.ImageStim(
    win=win, name='CARD1',
    image='media/image1.png', mask=None,
    ori=0, pos=(-400, 0), size=(186, 289),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
CARD2 = visual.ImageStim(
    win=win, name='CARD2',
    image='media/image2.png', mask=None,
    ori=0, pos=(0, 0), size=(186, 289),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
CARD3 = visual.ImageStim(
    win=win, name='CARD3',
    image='media/image3.png', mask=None,
    ori=0, pos=(400, 0), size=(186, 289),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
polygon = visual.Rect(
    win=win, name='polygon',
    width=(5, 5)[0], height=(5, 5)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "result"
resultClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Your selection:',
    font='Arial',
    pos=(0, 300), height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(186, 289),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "selection"-------
    t = 0
    selectionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    # If we are using eye tracking
    if expInfo['Eye Tracker']:
        # start getting live data from the eye tracker
        my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    # create a list to collect position data when it is within one of the stimuli.
    # this will be reset everytime we look outside a stimulus
    gazeCount=[]
    # keep track of which components have finished
    selectionComponents = [mouse, CARD1, CARD2, CARD3, polygon]
    for thisComponent in selectionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "selection"-------
    while continueRoutine:
        # get current time
        t = selectionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # If we are using eye tracking
        if expInfo['Eye Tracker']:
            # if we have some gaze returned from the eye tracker
            if len(gaze_list) > 0:
                # get the last sample sent from eye tracker
                gpos = gaze_list[-1]
                # use our custom function to convert gaze coordinates to pixels and reset origin to center.
                dotPosition=norm2pix(gpos[1], win)
            # if we don't have gaze data
            else:
                # set position to na
                dotPosition = (np.nan, np.nan)
        # if we are not using eye tracking
        else:
            # get mouse position
            dotPosition = mouse.getPos()
        
        # if our position variable is not na
        if not np.isnan(dotPosition[0]):
            # check if it is within one of the images
            if CARD1.contains(dotPosition):
                gazeCount.append(dotPosition)
                imageName="image1"
            elif CARD2.contains(dotPosition):
                gazeCount.append(dotPosition)
                imageName="image2"
            elif CARD3.contains(dotPosition):
                gazeCount.append(dotPosition)
                imageName="image3"
            # if gaze is out of stimuli, reset collection list
            else:
                gazeCount=[]
        else:
            gazeCount=[]
        
        # if we collect 60 sample or more in the same stimuli
        if len(gazeCount)>=60:
            # set result image file name to the selected image
            selectedImage = "media" + os.sep + imageName+'.png'
            # stop selection routine and show result
            continueRoutine=False
        
        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            # if using eye tracking
            if expInfo['Eye Tracker']:
                # stop getting data from eye tracker
                my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
            win.close()
            core.quit()
        
        # *CARD1* updates
        if t >= 0.0 and CARD1.status == NOT_STARTED:
            # keep track of start time/frame for later
            CARD1.tStart = t
            CARD1.frameNStart = frameN  # exact frame index
            CARD1.setAutoDraw(True)
        
        # *CARD2* updates
        if t >= 0.0 and CARD2.status == NOT_STARTED:
            # keep track of start time/frame for later
            CARD2.tStart = t
            CARD2.frameNStart = frameN  # exact frame index
            CARD2.setAutoDraw(True)
        
        # *CARD3* updates
        if t >= 0.0 and CARD3.status == NOT_STARTED:
            # keep track of start time/frame for later
            CARD3.tStart = t
            CARD3.frameNStart = frameN  # exact frame index
            CARD3.setAutoDraw(True)
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:  # only update if drawing
            polygon.setPos(dotPosition, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "selection"-------
    for thisComponent in selectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    # add the selected image to exported data
    trials.addData("Selected Image", selectedImage)
    # stop collecting data from eye tracker
    if expInfo['Eye Tracker']:
        my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
    # the Routine "selection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "result"-------
    t = 0
    resultClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image.setImage(selectedImage)
    # keep track of which components have finished
    resultComponents = [text, image]
    for thisComponent in resultComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "result"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = resultClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resultComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "result"-------
    for thisComponent in resultComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
