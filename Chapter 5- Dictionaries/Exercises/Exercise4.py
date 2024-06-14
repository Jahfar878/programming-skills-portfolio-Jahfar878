rivers = {
    'Nile': 'Egypt',
    'Yangtze River': 'China',
    'Mississippi River': 'United States',
    }

for river, country in rivers.items():
    print(f"The {river} flows through {country}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
<<<<<<< HEAD
    print(f"- {country}")
=======
    print(f"- {country}")
>>>>>>> 8ad3fc8c8d7add1cf082fac4a0a6c13385a0ffdf
