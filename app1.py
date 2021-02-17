import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(user_word):  # here, the variable is at the local scope
    user_word = user_word.lower() # just update user_word before the if statement
    if user_word in data:
        return data[user_word] # ... because it has meaning inside the function
    # Ardit's answer to how to check for capitalization:
    #elif user_word.title() in data:  # if user entered "texas" this will check for "Texas" as well.
    #    return data[user_word.title()]
    
    # my attempt: it actually works, but for some reason you can's use elif here
    user_word = user_word.capitalize()
    if user_word in data:
        return data[user_word]
    # mine again; also works#
    # user_word = user_word.upper()
    # if user_word in data:
        return data[user_word]
    # let's try Ardit's way:
    elif user_word.upper() in data:
        return data[user_word.upper()]

    elif len(get_close_matches(user_word,data.keys())) > 0: # put data.keys again get_close to find that nearest match, which will produce a list.
        print("Did you mean '%s' instead?" % get_close_matches(user_word, data.keys())[0])
        refined_answer = input("If so, just type 'Y' (no quotes needed); if not, then type 'N': ")
        print(refined_answer)
        if refined_answer.upper() == 'Y':
            return(data[get_close_matches(user_word, data.keys())[0]])
        elif refined_answer.upper() == 'N':
            user_word = input("No worries; let's restart. Enter a word: ")
            user_word = user_word.lower()  # just update user_word before the if statement
            if user_word in data:
                return data[user_word]
        else:
            print("Uhhh ... I can only use 'Y' or 'N' here.")
            user_word = input("Anyway ... so, why don't we try again? Enter a word: ")
            if user_word in data:
                return data[user_word]

    # my bloated, kludge solution:
    # elif user_word.islower() == False:
    #     lower_case = user_word.lower()
    #     if lower_case in data:
    #         return data[lower_case]
    
    else:
        return "I'm afraid there is no such word ..."

word = input("Enter word:  ") # global variable

output = translate(word)

# let's make it more user friendly
# to make sure it's from the list and not one of the string responses
if type(output) == list:

# iterate through the list, to make it more readable.
    for item in output:
        print(item)
else:
    print(item)
# print(translate(word)) # same global variable
