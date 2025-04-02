class new:
    a = 1

object = new()

print(object.a) #It fetches class attribute as no object/instance attribute is set
object.a = 0

print(new.a) #Assigning 0 to object attribute(object.a) does not change class attribute a
print(object.a) #Object/Instance attribute