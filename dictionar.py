import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        return "Are U sure? I think it should be \"%s\".    " %get_close_matches(w,data.keys())[0]
    else:
        return "The word does not exists. Try again later."


word = input("Enter a word: ")
print(translate(word))
