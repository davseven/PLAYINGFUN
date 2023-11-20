#MENU INTERCATIVO (Aplicación interactiva que integra juegos.)
print ("WELCOME TO THE PLAYINGFUN APP")
while ("True"):
    print ("""¿A qué tenes ganas de jugar? Elige una opcion
    1) PIEDRA PAPEL O TIJERA CONTRA LA MATRIX
    2) ADIVINAR UN NUMERO ENTRE 1 Y 10
    3) TIRAR UN DADO
    4) SALIR, NO TENGO GANAS DE JUGAR""")
    
    opción = input ()
    if opción == "1":
        print ("¿te atreves a jugar PIEDRA, PAPEL o TIJERA contra LA MATRIX?")

        import random

        opciones = ("piedra", "papel", "tijera")

        player1 = 0 
        matrix = random.choice (opciones)

        while player1 not in opciones:
            player1 = input ("Elegi una opcion (piedra, papel o tijera): ")

            print (f"Player1: {player1}")
            print (f"La Matrix: {matrix} ")

            if player1 == matrix:
                    print ('JUEGO EMPATADO!')
            elif player1 == "piedra" and matrix == "tijera":
                    print ('LE GANASTE A LA MATRIX!')
            elif player1 == 'papel' and matrix == "piedra":
                    print ('LE GANASTE A LA MATRIX')
            elif player1 == 'tijera' and matrix == "papel":
                    print ('LE GANASTE A LA MATRIX')
            else:
                    print ("PERDISTE!")

    
    elif opción == "2":   

        print ("¿TE SENTIS CON SUERTE HOY? ¡ADIVINA EN QUE NUMERO ESTOY PENSANDO!")
        import random

        numero = random.randint (1, 10)
        mi_numero = 0

        while mi_numero != numero:
            mi_numero = int (input ('ELIGE UN NUMERO ENTRE EL 1 Y EL 10: '))

            if (mi_numero < numero):
                print ('Intenta con un numero mas alto!')
            elif (mi_numero > numero):
                print ('Intenta con un numero mas bajo!')
            else:
                print ('ADIVINASTE! FELICITACIONES!')
    
    elif opción == "3":
        print ("¡Proba tu suerte tirando el dado!")
        import random


        tiro = input('Para tirar el DADO presiona ENTER')
        resultado = random.randint (1,6)
        print ('El resultado de tu tiro es:', resultado)

    elif opción == "4":
        print ("¡ESPERO QUE TE HAYAS DIVERTIVO!¡NOS VEMOS LA PROXIMA!")
        break
    
    else:
        print ("Comando desconocido, elije un número entre el 1 y el 4")


  

        
