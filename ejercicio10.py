# CÁLCULO DE LA EFICIENCIA DE UNA MAQUINA
energia_total, energia_perdida, energia_util = 0.0 , 0.0 , 0.0

# ASIGNACION DE VALORES
energia_total = 240
energia_perdida = 100

# CALCULO
energia_util = energia_total - energia_perdida
eficiencia_de_una_maquina = (energia_util / energia_total) * 100

# MOSTRAR VALORES
print ( " La energía total de una máquina es: " + str (energia_total))
print ( " La energía perdida de una máquina es: " + str (energia_perdida))
print ( " La energía de una máquina es: " + str (energia_util))
print ( " La eficiencia de una máquina es: " + str (eficiencia_de_una_maquina))
