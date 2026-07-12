class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Exhale Inhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater")

    def swim(self):
        print("Moving in water.")



nemo = Fish()

nemo.breathe()
