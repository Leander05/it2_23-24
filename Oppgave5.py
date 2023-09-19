

temperatur = str(input("skriv inn temperatur: "))
temp = temperatur
temperatur = temperatur.upper()
temperatur = temperatur.replace("F","")
temperatur = temperatur.replace("C","")

print(temperatur)
temperatur = float(temperatur)

print(temp)
if temp.index("F") == 1:
    temperatur = (temperatur - 32) * 5/9
    print(f"temperaturen i celsius = {temperatur:.1f}")
elif temp.index("C") == 1:
    temperatur = temperatur * (9/5) +32 
    print(f"temperaturen i farenheit = {temperatur:.1f}")
else:
    print("du skrev ikke C eller F")
