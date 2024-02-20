import gc

class Dog:
  instances = []
  def __init__(self, name, age, size, fed = False):
    self.__class__.instances.append(self)
    # Enforcing the type of the input parameters
    if not isinstance(name, str):
      raise TypeError("Name must be a string")
    if not isinstance(age, int):
      raise TypeError("Age must be an integer")
    if not (isinstance(size, str) or isinstance(size, int)):
      raise TypeError("Size must be a string or an integer")
    if not isinstance(fed, bool):
      raise TypeError("Fed must be a boolean")
    self.name = name
    self.age = age
    self.size = size
    self.fed = fed

  def bark(self):
    print(f"Woof! I am {self.name}.")

  def feed(self):
      self.fed = True
      print("Woof! I am fed.")

  def get_all_friends(self):
    for dog in Dog.instances:
      if dog != self:
        print(dog.name)


def get_all_dogs():
  for obj in gc.get_objects():
      if isinstance(obj, Dog):
          print(obj.name)

def get_hungry_dogs():
  for obj in gc.get_objects():
      if isinstance(obj, Dog):
          if not obj.fed:
            print(f"{obj.name} is still hungry.")