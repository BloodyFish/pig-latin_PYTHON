vowelList = "aeiou"
wordEndList = ".!?:;,"

myInput = input("Say something: ")
words = myInput.split(" ")
for word in words:
    wordEnd = ""
    if word[len(word) - 1] in wordEndList:
        wordEnd = word[len(word) - 1]
        word = word[:len(word) - 1]

    if word[0].lower() in vowelList:
        print(word.lower() + "hay" + wordEnd, end=" ")
    else:
        print(word[1:].lower() + word[0].lower() + "ay" + wordEnd, end=" ")