class PET:
    def display_name(self, name):
        return f'My pets name is: {name}'


class DOG(PET):
    def display_name(self, name):
        return f'My dogs name is: {name}'

class CAT(PET):
    pass

cat = DOG()
print(cat.display_name('kitty'))