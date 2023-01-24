import pandas as pd

def paisQuantitat(pais1, pais2 , pais3 , pais4 ,pais5 ,pais6 ,pais7 ,pais8 ,pais9 ,pais10):
    list = pd.read_csv('list.csv')
    filtro = (list['location'] == pais1) | (list['location'] == pais2) | (list['location'] == pais2) | (list['location'] == pais3) | (list['location'] == pais4) | (list['location'] == pais5) | (list['location'] == pais6) | (list['location'] == pais7) | (list['location'] == pais8) | (list['location'] == pais9) | (list['location'] == pais10)
    listapaises = list[filtro]
    filtro2 = listapaises.columns.isin(['location', 'date', 'total_cases'])
    selectedCols = listapaises.columns[filtro2]
    listapaises2 = listapaises[selectedCols]
    separar = listapaises2.date.str.split(pat='-', expand=True)
    listapaises3 = pd.DataFrame(separar, columns=[1])
    listapaises4 = pd.DataFrame(listapaises2, columns=["location", "total_cases"])
    listaDefinitiva = pd.concat([listapaises4, listapaises3], axis=1)
    print(listaDefinitiva)

    return listapaises2

def mortsTotals(pais1, pais2 , pais3 , pais4 ,pais5 ,pais6 ,pais7 ,pais8 ,pais9 ,pais10):
    list = pd.read_csv('list.csv')
    filtro = (list['location'] == pais1) | (list['location'] == pais2) | (list['location'] == pais2) | (
                list['location'] == pais3) | (list['location'] == pais4) | (list['location'] == pais5) | (
                         list['location'] == pais6) | (list['location'] == pais7) | (list['location'] == pais8) | (
                         list['location'] == pais9) | (list['location'] == pais10)
    listapaises = list[filtro]
    filtro2 = listapaises.columns.isin(['location', 'date','total_deaths'])
    selectedCols = listapaises.columns[filtro2]
    listapaises2 = listapaises[selectedCols]
    print(listapaises2)
    return listapaises2

def reproduccionRate(pais1, pais2 , pais3 , pais4 ,pais5 ,pais6 ,pais7 ,pais8 ,pais9 ,pais10):
    list = pd.read_csv('list.csv')
    filtro = (list['location'] == pais1) | (list['location'] == pais2) | (list['location'] == pais2) | (
                list['location'] == pais3) | (list['location'] == pais4) | (list['location'] == pais5) | (
                         list['location'] == pais6) | (list['location'] == pais7) | (list['location'] == pais8) | (
                         list['location'] == pais9) | (list['location'] == pais10)
    listapaises = list[filtro]
    filtro2 = listapaises.columns.isin(['location', 'date', 'reproduction_rate'])
    selectedCols = listapaises.columns[filtro2]
    listapaises2 = listapaises[selectedCols]
    print(listapaises2)
    return listapaises2



paisQuantitat("Albania", "Algeria", "Argentina", "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France", "Afghanistan")
mortsTotals("Albania", "Algeria", "Argentina", "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France", "Afghanistan")
reproduccionRate("Albania", "Algeria", "Argentina", "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France", "Afghanistan")