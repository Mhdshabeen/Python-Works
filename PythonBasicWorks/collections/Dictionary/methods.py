# Methods used in dictionary


student={"name":"shabeen","place":"kottappuram","course":"fullstack","duriation":"six months"}

student["name"]="ahamed" # used to update the value of a key by calling the key name

student["place"]="palakkad" 

student["father"]="Ibrahim" # add as a new key:value pair as it not present in dict

#print(student)

# =>    def key() returns the keys in a dictionary as a list

#print(student.keys())

# =>    def item() return all the key:value pairs in dict as a tuple element arranged in a list 

#new=student.items() # ([('name', 'ahamed'), ('place', 'palakkad'), ('course', 'fullstack'), ('duriation', 'six months'), ('father', 'Ibrahim')])

#print(new)

# Iterate


# for i in student:

#     print(f"{i}={student[i]}")

# =>    def pop("key name") used to remove the key:vlue pair from a dict

# student.pop("place")

# print(student) #{'name': 'ahamed', 'course': 'fullstack', 'duriation': 'six months', 'father': 'Ibrahim'}






