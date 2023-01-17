import index
import pandas as pd
import matplotlib.pyplot as plt



def graficos():
    df = index.ciutatPoblacio("Senglea", "Mandaluyong", "pateros", "Caloocan", "Katmandu", "Dakka", "Makati","Manhattan", "Vincennes", "Kalküta")
    nombres = pd.DataFrame(df)
    filterCiudad = nombres.pop("City")
    filterValores = nombres.pop("Population")
    cast= float(filterValores.replace(',',''))
    fig1, ax1 = plt.subplots()
    colores = ["#EE6055", "#60D394", "#AAF683", "#FFD97D", "#FF9B85", "#ff33d1", "#33b4ff", "#ff8633", "#33fff3", "#af33ff" ]
    ax1.pie(cast, labels=filterCiudad, autopct="%0.1f %%", colors=colores, shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

graficos()

