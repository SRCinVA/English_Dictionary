import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(user_word):  # here, the variable is at the local scope
    user_word = user_word.lower() # just update user_word before the if statement
    if user_word in data:
        return data[user_word] # ... because it has meaning inside the function
    
    elif len(get_close_matches(user_word,data.keys())) > 0: # put data.keys again get_close to find that nearest match, which will produce a list.
        return "Did you mean '%s' instead?" % get_close_matches(user_word, data.keys())[0]
    
    # my bloated, kludge solution:
    # elif user_word.islower() == False:
    #     lower_case = user_word.lower()
    #     if lower_case in data:
    #         return data[lower_case]
    else:
        return "I'm afraid there is no such word ..."

word = input("Enter word:  ") # global variable

print(translate(word)) # same global variable
