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
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    plants = [rose, oak, cactus, sunflower, fern]
    for plant in plants:
        print("Created:", end=" ")
        plant.show()
