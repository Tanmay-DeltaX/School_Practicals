amount = int(input("Enter the principal amount"))
rate = int(input("Enter the rate of interest"))
time = int(input("Enter the time for which the amount has to be invested"))

interest = amount*time*rate/100
print(interest)