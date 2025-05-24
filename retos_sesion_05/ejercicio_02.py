# conversor de temperatura de Farenheit a Celsius
# Datos de temperaturas son: 1= 25 farenheit, 2= 300 farenheit, 3=76 farenheit
# Fórmula de conversión: (°F - 32) * 5/9 para obtener celsius

temp1_f = 25
temp2_f = 300
temp3_f = 76
temp1_c = (temp1_f - 32) * 5/9
temp2_c = (temp2_f - 32) * 5/9
temp3_c = (temp3_f - 32) * 5/9

print(f"{temp1_f}°F = {temp1_c:.2f}°C")
print(f"{temp2_f}°F = {temp2_c:.2f}°C")
print(f"{temp3_f}°F = {temp3_c:.2f}°C")