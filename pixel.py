class _ObjectCharacteristics():
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

class Sand(_ObjectCharacteristics):
    def __init__(self, name = "Sand", color = (238,207,161), speed = 30):
        super().__init__(name, color, speed)

