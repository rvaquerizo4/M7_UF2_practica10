import pandas as pd

def mobilID():
    #Guardamos la lista en la variable list
    list = pd.read_csv('list.csv')
    #Hacemos un filtro para seleccionar solo las ids que queremos
    filtro = (list['id'] == 3) | (list['id'] == 13) | (list['id'] == 34) | (list['id'] == 56) | (list['id'] == 70) | (list['id'] == 85) | (list['id'] == 110) | (list['id'] == 120) | (list['id'] == 210) | (list['id'] == 400)
    #Aplicamos el filtro
    listaMobiles = list[filtro]
    #Hacemos un segundo filtro donde seleccionamos estas columnas con el isin
    filtro2 = listaMobiles.columns.isin(['id', 'clock_speed'])
    # Aplicamos el filtro
    selectedCols = listaMobiles.columns[filtro2]
    listaCiudades2 = listaMobiles[selectedCols]
    print(listaCiudades2)
    return listaCiudades2


def mobilMP():
    list = pd.read_csv('list.csv')
    filtro = (list['id'] == 3) | (list['id'] == 13) | (list['id'] == 34) | (list['id'] == 56) | (list['id'] == 70) | (list['id'] == 85) | (list['id'] == 110) | (list['id'] == 120) | (list['id'] == 210) | (list['id'] == 400)
    listaMobiles = list[filtro]
    filtro2 = listaMobiles.columns.isin(['id', 'fc'])
    selectedCols = listaMobiles.columns[filtro2]
    listaCiudades2 = listaMobiles[selectedCols]
    print(listaCiudades2)
    return listaCiudades2

def mobilBP():
    list = pd.read_csv('list.csv')
    filtro = (list['id'] == 3) | (list['id'] == 13) | (list['id'] == 34) | (list['id'] == 56) | (list['id'] == 70) | (list['id'] == 85) | (list['id'] == 110) | (list['id'] == 120) | (list['id'] == 210) | (list['id'] == 400)
    listaMobiles = list[filtro]
    filtro2 = listaMobiles.columns.isin(['id', 'battery_power'])
    selectedCols = listaMobiles.columns[filtro2]
    listaCiudades2 = listaMobiles[selectedCols]
    print(listaCiudades2)
    return listaCiudades2

#Llamadas a las funciones
print("----------Clock-Speed---------------")
mobilID()
print("----------Mega Pixels----------------")
mobilMP()
print("----------Battery Power--------------")
mobilBP()

