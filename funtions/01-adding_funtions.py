verses = ["mano hacia el frente","puño cerrado","dedo hacia arriba","lengua afuera"]

def intro():
    print("atencion, compañia")

def chorus():
    print("chuchuwa, chuchuwa, chuchuwa wa wa")
    print("chuchuwa, chuchuwa, chuchuwa wa wa")

def outro():
    print("lalala lalala lalala la la")
    print("lalala lalala lalala la la")

for verse in verses:
    intro()
    print(verse)
    chorus()
    print("-----------")