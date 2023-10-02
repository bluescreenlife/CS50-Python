# students = ["Hermione", "Harry", "Ron"] ##list of length 3

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])


## DICTIONARIES

# students = {
#     "Hermione": "Griffindor",
#     "Harry": "Griffindor",
#     "Ron": "Griffindor",
#     "Draco": "Slytherin"
# }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=", ")


## MORE DATA IN DICTIONARY

students = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], sep=", ")