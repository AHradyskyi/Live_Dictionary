import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
         yon = input("Are U sure? I think it should be \"%s\". Enter Y if yes or N if not: " %get_close_matches(w,data.keys())[0])
         if yon == "Y":
             return data[get_close_matches(w,data.keys())[0]]
         elif yon == "N":
             return "The word does not exists. Try again later."
         else:
             return "I am sorry, what was that?"

    else:
        return "The word does not exists. Try again later."


word = input("Enter a word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print('*',item)
else:
    print(output)