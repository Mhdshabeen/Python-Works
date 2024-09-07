

from json import load

f=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\FileOperations\\jsonWorks\\filims.json")

films=load(f)

for film in films:

    print(film.get("title"))