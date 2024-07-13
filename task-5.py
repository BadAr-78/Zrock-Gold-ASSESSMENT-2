# Write a Python class with a method that prints a message.

class Element:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)
    

elme = Element("Hellow Zrock")
print(elme)
