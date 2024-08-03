#It is same as global variable and local variable

x=4 #--------global variable is variable tha declare on codes main body we can acess everywhere in the code
def glo():
    print(x)
print(x+5)


def g():
    y=5 #here this variabl can only use inside the function
    print(y)

def av():
    global z  #by this way we can create a global variable inside a function
    z=8
    print(z)
print(z)