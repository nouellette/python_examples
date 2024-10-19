class PET:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def display_info(self):
        print(f'Name: {self.name} with {self.legs} legs.')



class DOG(PET):
    def __init__(self, name, legs, color):
        super().__init__(name, legs)
        self.color = color

    def display_info(self):
        print('I have no logs')

class CAT(PET):
    def __init__(self, name, legs, color):
        super().__init__(name, legs)
        self.color = color

    def display_info(self):
        super().display_info()

dog = DOG('Pup', 4, 'black')
cat = CAT('Kitty', 4, 'white')

dog.display_info()
cat.display_info()