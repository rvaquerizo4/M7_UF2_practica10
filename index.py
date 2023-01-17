import pandas as pd

def ciutatPoblacio(ciudad1, ciudad2 , ciudad3 , ciudad4 ,ciudad5 ,ciudad6 ,ciudad7 ,ciudad8 ,ciudad9 ,ciudad10):
    list = pd.read_csv('list.csv')
    filtro = (list['City'] == ciudad1) | (list['City'] == ciudad2) | (list['City'] == ciudad2) | (list['City'] == ciudad3) | (list['City'] == ciudad4) | (list['City'] == ciudad5) | (list['City'] == ciudad6) | (list['City'] == ciudad7) | (list['City'] == ciudad8) | (list['City'] == ciudad9) | (list['City'] == ciudad10)
    listaCiudades = list[filtro]
    filtro2 = listaCiudades.columns[1:3]
    listaCiudades2 = listaCiudades[filtro2]
    #print(listaCiudades2)
    return listaCiudades2

    
ciutatPoblacio("Senglea", "Mandaluyong", "pateros", "Caloocan", "Katmandu", "Dakka", "Makati", "Manhattan", "Vincennes", "Kalküta")