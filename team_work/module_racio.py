x = 0
y = 0
z = 0

def init(a, b, c):
    global x
    global y
    global z
    x = a
    y = b
    z = c

def Сalculator(a, b, c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/' and b == 0:
        print("Деление на 0!")
    elif c == '/' and b != 0:
        return a/b
        
# P.s. предложение как данный модуль должен работать с другими
# Testing program:
# while True:
#     z = input("Знак (+,-,*,/): ")
#     if z == '0':
#         break
#     if z in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if z == '+':
#             print("%.2f" % (x+y))
#         elif z == '-':
#             print("%.2f" % (x-y))
#         elif z == '*':
#             print("%.2f" % (x*y))
#         elif z == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Error: Деление на ноль!")
#     else:
#         print("Error: Неверный знак операции!")