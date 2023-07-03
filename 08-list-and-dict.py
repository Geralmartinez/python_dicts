students =[
    {
    "name": "sebastian",
    "lastname": "jimenez",
    "course": "viajes especiales",
    "grades": [90, 100, 85, 100],
    "active": False 
},
{ 
     
    "name" : "kylian",
    "lastname": "acevedo",
    "course": "viajes especiales",
    "grades":  [90, 100, 85,],
    "active":  True
}

   
]


for student in students:
    print("----------------------")
    print("estudiante:", student["name"], student["lastname"])
    print("curso:",  student["course"])

    sum = 0
    grades = student["grades"]
    for grade in grades:
        sum += grade

    print("promedio de notas:", sum/len(grades))

    if student["active"]:
     print("estado: activo")
    else:
        print("estado: inactivo")  