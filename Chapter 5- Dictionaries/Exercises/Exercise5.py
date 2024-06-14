pets = []

pet = {
    'animal type': 'dog',
    'name': 'sheezuu',
    'owner': 'jahfar',
}
pets.append(pet)

pet = {
    'animal type': 'Cat',
    'name': 'andrew',
    'owner': 'jahafar',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'tommy',
    'owner': 'jahfar',
}
pets.append(pet)

for pet in pets:
    print(f"\nWhat I know about {pet['name']}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
