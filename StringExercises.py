"""
Convert even-indexed characters to uppercase in a string:

before: "hi my name is john and i am learning python"
after: "Hi mY NaMe iS JoHn i aM LeArNiNg pYtHoN"

"""

def alternating(string):
    new_string= ""
    for string_index in range(len(string)):
        if string_index %2==0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("hi my name is john and i am learning python")