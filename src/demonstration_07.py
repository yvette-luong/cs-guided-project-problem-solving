"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"

Questions: 
    + What id there are non-alphabetic characters in the string? Including space?
        + We don't need to worry about this
    + What if we get an empty string? 
        + Return an empty string 
"""
def repeat_it(input_str):
    #  Check for empty string
    if input_str == "":
        return ""
    # Convert the input string to a list 
    input_list = list(input_str)
    result_list = []
    # Loop through the list 
    for reps, char in enumerate(input_list):
        repeated_char = ""    

        #  Repeat the character
        for _ in range(reps):
            repeated_char +=char

        #  Capitalize the new strings
        repeated_char = repeated_char.capitalize()
        print(repeated_char)
        #  Add items to result list
        result_list.append(repeated_char)
    print(result_list)
    # Join result list with - 
    result_str = "-".join(result_list)
    # Return the string  
    return result_str
print(repeat_it("abcd"))
print("-- First demo --")
print(repeat_it("RqaEzty"))
print("-- Second demo --")
print(repeat_it("cwAt"))
print("-- Third demo --")
