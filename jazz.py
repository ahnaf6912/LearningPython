def jazz(notes):
    for note in notes:
        if note[len(note) - 1] != "7":
            note = note + "7"
        print(note)

a = input("input some notes seperared by comma ")
b = a.split(",")
jazz(b)
        