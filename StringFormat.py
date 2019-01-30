# \'
# \"
# \\
# \n

course = "Python \"Programming"

print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

first = "Mosh"
last = "Hamedani"
# full = first + " " + last
full = f"{first} {last} len is {len(first) + len(last)}"
print(full)

text = " python Programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.rstrip())
print(text.find("Pro"))
print(text.replace("p", "j"))
print("Pro" in course)
print("swift" not in course)