def student_names(dictionary):
    name_list = []
    for names in dictionary:
        name_list.append(dictionary[names])
    name_list.sort()
    print(name_list)


a = {
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}
student_names(a)