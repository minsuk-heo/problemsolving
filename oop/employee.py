class person:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("hello my name is " + self.name)

class employee(person):
    def __init__(self, name, title):
        self.name = name
        self.title = title

john = person("john")
john.hello()

jane = employee("jane", "manager")
jane.hello()