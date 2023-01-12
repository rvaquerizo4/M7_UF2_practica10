import index
import pandas as pd
import matplotlib.pyplot as plt
import PIL
from PIL import Image
from PIL import _imaging


def graficos():
    df = index.ciutatPoblacio("Senglea", "Mandaluyong", "pateros", "Caloocan", "Katmandu", "Dakka", "Makati","Manhattan", "Vincennes", "Kalküta")
    nombres = pd.DataFrame(df)
    filterCiudad = nombres.pop("City")
    filterValores = nombres.pop("Population")
    cast= float(filterValores.replace(',',''))
    colores = ["#EE6055", "#60D394", "#AAF683", "#FFD97D", "#FF9B85", "#ff33d1", "#33b4ff", "#ff8633", "#33fff3", "#af33ff" ]
    #plt.pie(cast, labels=filterCiudad, autopct="%0.1f %%", colors=colores)
    #plt.axis("equal")
    #plt.show
    print(cast)

graficos()

