class Plant:
    def __init__(self, name: str, height: float, current_age: int) -> None:
        self.name = name
        self.height = height
        self.current_age = current_age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.current_age} days old")

    def grow(self) -> None:
        self.height = round(self.height + (0.03 * self.height), 1)

    def age(self) -> None:
        self.current_age = self.current_age + 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)
    start_height = rose.height
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    final_height = rose.height
    growth = round(final_height - start_height, 1)
    print(f"Growth this week: {growth}cm")
