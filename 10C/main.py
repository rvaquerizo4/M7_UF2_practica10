import index
import pandas as pd
import matplotlib.pyplot as plt



def grafico1():
    print("--------Casos totals per mes------------")
    #Guardamos la funcion de mobilId en df
    df = index.paisQuantitat("Albania", "Algeria", "Argentina", "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France", "Afghanistan")
    # Separem les dades pais per pais y agafem nmomes la fila que volem
    filterAlbania = df.loc[['Albania']]
    Albania = filterAlbania.loc['Albania']
    # plotejem el df i fem que a cada punt el marqui amb una x i seleccionem un color
    plt.plot(Albania, 'x-m')

    # Separem les dades pais per pais y agafem nmomes la fila que volem
    filterAlgeria = df.loc[['Algeria']]
    Algeria = filterAlgeria.loc['Algeria']
    # plotejem el df i fem que a cada punt el marqui amb una x i seleccionem un color
    plt.plot(Algeria, 'x-k')

    # Separem les dades pais per pais y agafem nmomes la fila que volem
    filterArgentina = df.loc[['Argentina']]
    Argentina = filterArgentina.loc['Argentina']
    # plotejem el df i fem que a cada punt el marqui amb una x i seleccionem un color
    plt.plot(Argentina, 'x-c')

    # Separem les dades pais per pais y agafem nmomes la fila que volem
    filterMexico = df.loc[['Mexico']]
    Mexico = filterMexico.loc['Mexico']
    # plotejem el df i fem que a cada punt el marqui amb una x
    plt.plot(Mexico, 'x-')

    # Separem les dades pais per pais y agafem nmomes la fila que volem
    filterThailand = df.loc[['Thailand']]
    Thailand = filterThailand.loc['Thailand']
    # plotejem el df i fem que a cada punt el marqui amb una x
    plt.plot(Thailand, 'x-')

    filterJapan = df.loc[['Japan']]
    Japan = filterJapan.loc['Japan']
    # plotejem el df i fem que a cada punt el marqui amb una x
    plt.plot(Japan, 'x-')

    # Separem les dades pais per pais y agafem nmomes la fila que volem
    filterSingapore = df.loc[['Singapore']]
    Singapore = filterSingapore.loc['Singapore']
    # plotejem el df i fem que a cada punt el marqui amb una x i seleccionem un color
    plt.plot(Singapore, 'x-g')

    # Separem les dades pais per pais y agafem nmomes la fila que volem
    filterSpain = df.loc[['Spain']]
    Spain = filterSpain.loc['Spain']
    # plotejem el df i fem que a cada punt el marqui amb una x i seleccionem un color
    plt.plot(Spain, 'x-r')

    # Separem les dades pais per pais y agafem nmomes la fila que volem
    filterFrance = df.loc[['France']]
    France = filterFrance.loc['France']
    # plotejem el df i fem que a cada punt el marqui amb una x i seleccionem un color
    plt.plot(France, 'x-b')

    #Separem les dades pais per pais y agafem nmomes la fila que volem
    filterAfghanistan = df.loc[['Afghanistan']]
    Afghanistan = filterAfghanistan.loc['Afghanistan']
    #plotejem el df i fem que a cada punt el marqui amb una x i de color yellow
    plt.plot(Afghanistan, 'x-y')

    #Labels de x i y
    plt.ylabel("casos totals")
    plt.xlabel("months")
    #titol
    plt.title("total de casos per mes")
    #Llegenda
    plt.legend(['Albania', 'Algeria', 'Argentina', "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France", "Afghanistan"])
    #imprimir la grafica
    plt.show()

