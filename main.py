from calculadora import soma


# try:
#     print(soma('10', 20))
# except TypeError as e:
#     print('Conta inválida.')
#     print(e)


try:
    print(soma(10, 20))
except AssertionError as e:
    print(f'Conta inválida: {e}')

print('Conta', soma(25, 25))










