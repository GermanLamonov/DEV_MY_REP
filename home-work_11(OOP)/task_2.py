class Math:

    def addition(self, a, b):

        result = a + b
        print(f"Результат сложения {a} и {b}  = {result}")

    def subtraction(self, a, b):
        result = a - b
        print(f"Результат вычитания {a} и {b} = {result}")

    def multiplication(self, a, b):
        result = a * b
        print(f"Результат умножения {a} и {b} = {result}")

    def division(self, a, b):
        if b == 0:
            print("На ноль делить нельзя")
        else:
            result = a / b
            print(f"Результат деления {a} на {b} = {result}")


math_go = Math()
math_go.addition(5, 7)
math_go.subtraction(8, 5)
math_go.multiplication(5, 8)
math_go.division(6, 5)