# BOLETA DE NOTAS DE TRES ÁREAS
alumno = input ( " INGRESE EL NOMBRE DEL ALUMNO: " )
area_1 = input ( " INGRESE LA PRIMERA AREA: " )
nota_1 = float ( input ( " INGRESE LA NOTA DE LA PRIMERA AREA: " ))
area_2 = input ( " INGRESE LA SEGUNDA AREA: " )
nota_2 = float ( input ( " INGRESE LA NOTA DE LA SEGUNDA AREA: " ))
area_3 = input ( " INGRESE LA SEGUNDA AREA: " )
nota_3 = float ( input ( " INGRESE LA TERCERA NOTA: " ))
promedio = (nota_1 + nota_2 + nota_3) / 3

print ( " ############################################### ################ " )
print ( " # COLEGIO ´´JUAN MEJIA BACA´´ # " )
print ( " # " )
print ( " # ALUMNO: " + alumno)
print ( " # " )
imprimir ( " # ÁREA 1    " + " ÁREA 2   " + " ÁREA 3    " )
print ( " # " + str (nota_1) + "       " + str (nota_2) + "      " + str (nota_3))
print ( " # " )
print ( " # PROMEDIO: " + str (promedio))
print ( " # " )
print ( " ############################################### ################ " )
