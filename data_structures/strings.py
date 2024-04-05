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


def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other
    An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).
    For example:
        "rat" is an anagram of "art"
        "alert" is an anagram of "alter"
        "Slot machines" is an anagram of "Cash lost in me"

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    
    str1 = sorted(str1.lower().replace(" ", ""))
    str2 = sorted(str2.lower().replace(" ", ""))
    
    if str1 == str2:
        return(True)
    else:
        return(False)