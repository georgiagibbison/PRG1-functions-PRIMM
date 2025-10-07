def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius= (fahrenheit/9*5)-32
    return celsius
# Test the c to f function
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(20))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(-40))
# Test the f to c function 
print(fahrenheit_to_celsius(0))
print(fahrenheit_to_celsius(20))
print(fahrenheit_to_celsius(100))
print(fahrenheit_to_celsius(-40))


def kilometers_to_miles(kilometers):
    miles=kilometers*0.621371
    return miles
print (kilometers_to_miles(1))
print(kilometers_to_miles(5))