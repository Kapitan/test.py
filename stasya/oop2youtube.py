class Person:
    name = "Ivan"
    age = 30


i = Person()

print(i.age)
print(Person.__dict__)
print(getattr(i, "x", "нет аутрибута"))
Person.x = 200
setattr(Person, "qqq", 400)
print(Person.__dict__)
del Person.qqq
print(Person.__dict__)
delattr(Person, "x")
print(Person.__dict__)
