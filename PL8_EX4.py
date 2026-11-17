import math

a = float(input("Medida do lado A: "))
b = float(input("Medida do lado B: "))

c = math.hypot(a, b)
angle = math.degrees(math.atan2(b, a))

print(f"Hipotenusa: {round(c, 1)}")
print(f"Ângulo entre o lado A e a hipotenusa: {round(angle, 1)} graus")
