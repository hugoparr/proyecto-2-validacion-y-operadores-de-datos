

print('')
print('VAMOS A COMPROBAR LAS LETRAS DE UAN PALABRA SI SOBRAN, SI FALTAN O SI LAS LETRAS DE LA PALABARA SON EXACTAMENTE LAS QUE EL PROGRAMA SOLICITA')
print('')

#en esta linea guardamos la variable palabra con el tipo de variable que necesitamos en este caso string  ademas de indicarle al usuario que debe ingresar en su teclado
palabra = input(str("Introduce una palabra que tenga entre 4 y 8 letras porfavor: "))

#aqui iniciamos con las condiciones if donde escribiremos el mensaje que se dara en cada caso posible dentro de los limites

#si faltan letras mandamos un mensaje donde indiquemos la palabra y cuantas letras faltan
if len(palabra) < 4:
 
  print('Faltan letras, la palabra '+ palabra + " solo tiene " + str(len(palabra)) + " letras deben ser al menos 4")

#si sobran le mandamos un mensaje con la palabra y cuantas letrsa faltan 
elif len(palabra) > 8:
 
  print('Sobran letras, la palabra '+ palabra + " tiene " + str(len(palabra)) + " no deberian ser mas de 8")

#la ultima condicion donde use el (and) para indicarle que se mandaria el mensaje en caso de quen la palabra tenga 4,5,6,7 u 8 letras
elif len(palabra) == 4 and 5 and 6 and 7 and 8:

  print('la palabra es valida ya que ' +palabra+' tiene ' +str(len(palabra))+' letras y entra en el rango de 4 a 8 letras') 

else :
  print('no es caracter valido')



  
