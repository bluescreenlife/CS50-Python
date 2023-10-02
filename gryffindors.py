# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"}
# ]

# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gryffindor in gryffindors:
#     print(gryffindor["name"])

# ------------------------------------------------------------

# students = ["Hermione", "Harry", "Ron"]

# gryffindors = {student: "Gryffindor" for student in students}

# # replaced by dict comprehension above
# # for student in students:
# #     gryffindors.append({"name": student, "house": "Gryffindor"})

# print(gryffindors)

# ------------------------------------------------------------

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students): #replaces range, len
    print(i + 1, student)