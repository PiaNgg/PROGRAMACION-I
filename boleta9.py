# BOLETA DE VENTA DE TIENDA DEPORTIVA
nombre_del_producto = input ( " INGRESO EL NOMBRE DEL PRODUCTO: " )
unidades_del_producto = int ( input ( " INGRESE LAS UNIDADES DEL PRODUCTO: " ))
precio_unitario = float ( input ( " INGRESE EL PRECIO UNITARIO DEL PRODUCTO: " ))
igv = (unidades_del_producto * precio_unitario) * 0.18
TOTAL = (unidades_del_producto * precio_unitario) + igv

imprimir ( " HACIENDO EL CALCULO .... " )

print ( " ############################################### ########### " )
print ( " # ´´CASA DEL DEPORTE´´ # " )
print ( " # " )
print ( " # PRODUCTO: " + nombre_del_producto)
print ( " # UNIDADES: " + str (unidades_del_producto))
print ( " # PU: " + str (precio_unitario))
print ( " # IGV: " + str (igv))
print ( " # TOTAL A PAGAR: " + str ( TOTAL ))
print ( " # " )
print ( " ############################################### ########### " )
