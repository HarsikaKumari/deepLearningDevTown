dog_age = 7

def age():
  human_age = dog_age * 7
  print (human_age)

age()

# dp:- while defining we give parameters, ca:- while calling we give argument

def age(dog_age):
  human_age = dog_age * 7
  return human_age


a = age(4)
print(a)