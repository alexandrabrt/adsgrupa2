# var = 1
msg = "Hello1"
param_msg = "Hello2"

def functie():
    # param_msg = "Hello"
    print(param_msg, 'rand 5')
    # global var
    # print(var, 'linia 5')
    # var = 2
    # print(var, 'linia 5')
    # print(param_msg.upper())
    param_msg = "hello3"
    print(param_msg)
    return param_msg


# print(var, 'linia 7')
print(param_msg, 'linia 19')
functie()
# print(var, 'linia 9')
print(msg)
