def main():
    student = Student.get()
    print(student)

class Student:
    def __init__(self, name, house): # initialize object from class
        self.name = name
        self.house = house
        # self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing name")
    #     self._name = name

    # @property # Getter
    # def house(self):
    #     return self._house

    # @house.setter # Setter
    # def house(self, house):
    #     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #         raise ValueError("Invalid house")
    #     self._house = house

    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🐴"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russel terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"

if __name__ == "__main__":
    main()



