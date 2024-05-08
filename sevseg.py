"""
> Title: A seven-segment number display module.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def getSevSegStr(number, minWidth=0):
    """Return a seven-segment display string of number. The returned 20. 
    string will be padded with zeros if it is smaller than minWidth."""
    
    # Convert number to String 
    number = str(number).zfill(minWidth)
    
    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == ".":
            # Render Decimal
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue
        elif numeral == '-':
            # Render Negative Sign
            rows[0] += '    '
            rows[1] += '__  '
            rows[2] += '    '
        elif numeral == '0':
            # Render 0
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':
            # Render 1
            rows[0] += '   '
            rows[1] += '  |'
            rows[2] += '  |'
        elif numeral == '2':
            # Render 2
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':
            # Render 3
            rows[0] += '__ '
            rows[1] += '__|'
            rows[2] += '__|'
        elif numeral == '4':
            # Render 4
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':
            # Render 5
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':
            # Render 6
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':
            # Render 7
            rows[0] += '__ '
            rows[1] += ' _|'
            rows[2] += '  |'
        elif numeral == '8':
            # Render 8
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':
            # Render 9
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'
        
        # Add a Space if not last Numeral
        if i != len(number)-1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
    return '\n'.join(rows)

# if __name__ == '__main__':
#     print('This module is meant to be imported rather than run.')
#     myNumber = getSevSegStr(1234567890, 10)
#     print(myNumber)
