class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f'У Вас газировка с {self.taste} вкусом'
        else:
            return "У Вас простая газировка"


gazirovka = Soda("клубничным")
print(gazirovka)