def grafico2():
    print("--------Morts totals------------")
    df2 = index.mortsTotals("Albania", "Algeria", "Argentina", "Mexico", "Thailand", "Japan", "Singapore", "Spain",
                             "France", "Afghanistan")
    filterAlbania2 = df2.loc[['Albania']]
    Albania2 = filterAlbania2.loc['Albania']
    plt.plot(Albania2, 'x-m')

    filterAlgeria2 = df2.loc[['Algeria']]
    Algeria2 = filterAlgeria2.loc['Algeria']
    plt.plot(Algeria2, 'x-k')

    filterArgentina2 = df2.loc[['Argentina']]
    Argentina2 = filterArgentina2.loc['Argentina']
    plt.plot(Argentina2, 'x-c')

    filterMexico2 = df2.loc[['Mexico']]
    Mexico2 = filterMexico2.loc['Mexico']
    plt.plot(Mexico2, 'x-')

    filterThailand2 = df2.loc[['Thailand']]
    Thailand2 = filterThailand2.loc['Thailand']
    plt.plot(Thailand2, 'x-')

    filterJapan2 = df2.loc[['Japan']]
    Japan2 = filterJapan2.loc['Japan']
    plt.plot(Japan2, 'x-')

    filterSingapore2 = df2.loc[['Singapore']]
    Singapore2 = filterSingapore2.loc['Singapore']
    plt.plot(Singapore2, 'x-g')

    filterSpain2 = df2.loc[['Spain']]
    Spain2 = filterSpain2.loc['Spain']
    plt.plot(Spain2, 'x-r')

    filterFrance2 = df2.loc[['France']]
    France2 = filterFrance2.loc['France']
    plt.plot(France2, 'x-b')

    filterAfghanistan2 = df2.loc[['Afghanistan']]
    Afghanistan2 = filterAfghanistan2.loc['Afghanistan']
    plt.plot(Afghanistan2, 'x-y')

    plt.ylabel("morts totals")
    plt.xlabel("months")
    plt.title("total de morts per mes")
    plt.legend(['Albania', 'Algeria', 'Argentina', "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France",
                "Afghanistan"])
    plt.show()
def grafico3():
    print("--------reproduction rate------------")
    df2 = index.reproduccionRate("Albania", "Algeria", "Argentina", "Mexico", "Thailand", "Japan", "Singapore", "Spain",
                            "France", "Afghanistan")
    filterAlbania2 = df2.loc[['Albania']]
    Albania2 = filterAlbania2.loc['Albania']
    plt.plot(Albania2, 'x-m')

    filterAlgeria2 = df2.loc[['Algeria']]
    Algeria2 = filterAlgeria2.loc['Algeria']
    plt.plot(Algeria2, 'x-k')

    filterArgentina2 = df2.loc[['Argentina']]
    Argentina2 = filterArgentina2.loc['Argentina']
    plt.plot(Argentina2, 'x-c')

    filterMexico2 = df2.loc[['Mexico']]
    Mexico2 = filterMexico2.loc['Mexico']
    plt.plot(Mexico2, 'x-')

    filterThailand2 = df2.loc[['Thailand']]
    Thailand2 = filterThailand2.loc['Thailand']
    plt.plot(Thailand2, 'x-')

    filterJapan2 = df2.loc[['Japan']]
    Japan2 = filterJapan2.loc['Japan']
    plt.plot(Japan2, 'x-')

    filterSingapore2 = df2.loc[['Singapore']]
    Singapore2 = filterSingapore2.loc['Singapore']
    plt.plot(Singapore2, 'x-g')

    filterSpain2 = df2.loc[['Spain']]
    Spain2 = filterSpain2.loc['Spain']
    plt.plot(Spain2, 'x-r')

    filterFrance2 = df2.loc[['France']]
    France2 = filterFrance2.loc['France']
    plt.plot(France2, 'x-b')

    filterAfghanistan2 = df2.loc[['Afghanistan']]
    Afghanistan2 = filterAfghanistan2.loc['Afghanistan']
    plt.plot(Afghanistan2, 'x-y')

    plt.ylabel("reproduction rate")
    plt.xlabel("months")
    plt.title("reproducció per mes")
    plt.legend(['Albania', 'Algeria', 'Argentina', "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France",
                "Afghanistan"])
    plt.show()


#Llamada a la funcion
grafico1()
grafico2()
grafico3()
