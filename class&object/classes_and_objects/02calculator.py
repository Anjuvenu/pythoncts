class Calculator:
    def __init__(self, num1, num2):
        self.Number_1 = num1
        self.Number_2 = num2
        self.sum = None
        self.power_of = None
        self.divisible = None
        self.product = None
        self.difference = None

    def addition(self):
        self.sum = self.Number_1 + self.Number_2
        print(f"{self.Number_1}+{self.Number_2} = {self.sum}")

    def subtraction(self):
        self.difference = self.Number_1 - self.Number_2
        print(f"{self.Number_1}-{self.Number_2} = {self.difference}")

    def multiplication(self):
        self.product = self.Number_1 * self.Number_2
        print(f"{self.Number_1}*{self.Number_2} = {self.product}")

    def division(self):
        self.divisible = self.Number_1 / self.Number_2
        print(f"{self.Number_1}/{self.Number_2} = {self.divisible}")

    def power(self):
        self.power_of = self.Number_1 ** self.Number_2
        print(f"{self.Number_1}^{self.Number_2} = {self.power_of}")

def input_fun():
    input_Number1 = int(input("Enter the first number:"))
    input_Number2 = int(input("Enter the second number:"))
    input_function = input("Enter the operation (Either: +,-,*,/,^)")
    Calc_1 = Calculator(input_Number1, input_Number2)
    if input_function == "+":
        Calc_1.addition()
    elif input_function == "-":
        Calc_1.subtraction()
    elif input_function == "*":
        Calc_1.multiplication()
    elif input_function == "/":
        Calc_1.division()
    elif input_function == "^":
        Calc_1.power()
input_fun()
