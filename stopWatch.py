#!
#stopwatch.py - A simple stopwatch program.

import time

#Display the program's instructions.
print('press enter to begin. Afterwards, press enter to "click" the stop watch')
print('press Ctrl-C to quit.')

input() #press Enter to begin
print('Started.')

startTime = time.time() # get the first lap's start time
lastTime = startTime

lapNum = 1

#TODO: Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' %(lapNum, totalTime, lapTime), end='')
        #end='' avoids a \n being added automatically
        lapNum += 1
        lastTime = time.time() #reset the last lap time


except KeyboardInterrupt:
    #handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')


    print('hey')
