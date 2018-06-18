#    Matthew Shaw
#    Sunday, 1 November 2015 at 15:43:18
#    r2l.py


def r2l(string):
    """
    Prints a string downwardly diagonal from right to left
    """
    
    width = len(string)                         
    for i in string:                        # For the length of the string
        print(' '*(width-1), i)             # Ensure there will be enough spaces
        width = width - 1                   # Make indentation diagonal

        
r2l("slantwise")

