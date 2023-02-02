import pandas as pd

def paisQuantitat(pais1, pais2 , pais3 , pais4 ,pais5 ,pais6 ,pais7 ,pais8 ,pais9 ,pais10):
    #llegim el csv i el guardo a una variable
    list = pd.read_csv('list.csv')
    #Aplico un filtre per seleccionar els 10 paisos que volem
    filtro = (list['location'] == pais1) | (list['location'] == pais2) | (list['location'] == pais2) | (list['location'] == pais3) | (list['location'] == pais4) | (list['location'] == pais5) | (list['location'] == pais6) | (list['location'] == pais7) | (list['location'] == pais8) | (list['location'] == pais9) | (list['location'] == pais10)
    #Guardo el nou df amb els 10 paisos
    listapaises = list[filtro]
    #He fet un nou filtre per seleccionar nomes les 3 columnes que ens interessen
    filtro2 = listapaises.columns.isin(['location', 'date', 'total_cases'])
    selectedCols = listapaises.columns[filtro2]
    # Guardo el nou df amb les columnes
    listapaises2 = listapaises[selectedCols]
    #Com la data venia en un format dd-mm-aa, utilitzo aixo per poder agafar el mes
    separar = listapaises2.date.str.split(pat='-', expand=True)
    listapaises3 = pd.DataFrame(separar, columns=[1])
    listapaises4 = pd.DataFrame(listapaises2, columns=["location", "total_cases"])
    listaDefinitiva = pd.concat([listapaises4, listapaises3], axis=1)
    listaAgrupada = listaDefinitiva.rename(columns={1:'mes'})
    #Com hi havia 30 dades una per cada dia i nomes volia el total agrupo les dades per location i mes y ho sumo
    listaAgrupada2 = listaAgrupada.groupby(['location', 'mes']).sum()
    print(listaAgrupada2)
    return listaAgrupada2


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
    separar = listapaises2.date.str.split(pat='-', expand=True)
    listapaises3 = pd.DataFrame(separar, columns=[1])
    listapaises4 = pd.DataFrame(listapaises2, columns=["location", "total_deaths"])
    listaDefinitiva = pd.concat([listapaises4, listapaises3], axis=1)
    listaAgrupada = listaDefinitiva.rename(columns={1: 'mes'})
    listaAgrupada2 = listaAgrupada.groupby(['location', 'mes']).sum()
    print(listaAgrupada2)
    return listaAgrupada2


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
    separar = listapaises2.date.str.split(pat='-', expand=True)
    listapaises3 = pd.DataFrame(separar, columns=[1])
    listapaises4 = pd.DataFrame(listapaises2, columns=["location", "reproduction_rate"])
    listaDefinitiva = pd.concat([listapaises4, listapaises3], axis=1)
    listaAgrupada = listaDefinitiva.rename(columns={1: 'mes'})
    listaAgrupada2 = listaAgrupada.groupby(['location', 'mes']).sum()
    print(listaAgrupada2)
    return listaAgrupada2


paisQuantitat("Albania", "Algeria", "Argentina", "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France", "Afghanistan")
mortsTotals("Albania", "Algeria", "Argentina", "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France", "Afghanistan")
reproduccionRate("Albania", "Algeria", "Argentina", "Mexico", "Thailand", "Japan", "Singapore", "Spain", "France", "Afghanistan")
