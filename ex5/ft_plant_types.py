class Plant:
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

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._current_age} days old")

    def grow(self) -> None:
        self._height = round(self._height + (0.03 * self._height), 1)

    def age(self) -> None:
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


class Flower(Plant):
    def __init__(self, name: str, height: float, current_age: int,
                 color: str):
        super().__init__(name, height, current_age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
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

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of"
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, current_age: int,
                 harvest_season: str):
        super().__init__(name, height, current_age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()

    def age(self) -> None:
        super().age()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    tree.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    for day in range(1, 21):
        tomato.grow()
        tomato.age()
        tomato.nutritional_value += 1
    tomato.show()
