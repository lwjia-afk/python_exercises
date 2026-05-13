
from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    sound: str

    def speak(self) -> str:
        return self.sound
        
    @property
    def description(self):
        return f"{self.name} says {self.speak()}"
        
    @classmethod
    def from_dict(cls, d:dict):
        animal = cls(d.get("name", ""), d.get("sound", ""))
        return animal

 
class Dog(Animal):
    def __init__(self, name:str, sound: str = "wof wof"):
        super().__init__(name, sound)
        
    def speak(self) -> str:
        return self.sound
    
        
class Cat(Animal):
    def __init__(self, name:str, sound: str = "miou miou"):
        super().__init__(name, sound)
    
    def speak(self) -> str:
        return self.sound

def make_noise(thing):
    return thing.speak()

if __name__ == "__main__":
    dog = Dog("tommy")
    cat = Cat("kitty")
    
    d1 = Dog.from_dict({ "name": "gougou", "sound": "wowo" })
    cat1 = Cat.from_dict({ "name": "mimi", "sound" : "miaomiao" })
    
    print(dog.description)
    print(cat.description)
    print(d1.description)
    print(cat1.description)

    print(make_noise(dog))
    print(make_noise(cat))