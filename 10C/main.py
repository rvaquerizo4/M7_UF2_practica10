import index
import pandas as pd
import matplotlib.pyplot as plt



def graficos():
    print("--------Total de poblacio------------")
    df = index.ciutatPoblacio("Senglea", "Mandaluyong", "pateros", "Caloocan", "Katmandu", "Dakka", "Makati","Manhattan", "Vincennes", "Kalküta")
    nombres = pd.DataFrame(df)
    filterpais = nombres.pop("location")
    filterValores = nombres.pop("Population")
    cast = []
    array = filterValores.to_numpy()
    for i in array:
        cast += [i.replace(",", "")]

    fig1, ax1 = plt.subplots()
    colores = ["#EE6055", "#60D394", "#AAF683", "#FFD97D", "#FF9B85", "#ff33d1", "#33b4ff", "#ff8633", "#33fff3", "#af33ff"]
    ax1.pie(cast, labels=filterpais, autopct="%0.1f%%", colors=colores, shadow=True, startangle=90, labeldistance = 1.2)
    ax1.axis('equal')
    plt.title("Total de poblacio", loc="left")
    plt.legend(loc="lower left")
    plt.show()


    print("--------Densidad por KM2------------")
    df2 = index.ciutatKM("Senglea", "Mandaluyong", "pateros", "Caloocan", "Katmandu", "Dakka", "Makati","Manhattan", "Vincennes", "Kalküta")
    nombres2 = pd.DataFrame(df2)
    filterpais2 = nombres2.pop("location")
    filterValores2 = nombres2.pop("Density KM2")
    cast2 = []
    array2 = filterValores2.to_numpy()
    for i in array2:
        cast2 += [i.replace(",", "")]
    fig2, ax2 = plt.subplots()
    colores2 = ["#EE6055", "#60D394", "#AAF683", "#FFD97D", "#FF9B85", "#ff33d1", "#33b4ff", "#ff8633", "#33fff3", "#af33ff"]
    ax2.pie(cast2, labels=filterpais2, autopct="%0.1f%%", colors=colores2, shadow=True, startangle=90, labeldistance = 1.2)
    ax2.axis('equal')
    plt.legend(loc="lower left")
    plt.title("Densidad por KM2", loc="left")
    plt.show()


    print("--------Densidad por M2------------")
    df3 = index.ciutatM("Senglea", "Mandaluyong", "pateros", "Caloocan", "Katmandu", "Dakka", "Makati","Manhattan", "Vincennes", "Kalküta")
    nombres3 = pd.DataFrame(df3)
    filterpais3 = nombres3.pop("location")
    filterValores3 = nombres3.pop("Density  M2")
    cast3 = []
    array3 = filterValores3.to_numpy()
    for i in array3:
        cast3 += [i.replace(",", "")]
    fig3, ax3 = plt.subplots()
    colores3 = ["#EE6055", "#60D394", "#AAF683", "#FFD97D", "#FF9B85", "#ff33d1", "#33b4ff", "#ff8633", "#33fff3", "#af33ff"]
    ax3.pie(cast, labels=filterpais3, autopct="%0.1f%%", colors=colores3, shadow=True, startangle=90, labeldistance = 1.2)
    ax3.axis('equal')
    plt.title("Densidad por M2", loc="left")
    plt.legend(loc="lower left")
    plt.show()



graficos()

