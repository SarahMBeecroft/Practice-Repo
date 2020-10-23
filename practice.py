def f_to_c():
    f_temp = int(input("Enter temperature in Fahrenheit: "))
    f_temp = str((f_temp - 32) * 5/9)
    print("The temperature in Celsius is: " + f_temp + " degrees.")


f_to_c()
