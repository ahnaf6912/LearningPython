def vowel(sentence):
    v = {}
    for letter in sentence:
        if letter == 'a' or  letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
          if v.get(letter) == None:
             v[letter] = 0
          v[letter] = v[letter] + 1
          
    print(v)
        

a = input("What is your sentence? ")
vowel(a)