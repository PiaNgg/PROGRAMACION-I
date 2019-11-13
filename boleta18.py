# BOLETA DE VENTA DE BEBIDA ASLCOLICAS
bebida = input ( " INGRESO EL NOMBRE DE LA BEBIDA ALCHOLICA: " )
precio = float ( input ( " INGRESE EL PRECIO DE LA BEBIDA ALCHOLICA: " ))
unidades = int ( input ( " INGRESE LAS UNIDADES QUE DESEA LLEVAR: " ))
total = precio * unidades
igv = total * 0.18

print ( " ############################################## " )
imprimir ( " # LICOLERIA EL PARAISO # " )
print ( " # " )
print ( " # PRODUCTO: " + bebida)
print ( " # PU: " + str (precio))
print ( " # UNIDADES: " + str (unidades))
print ( " # IGV: " + str (igv))
print ( " # TOTAL A PAGAR: " + str (total))
print ( " # " )
print ( " ############################################### " )
