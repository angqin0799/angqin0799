
# ##### list #####
# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)

# ##### len #####
# ##### indexing #####
# # for i in range(len(students)):
# #     print(students[i])

# for i in range(len(students)):
#      print(i + 1, students[i])

# ##### dictionaries #####
#      # keys : values
# studs = {
#      "Hermione" : "Gryffindor",
#      "Harry" : "Gryffindor",
#      "Ron" : "Gryffindor",
#      "Draco" : "Slytherin",
# }

# for stud in studs:
#      print(stud, studs[stud], sep = ", ")       # using for-loop in dictionary will interate through the keys

# list of dictionaries
    # four dictionaries; three keys each, three values each
students = [
     {"name" : "Hermione",  "house" : "Gryffindor",     "patronus" : "Otter"},
     {"name" : "Harry",     "house" : "Gryffindor",     "patronus" : "Stag"},
     {"name" : "Ron",       "house" : "Gryffindor",     "patronus" : "Jack Russell terrier"},
     {"name" : "Draco",     "house" : "Slytherin",      "patronus" : None},
]

for student in students:
     print(student["name"], student["house"], student["patronus"], sep = ", ")
