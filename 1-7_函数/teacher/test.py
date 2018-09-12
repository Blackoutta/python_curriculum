def add(num1, num2):
    return num1 + num2

total = add(100, 150)
print(total)

# age + (height - (iq/2) * weight)
add(age, subtract(height, multiply(weight, divide(iq, 2))))

# 24 + 34 / 100 - 1023
subtract(add(24, subtract(34/100)), 1023)
