pets = []

pet = {
<<<<<<< HEAD
    'animal type': 'cat',
    'name': 'tom',
    'owner': 'shahul',
=======
    'animal type': 'dog',
    'name': 'sheezuu',
    'owner': 'jahfar',
>>>>>>> 8ad3fc8c8d7add1cf082fac4a0a6c13385a0ffdf
}
pets.append(pet)

pet = {
    'animal type': 'Cat',
    'name': 'andrew',
<<<<<<< HEAD
    'owner': 'abdu',
=======
    'owner': 'jahafar',
>>>>>>> 8ad3fc8c8d7add1cf082fac4a0a6c13385a0ffdf
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'tommy',
    'owner': 'jahfar',
}
pets.append(pet)

for pet in pets:
    print(f"\n what I know about {pet['name']}:")
    for key, value in pet.items():
<<<<<<< HEAD
        print(f"\t{key}: {value}")
=======
        print(f"\t{key}: {value}")
>>>>>>> 8ad3fc8c8d7add1cf082fac4a0a6c13385a0ffdf
