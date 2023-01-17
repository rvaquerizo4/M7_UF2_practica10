import index
import pandas as pd
import matplotlib.pyplot as plt



def grafico1():
    df = index.ciutatPoblacio("Senglea", "Mandaluyong", "pateros", "Caloocan", "Katmandu", "Dakka", "Makati","Manhattan", "Vincennes", "Kalküta")
    nombres = pd.DataFrame(df)
    filterCiudad = nombres.pop("City")
    filterValores = nombres.pop("Population")
    cast = []
    array = filterValores.to_numpy()
    for i in array:
        cast += [i.replace(",", "")]

    fig1, ax1 = plt.subplots()
    colores = ["#EE6055", "#60D394", "#AAF683", "#FFD97D", "#FF9B85", "#ff33d1", "#33b4ff", "#ff8633", "#33fff3", "#af33ff" ]
    ax1.pie(cast, labels=filterCiudad, autopct="%0.1f%%", colors=colores, shadow=True, startangle=90, labeldistance = 1.2)
    ax1.axis('equal')
    plt.legend(loc="lower left")
    plt.show()


def grafico2():
    df = index.ciutatKM("Senglea", "Mandaluyong", "pateros", "Caloocan", "Katmandu", "Dakka", "Makati","Manhattan", "Vincennes", "Kalküta")
    nombres = pd.DataFrame(df)
    filterCiudad = nombres.pop("City")
    filterValores = nombres.pop("Density KM2")
    cast = []
    array = filterValores.to_numpy()
    for i in array:
        cast += [i.replace(",", "")]
    fig1, ax1 = plt.subplots()
    colores = ["#EE6055", "#60D394", "#AAF683", "#FFD97D", "#FF9B85", "#ff33d1", "#33b4ff", "#ff8633", "#33fff3", "#af33ff" ]
    ax1.pie(cast, labels=filterCiudad, autopct="%0.1f%%", colors=colores, shadow=True, startangle=90, labeldistance = 1.2)
    ax1.axis('equal')
    plt.legend(loc="lower left")
    plt.show()

def grafico3():
    df = index.ciutatM("Senglea", "Mandaluyong", "pateros", "Caloocan", "Katmandu", "Dakka", "Makati","Manhattan", "Vincennes", "Kalküta")
    nombres = pd.DataFrame(df)
    filterCiudad = nombres.pop("City")
    filterValores = nombres.pop("Density  M2")
    cast = []
    array = filterValores.to_numpy()
    for i in array:
        cast += [i.replace(",", "")]
    fig1, ax1 = plt.subplots()
    colores = ["#EE6055", "#60D394", "#AAF683", "#FFD97D", "#FF9B85", "#ff33d1", "#33b4ff", "#ff8633", "#33fff3", "#af33ff" ]
    ax1.pie(cast, labels=filterCiudad, autopct="%0.1f%%", colors=colores, shadow=True, startangle=90, labeldistance = 1.2)
    ax1.axis('equal')
    plt.legend(loc="lower left")
    plt.show()

print("--------Total de poblacio------------")
grafico1()
print("--------Densidad por KM2------------")
grafico2()
print("--------Densidad por M2------------")
grafico3()

