print("Ejemplo de aserciones en Micropython")
# Caso 1: Valor correcto
valor_sensor=500 #valor dentro del rango esperado(0 a 1023)
print("Asercion exitosa: valor_sensor=", valor_sensor)
assert 0<= valor_sensor <= 1023, "Valor del sensor fuera de rango"
print("Asercion exitosa:valor_sensor=", valor_sensor)
# Caso 2: Valor Incorrecto
valor_sensor_erroneo = 1500 #Valor fuera del rango esperado
try:
assert 0 <= valor_sensor_erroneo = 1023 #Valor del sensor fuera de rango "
try:
    assert 0<=Valor_sensor_erroneo <=1023, "Valor del sensor fuera del rango"
except AssertionError as error:
    print("Asercion fallo:", error)
