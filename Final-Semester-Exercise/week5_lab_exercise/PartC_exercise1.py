class Swimmer:
    def __init__(self):
        self.name = input("please enter the name of this swimmer: ")

    def get_name(self):
        return self.name

    def set_name(self):
        self.name = input("please enter the updated name of this swimmer: ")