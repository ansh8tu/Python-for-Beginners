student = {
    "Name" : "Ari Leff",
    "Profession" : "Singer/Songwriter",
    "Contact" : 1235
}

print(student["Name"])
print(student.get("Profession"))
print(student.get('Birthdate', 'Jan 21'))