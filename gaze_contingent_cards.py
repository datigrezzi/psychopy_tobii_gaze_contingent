#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), settembre 21, 2016, at 15:53
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008

Sitmuli downloaded from:
https://www.1001freedownloads.com/free-clipart/guyenne-classic-card-deck
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Fancy Cards'  # from the Builder filename that created this script
expInfo = {u'Eye Tracker': False, u'showAoi': True, u'Participant': u'XX'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['Participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
mouse = event.Mouse(win=win)

dotPosition=mouse.getPos()

def norm2pix(point, win):
    if not np.isnan(point[0]):
        x = point[0] * win.size[0]
        y = point[1] * win.size[1]
        xAdj = x - (win.size[0] / 2)
        yAdj = y - (win.size[1] / 2) * -1
        return (xAdj, yAdj)
    else:
        return (np.nan, np.nan)

if expInfo['Eye Tracker']:
    mouse.setVisible(0)
    import tobii_research as tr
    import time
    import csv
    # find eye trackers
    found_eyetrackers = tr.find_all_eyetrackers()
    # select first eye tracker
    my_eyetracker = found_eyetrackers[0]
    # create list in which we append gaze data
    gaze_list = []
    # create call back to get gaze data
    def gaze_data_callback(gaze_data):
        # append ts, gpl and gpr
        gaze_list.append([gaze_data['system_time_stamp'],gaze_data['device_time_stamp']
    ,gaze_data['left_gaze_point_on_display_area'],gaze_data['right_gaze_point_on_display_area']])

ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
image1 = visual.ImageStim(win=win, name='image1',
    image='media/image1.png', mask=None,
    ori=0, pos=[-400, 0], size=[185, 288],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image2 = visual.ImageStim(win=win, name='image2',
    image='media/image2.png', mask=None,
    ori=0, pos=[0, 0], size=[185, 288],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image3 = visual.ImageStim(win=win, name='image3',
    image='media/image3.png', mask=None,
    ori=0, pos=[400, 0], size=[185, 288],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

text = visual.TextStim(win=win, ori=0, name='text',
    text='Choose a card!',    font='Arial',
    pos=[0, -450], height=40, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0)
aoi1 = visual.Rect(win=win, name='aoi1',
    width=[350, 400][0], height=[350, 400][1],
    ori=0, pos=[-400, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0.5,depth=-9.0, 
interpolate=True)
aoi2 = visual.Rect(win=win, name='aoi2',
    width=[350, 400][0], height=[350, 400][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0.5,depth=-10.0, 
interpolate=True)
aoi3 = visual.Rect(win=win, name='aoi3',
    width=[350, 400][0], height=[350, 400][1],
    ori=0, pos=[400, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0.5,depth=-11.0, 
interpolate=True)

# Initialize components for Routine "selectionView"
selectionViewClock = core.Clock()
imageSelected = visual.ImageStim(win=win, name='imageSelected',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[185, 288],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Is this your card?',    font='Arial',
    pos=[0, -450], height=40, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='Thank you for playing!',    font='Arial',
    pos=[0, 0], height=40, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if expInfo['Eye Tracker']:
        my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
        gpos = gaze_list # left eye only
    gazeCount=[]
    
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(image1)
    trialComponents.append(image2)
    trialComponents.append(image3)

    trialComponents.append(text)
    trialComponents.append(aoi1)
    trialComponents.append(aoi2)
    trialComponents.append(aoi3)

    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if expInfo['Eye Tracker']:
            if len(gaze_list) > 0:
                gpos = gaze_list[-1] # last sample    
                dotPosition=gpos[2] # left eye only
            else:
                dotPosition = (np.nan, np.nan)
        else:
            dotPosition = mouse.getPos()
        print dotPosition
        if not np.isnan(dotPosition[0]):
            if aoi1.contains(dotPosition): #add ifs for all images
                gazeCount.append(dotPosition)
                imageName="image1"
            elif aoi2.contains(dotPosition): #add ifs for all images
                gazeCount.append(dotPosition)
                imageName="image2"
            elif aoi3.contains(dotPosition): #add ifs for all images
                gazeCount.append(dotPosition)
                imageName="image3"
            else:
                gazeCount=[]
        else:
            gazeCount=[]
        
        # if we collect 60 sample or more in the same AOI
        if len(gazeCount)>=60:
            selectedImage = "media" + os.sep + imageName+'.png'
            continueRoutine=False
        
        # *image1* updates
        if t >= 0.0 and image1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image1.tStart = t  # underestimates by a little under one frame
            image1.frameNStart = frameN  # exact frame index
            image1.setAutoDraw(True)
        
        # *image2* updates
        if t >= 0.0 and image2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image2.tStart = t  # underestimates by a little under one frame
            image2.frameNStart = frameN  # exact frame index
            image2.setAutoDraw(True)
        
        # *image3* updates
        if t >= 0.0 and image3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image3.tStart = t  # underestimates by a little under one frame
            image3.frameNStart = frameN  # exact frame index
            image3.setAutoDraw(True)
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        if expInfo["showAoi"]:
            # *aoi1* updates
            if t >= 0.0 and aoi1.status == NOT_STARTED:
                # keep track of start time/frame for later
                aoi1.tStart = t  # underestimates by a little under one frame
                aoi1.frameNStart = frameN  # exact frame index
                aoi1.setAutoDraw(True)
            
            # *aoi2* updates
            if t >= 0.0 and aoi2.status == NOT_STARTED:
                # keep track of start time/frame for later
                aoi2.tStart = t  # underestimates by a little under one frame
                aoi2.frameNStart = frameN  # exact frame index
                aoi2.setAutoDraw(True)
            
            # *aoi3* updates
            if t >= 0.0 and aoi3.status == NOT_STARTED:
                # keep track of start time/frame for later
                aoi3.tStart = t  # underestimates by a little under one frame
                aoi3.frameNStart = frameN  # exact frame index
                aoi3.setAutoDraw(True)
 
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            if expInfo['Eye Tracker']:
                my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
            win.close()
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    win.flip()
    
    if expInfo['Eye Tracker']:
        my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "selectionView"-------
    t = 0
    selectionViewClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    imageSelected.setImage(selectedImage)
    # keep track of which components have finished
    selectionViewComponents = []
    selectionViewComponents.append(imageSelected)
    selectionViewComponents.append(text_2)
    for thisComponent in selectionViewComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "selectionView"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = selectionViewClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageSelected* updates
        if t >= 0.0 and imageSelected.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageSelected.tStart = t  # underestimates by a little under one frame
            imageSelected.frameNStart = frameN  # exact frame index
            imageSelected.setAutoDraw(True)
        if imageSelected.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            imageSelected.setAutoDraw(False)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        if text_2.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectionViewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "selectionView"-------
    for thisComponent in selectionViewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(text_3)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    if text_3.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
