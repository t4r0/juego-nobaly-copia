import os
os.system("cls")
print("Bienvenido a ¿Qué decides?")

contador = 100
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
os.system("cls")
print ("Bienvenido", nombre, "has entrado a una historia de la cual no podrás salir tan fácil. Se contará una historia, de la cual, tu eres el protagonista. Durante toda la historia se irán presentando decisiones que debes tomar sabiamente, una es la correcta y te permitirá avanzar sin mayor dificultad en la historia. Otra es una opción penalizadora, es decir, restará cierta cantidad de puntos a tu marcador, pero, no representará un riesgo para tu final. La última opción es incorrecta, ésta te llevará a un final inesperado. Existen distintos finales, de los cuales, solo uno es el correcto, tu objetivo es llegar al único final que te favorece sin perder la mayor cantidad de puntos. ")
print(nombre,", has llegado a Sídney, Australia. Son las 9:30 am. Has estado en un vuelo durante muchas horas y necesitas descansar. Caminas hacia el restaurante, tomas tu comida y te diriges hacia tu mesa. Vas tan cansado que no eres conciente de lo que sucede a tu alrededor. Sin darte cuenta, tropiezas con una persona... ")

print("1. Le alegas")
print("2. Te disculpas")
print("3. Lo ignoras")

a = int(input("¿Qué decides?: "))
os.system("cls")
if (a==1):
    contador = contador - 30
    print("//Opcion incorrecta, tu vida restante es de: ", contador, "puntos//")
    print("*Se caen las dos bandejas con comida*")
    print("tomas una actitud agresiva.")
    print("Tu: ¡Fíjate por donde caminas!")
    print("Él: ¿Yo? tu debes fijarte por donde caminas. Mira lo que ocasionaste, ")
    print("Tu: Eso no me importa, no estoy de humor para tratar con personas como tu, asi que vete de mi vista.")
    print("Él: Tu no eres nadie para tratarme así, no sabes con quien te estas metiendo.")
    print("Tu: ¿Qué me harás, irás corriendo con tu mamá para quejarte que alguien te trató mal?")
    print("*Él saca una navaja que llevaba en el bolsillo derecho del pantalón y te apuñala*")
    print("Afortunadamente para ti, no es una herida profunda pero pierdes sangre... ")
    
    print("1. Te quedas y lo enfrentas")
    print("2. Sales corriendo")
    print("3. Llamas a la policia")
    b = int(input("¿Qué decides?: "))
    os.system("cls")

    if (b == 1):
        contador = contador - 10
        print("//Opcion incorrecta, tu vida restante es de: ", contador, "puntos//")
        from Enfrenta_B1 import enfrenta
        enfrenta = ("Decides enfrentarlo a pesar de tu situación")
    elif (b == 2):
        contador = contador - 15
        print("//Opcion incorrecta, tu vida restante es de: ", contador, "puntos//")
        from Sale_corriendo import huyes
        huyes = ("Corres por tu vida")
    else: 
        print("El vato intenta dispararte, pero falla y le da a un policia, tu aprovechas y tomas su arma")
        print("1. Le apuntas")
        print("2. Hablan")
        print("3. Lo enfrentas")
        c = int(input("¿Qué haces?: "))
        os.system("cls")
        if (c == 1):
            print("Fallas y el vato te dispara. FIN DEL JUEGO")
        elif(c == 2):
            print("Lo distraes señalando hacia una ventana, el vato voltea y no habia nada, cuando voltea lo atacas por la espalda y pierden el equilibrio, caen desde el 8vo. piso y ambos mueren")
        else:
            from Enfrenta_B1 import enfrenta
            enfrenta = ("Decide enfrentarlo")
            os.system("cls")
            if(d == 1):
                print("Se cae del 8vo piso")

elif (a==2): 
    print("Te disculpas con el tipo y el responde: ")
    print("No te preocupes, debemos tener mas cuidado de donde caminamos, ¿Te parece si comemos juntos?, tu respondes que si, se hacen amigos y despues de un rato juntos el vato te pregunta ¿Vienes solo?")
    print("1. Si")
    print("2. No")
    print("3. Espero a alguien")
    b = int(input("¿Qué respondes?: "))
    os.system("cls")
    if (b == 1):
        print("Trata de convencerlo")
        #FALTA TERMINAR
    elif(b == 2):
        print("Me esperan en mi habitación. Luego siguen conversando y te retiras, vas a conocer la ciudad, tomas fotos, pruebas los dulces tipicos")
        #FALTA TERMINAR
    else:
        print("Espero a alguien, estoy aqui para una reunion de trabajo. ")
        #FALTA TERMINAR

else:
    print("")