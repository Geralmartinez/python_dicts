verses = ["mano hacia el frente", "puño cerrado", "dedo hacia arriva","lengua afuera"]
print(verses[-1])

for verse in verses:
    if verse != verses[1]:
        print("todavia no llegamos")
    else:
        print("llegamos al final")