import indexb
import pandas as pd
import matplotlib.pyplot as plt



def graficos():
    print("--------Clock Speed------------")
    #Guardamos la funcion de mobilId en df
    df = indexb.mobilID()
    #Utilizando el pandas guardo el dataframe en nombres
    nombres = pd.DataFrame(df)
    #Hago unos filtros selecciona la columna que queremos con el pop
    filterMobile = nombres.pop("id")
    filterValores = nombres.pop("clock_speed")
    #Para evita que nos salga dispersada la grafica debido a los ids tan grandes, convertimos en un array la lista de ids y la casteo a string
    array = filterMobile.to_numpy()
    cast = []
    for i in array:
        cast += [str(i)]
    #Asignamos un espacio para la grafica
    fig = plt.figure(figsize = (10, 5))
    #Colores
    colores = ["#EE6055", "#60D394", "#AAF683", "#FFD97D", "#FF9B85", "#ff33d1", "#33b4ff", "#ff8633", "#33fff3",
               "#af33ff"]
    #Label de x
    plt.xlabel("ID")
    #Label de y
    plt.ylabel("Clock Speed")
    #Creamos la grafica con los valores de los filtros de antes, y le asignamos un width a las barras y un color con la array de antes
    plt.bar(cast, filterValores, width=0.4 , color=colores)
    #Asignamos un titulo
    plt.title("Clock Speed")
    #Mostramos la grafica
    plt.show()


    print("--------MegaPixels------------")
    df2 = indexb.mobilMP()
    nombres2 = pd.DataFrame(df2)
    filterValores2 = nombres2.pop("fc")
    fig = plt.figure(figsize = (10, 5))
    plt.xlabel("ID")
    plt.ylabel("Mega Pixels")
    plt.bar(cast, filterValores2, width=0.4, color=colores)
    plt.title("Mega Pixels")
    plt.show()

    print("--------battery_power------------")
    df3 = indexb.mobilBP()
    nombres3 = pd.DataFrame(df3)
    filterValores3 = nombres3.pop("battery_power")
    fig = plt.figure(figsize = (10, 5))
    plt.xlabel("ID")
    plt.ylabel("battery power")
    plt.bar(cast, filterValores3, width=0.4 ,color=colores)
    plt.title("Battery Power")
    plt.show()


#Llamada a la funcion
graficos()
