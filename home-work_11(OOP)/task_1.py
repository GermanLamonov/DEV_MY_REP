class Soda:
    def __init__(self, taste):
        if taste == 'клубника':
            print('У Вас газировка со вкусом клубники')
        elif taste == 'апельсин':
            print('У Вас газировка со вкусом апельсина')
        else:
            print("У Вас простая газировка")


gazirovka = Soda(input("Выберите вкус газировки апельсин или клубника:\n"))
