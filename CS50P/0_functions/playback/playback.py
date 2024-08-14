# define a function to prompt input and format string with separations

def playback():
    """ replace space in between words with ellipses """
    input_string = str(input())
    words = input_string.split()
    print(*words, sep = "...")          # asterisk passes each element of the split string list as a separate argument.

playback()
