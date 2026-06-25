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


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()
    print()
    rose.set_height(25.0)
    print(f"Height updated: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated:{rose.get_age()} days")
    print()
    rose.set_height(-20)
    rose.set_age(-10)
    print()
    print("Current state:", end=" ")
    rose.show()
