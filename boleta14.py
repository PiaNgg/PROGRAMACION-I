# BOLETA DE VENTA DE UNA PANADERIA
tipo_pan_1 = input ( " INGRESE EL TIPO DE PAN: " )
tipo_de_pan_2 = input ( " INGRESE EL TIPO DE PAN: " )
P_U_1 = flotante ( entrada ( " INGRESO EL PRECIO UNITARIO DEL PRIMER TIPO DE PAN: " ))
P_U_2 = flotante ( entrada ( " INGRESO EL PRECIO UNITARIO DEL SEGUNDO TIPO DE PAN: " ))
unidades_1 = int ( input ( " INGRESO LAS UNIDADES DEL PRIMER TIPO DE PAN: " ))
unidades_2 = int ( input ( " INGRESO LAS UNIDADES DEL SEGUNDO TIPO DE PAN: " ))
TOTAL = P_U_1 * unidades_1 + P_U_2 * unidades_2

print ( " ############################################### ######## " )
print ( " # PANADERIA ´´DON JUAN´´ # " )
print ( " # " )
print ( " # PRIMER TIPO DE PAN: " + tipo_pan_1)
print ( " # SEGUNDI TIPO DE PAN: " + tipo_de_pan_2)
print ( " # PU 1: " + str ( P_U_1 ))
print ( " # PU 2: " + str ( P_U_2 ))
print ( " # UNIDADES 1 °: " + str (unidades_1))
print ( " # UNIDADES 2 °: " + str (unidades_2))
print ( " # TOTAL A PAGAR: " + str ( TOTAL ))
print ( " # " )
print ( " ############################################### ########## " )
