# Генератор для циклической последовательности чисел
def cyclic_generator(sequence):
    while True:
        for number in sequence:
            yield number


n = int(input("Введите количество чисел для вывода: "))

sequence = [1, 2, 3]

gen = cyclic_generator(sequence)

print("Циклическая последовательность:")
for i in range(n):
    print(next(gen), end=" ")
