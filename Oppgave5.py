

temp = float(input("skriv inn temperatur: "))
type = input("skriv F for farenheit og C for celsius: ")

if type == "F":
    temp = (temp - 32) * 5/9
    print(f"temperaturen i celsius = {temp:.1f}")
elif type == "C":
    temp = temp * (9/5) +32 
    print(f"temperaturen i farenheit = {temp:.1f}")
else:
    print("du skrev ikke C eller F")
