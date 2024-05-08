"""
> Title: Countdown Timer.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

import sys, time
import sevseg

secondsLeft = 5

try:
    while True:
        # Clear the screen by printing several newlines
        print('\n'*60)
        
        # Get the hours/minutes/seconds from secondsLeft:
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)
        
        # Get the digit strings from the sevseg module
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        
        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        
        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()
        
        # Display Countdown
        print(hTopRow + '   ' + mTopRow + '   ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)
        
        if secondsLeft == 0:
            print()
            print('\n     * * * * BOOM * * * *\n')
            break
        
        print()
        print('     Press Ctrl+C to quit.')
        
        time.sleep(1)
        secondsLeft -= 1

except KeyboardInterrupt:
    print('\nThank You!\n')
    sys.exit()
