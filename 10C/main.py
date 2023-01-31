import index
import pandas as pd
import matplotlib.pyplot as plt



def graficos():
    print("--------Casos totals per mes------------")
    #Guardamos la funcion de mobilId en df
    df = index.paisQuantitat("Albania", "Algeria", "Argentina", "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France", "Afghanistan")
    filterAlbania = df.loc[['Albania']]


    print(filterAlbania)
    """
    plt.plot(df['location'] =='Albania')
    plt.plot(df['location'] =='Algeria')
    plt.plot(df['location'] =='Argentina')
    plt.plot(df['location'] =='Mexico')
    plt.plot(df['location'] =='Thailand')
    plt.plot(df['location'] =='Japan')
    plt.plot(df['location'] =='Singapore')
    plt.plot(df['location'] =='Spain')
    plt.plot(df['location'] =='France')
    plt.plot(df['location'] =='Afghanistan')
    plt.legend()
    plt.show()

"""

    """
    print("--------MegaPixels------------")
    df2 = index.mobilMP()
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
    """

#Llamada a la funcion
graficos()
