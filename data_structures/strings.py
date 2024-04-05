def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    
    reversed_str = ""
    
    for i in range(len(our_string)-1, -1, -1):
        reversed_str += our_string[i]
    
    return reversed_str