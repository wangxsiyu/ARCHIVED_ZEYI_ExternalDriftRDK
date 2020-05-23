#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Sat Apr 18 20:45:01 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='/Volumes/WANG/Lab_Wilson/Projects/Projects_Pilot/DDM_ExternalDrift_Zeyi/test_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
bL = visual.Rect(
    win=win, name='bL',
    width=(0.1, 0.5)[0], height=(0.1, 0.5)[1],
    ori=0, pos=(-0.8,0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
bR = visual.Rect(
    win=win, name='bR',
    width=(0.1, 0.5)[0], height=(0.1, 0.5)[1],
    ori=0, pos=(0.8, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
dot = visual.Rect(
    win=win, name='dot',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
mykey = keyboard.Keyboard()

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
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    bL.setFillColor([1,1,1])
    bR.setFillColor([1,1,1])
    dot.setPos((0, 0))
    mykey.keys = []
    mykey.rt = []
    _mykey_allKeys = []
    speed0 = 0.0001
    speedn = 32
    currentkey = 0
    previouskey = 1
    nkey = 0
    currentx = 0
    lastkeys = []
    xright = 0.7
    xleft = -0.7
    bL.setFillColor([0,1,1], log=None)
    bR.setFillColor([0,1,1], log=None)
    
    # keep track of which components have finished
    trialComponents = [bL, bR, dot, mykey]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *bL* updates
        if bL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bL.frameNStart = frameN  # exact frame index
            bL.tStart = t  # local t and not account for scr refresh
            bL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bL, 'tStartRefresh')  # time at next scr refresh
            bL.setAutoDraw(True)
        
        # *bR* updates
        if bR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bR.frameNStart = frameN  # exact frame index
            bR.tStart = t  # local t and not account for scr refresh
            bR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bR, 'tStartRefresh')  # time at next scr refresh
            bR.setAutoDraw(True)
        
        # *dot* updates
        if dot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dot.frameNStart = frameN  # exact frame index
            dot.tStart = t  # local t and not account for scr refresh
            dot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dot, 'tStartRefresh')  # time at next scr refresh
            dot.setAutoDraw(True)
        
        # *mykey* updates
        waitOnFlip = False
        if mykey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mykey.frameNStart = frameN  # exact frame index
            mykey.tStart = t  # local t and not account for scr refresh
            mykey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mykey, 'tStartRefresh')  # time at next scr refresh
            mykey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(mykey.clock.reset)  # t=0 on next screen flip
        if mykey.status == STARTED and not waitOnFlip:
            theseKeys = mykey.getKeys(keyList=None, waitRelease=False)
            _mykey_allKeys.extend(theseKeys)
            if len(_mykey_allKeys):
                mykey.keys = [key.name for key in _mykey_allKeys]  # storing all keys
                mykey.rt = [key.rt for key in _mykey_allKeys]
        if mykey.keys != lastkeys:
           lastkeys = mykey.keys
           nkey = nkey + 1
           if lastkeys[nkey-1] == 'left':
               currentkey = -1
           if lastkeys[nkey-1] == 'right':
               currentkey = 1
           if currentkey != previouskey:
               speedn = currentkey
           if currentkey == previouskey:
               speedn = speedn * 2
           previouskey = currentkey
        currentx = currentx + speedn*speed0;
        dot.setPos((currentx, 0), log=False)
        if ((currentx > xright)):
            continueRoutine = False
            bR.setFillColor([1,0,0], log=None)
        if ((currentx < xleft)):
            continueRoutine = False
            bL.setFillColor([1,0,0], log=None)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('bL.started', bL.tStartRefresh)
    trials.addData('bL.stopped', bL.tStopRefresh)
    trials.addData('bR.started', bR.tStartRefresh)
    trials.addData('bR.stopped', bR.tStopRefresh)
    trials.addData('dot.started', dot.tStartRefresh)
    trials.addData('dot.stopped', dot.tStopRefresh)
    # check responses
    if mykey.keys in ['', [], None]:  # No response was made
        mykey.keys = None
    trials.addData('mykey.keys',mykey.keys)
    if mykey.keys != None:  # we had a response
        trials.addData('mykey.rt', mykey.rt)
    trials.addData('mykey.started', mykey.tStartRefresh)
    trials.addData('mykey.stopped', mykey.tStopRefresh)
    dot.draw()
    bL.draw()
    bR.draw()
    win.flip()
    core.wait(1.0);
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
