#discuklpe no pude hacer qie mabos programas se ejecutaran en paralelo asi que comente uno para dejar que el primero trabaje porfavor comente el primero y descomente el segundo para que pueda funcionar 


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



  
# # en este programa le pediremos al usuario  que ingrese 2 coordenadas que estran entre los numeros positivos o negativos los cuadrantes los coloque con las 
# # siguentes relaciones segun entendi yo cuadrante1 (++) cuadrante2 (-+) cuadrante3 (--) cuadrante4 (+-) 

# #en esta parte solicito los datos y los guardo en una variable
# x = float(input('Ingresa la coordenada de x: ')) 
# y = float(input('Ingresa la coordenada de y: '))

# # aqui inician las codiciones si el numero de cada variable coincide con los cuadrantes es decir las cuatro combinaciones posibles pues mandara un mensaje 
# # donde indique en que cuandrante se encuentra en caso de ser ambas variables 0 entonces indicara que es el punto de origen
# if((x>0) and (y>0)):
#  print(+x+' y '+y+'se encuentran en el primer cuadrante')

# elif((x<0) and (y>0)):
#  print(+x+' y '+y+'se encuentran en el segundo cuadrante')

# elif((x<0) and (y<0)):
#  print(+x+' y '+y+'se encuentran en el tercer cuadrante')

# elif((x>0) and (y<0)):
#  print(+x+' y '+y+'se encuentran en el cuarto cuadrante')

# else:
#   print('PUNTO EN EL ORIGEN')
