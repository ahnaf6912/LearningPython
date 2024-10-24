def isonogram(word):
    for letters in word:
      if word.count(letters) > 1:
            print(False)
            break
    else:
            print(True)

a = input("what is your word ")
isonogram(a)