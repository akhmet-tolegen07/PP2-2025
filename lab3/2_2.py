def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = int(input("Fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)

print(celsius)
