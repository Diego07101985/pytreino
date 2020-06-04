
def saudacao(saudacao="Ola", nome="Agnes"):
    print(saudacao, nome)


saudacao()


def soma(num1, num2, num3):
    sum = num1+num2+num3
    print(sum)


soma(1, 2, 3)


def percentual_number(valor, percentual):
    return valor * (percentual/100)


print('{0}%'.format(percentual_number(100, 10)))


def divi(number):

    if (number % 5) == 0 and (number % 3) == 0:
        return f'{number} FizzBuzz'
    elif number % 3 == 0:
        return f'{number} fizz'
    elif number % 5 == 0:
        return f'{number} buzz'

    return number


print('{0}'.format(divi(3)))
