
  
# en este programa le pediremos al usuario  que ingrese 2 coordenadas que estran entre los numeros positivos o negativos los cuadrantes #los coloque con las 
#siguentes relaciones segun entendi yo cuadrante1 (++) cuadrante2 (-+) cuadrante3 (--) cuadrante4 (+-) 

#en esta parte solicito los datos y los guardo en una variable
 x = float(input('Ingresa la coordenada de x: ')) 
 y = float(input('Ingresa la coordenada de y: '))

# # aqui inician las codiciones si el numero de cada variable coincide con los cuadrantes es decir las cuatro combinaciones posibles pues mandara un mensaje 
# # donde indique en que cuandrante se encuentra en caso de ser ambas variables 0 entonces indicara que es el punto de origen
 if((x>0) and (y>0)):
  print(+x+' y '+y+'se encuentran en el primer cuadrante')

elif((x<0) and (y>0)):
 print(+x+' y '+y+'se encuentran en el segundo cuadrante')

elif((x<0) and (y<0)):
  print(+x+' y '+y+'se encuentran en el tercer cuadrante')

elif((x>0) and (y<0)):
  print(+x+' y '+y+'se encuentran en el cuarto cuadrante')

else:
  print('PUNTO EN EL ORIGEN')
