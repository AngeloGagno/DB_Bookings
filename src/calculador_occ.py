from datetime import timedelta
from API_Data.get import read_df
from API_Data.transform import transform_df
import pandas as pd

def calcular_ocupacao():
    df = read_df()
    dados = transform_df(df)
    lista = []
    for index in dados.index:
        localizador = dados.loc[index,'Localizador']
        checkin = dados.loc[index,'Data de check-in']
        checkout = dados.loc[index,'Data de check-out']
        nome_acomodacao = dados.loc[index,'Nome acomodação']
        status = dados.loc[index,'Estado']
        adr = dados.loc[index,'ADR']
        while checkin < checkout:
            checkin += timedelta(days=1)
            lista += [(localizador,checkin,nome_acomodacao,status,adr)]
    return pd.DataFrame(data= lista,columns= ['Localizador','Dia','Acomodacao','Status','ADR'], index = 
                        [i for i in range(0,len(lista))])

if __name__ == '__main__':
    df = calcular_ocupacao()
    df.to_excel('OCC_teste.xlsx')