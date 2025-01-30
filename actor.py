class Actor:
    def __init__(self):
        self.name = ""
        self.speed = 0

    def __repr__(self):
        return f"{self.name} {self.speed}"