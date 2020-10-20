def powGen(exp):
    def power(num):
        return num ** exp
    return power

square = powGen(2)
print(square(3))