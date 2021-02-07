import json

data = json.load(open("data.json"))

def translate(user_word):  # here, the variable is at the local scope
    if user_word in data:
        return data[user_word] # ... because it has meaning inside the function
    elif user_word.islower() == False:
        lower_case = user_word.lower()
        if lower_case in data:
            return data[lower_case]
    else:
        return "I'm afraid there is no such word ..."

word = input("Enter word:  ") # global variable

print(translate(word)) # same global variable
