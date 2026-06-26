class Plant:
    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, {self.show_calls} show")


    def __init__(self, name: str, height: float, current_age: int) -> None:
        self.name = name 
        if height < 0:
            self._height = 0.0
        else:
            self._height = height
        if current_age < 0:
            self._current_age = 0
        else:
            self._current_age = current_age
       self. _stats = Plant.Stats()

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._current_age} days old")

    def grow(self) -> None:
        self._stats.grow_calls += 1
        self._height = round(self._height + (0.03 * self._height), 1)

    def age(self) -> None:
        self._stats.age_calls += 1
        self._current_age = self._current_age + 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._current_age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._current_age

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(plant):
        return plant("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, current_age: int,
                 color: str) -> None:
        super().__init__(name, height, current_age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

class Tree(Plant):
    def __init__(self, name: str, height: float, current_age: int,
                 trunk_diameter: float):
        super().__init__(name, height, current_age)
        self.trunk_diameter = trunk_diameter
        self._stats.produce_shade_calls = 0
        
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats.produce_shade_calls += 1
        print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")

    def display(self):
        super()._stats.display()
        print(f"{self._stats.produce_shade_calls} shade")


class   Seed(Flower):
    def __init__(self, name: str, height: float, current_age: int,
                 color: str):
        super().__init__(name, height, current_age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")

def Global_Stats(plant: Plant) -> None:
    plant._stats.display()


if  __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    tmp = Plant.is_older_than_year(30)
    print(f"Is 30 days more than a year? -> {tmp}")
    tmp = Plant.is_older_than_year(400)
    print(f"Is 400 days more than a year? -> {tmp}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    rose._stats.display()
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    print("[statistics for Rose]")
    rose._stats.display()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[statistics for Oak]")
    tree.display()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print("[statistics for Oak]")
    Global_Stats(tree)
    print()
    print("=== Seed")
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.grow()
    seed.age()
    seed.bloom()
    seed.show()
    print("[statistics for Sunflower]")
    Global_Stats(seed)
    print()
    print("=== Anonymous")
    anonymous = Plant.anonymous()
    #print("Unknown plant:", end = " ")
    anonymous.show()
    print("[statistics for Unknown plant]")
    Global_Stats(anonymous)
