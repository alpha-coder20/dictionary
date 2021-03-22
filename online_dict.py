import json
import difflib
import time
from difflib import get_close_matches as gcm

data = json.load(open("data.json"))
print("Welcome to Online Dictionary! ")
def translate(w):
    if w in data:
        return data[w]
    elif len(gcm(w, data.keys())):
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %gcm(w, data.keys())[0])
        if yn.lower() == 'y':
            return data[gcm(w, data.keys())[0]]
        elif yn.lower() == 'n':
            return "The word does not exist. Please double check it."
        else:
            return "We did not understand your entry."
    else:
        return "The word does not exist. Please double check it."


word = input("Enter word you want to know meaning of: ").lower()

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

time.sleep(5)