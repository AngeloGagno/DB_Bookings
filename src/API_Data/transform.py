import pandas as pd 

def transform_str_date(dataframe):
    return pd.to_datetime(dataframe,dayfirst=True)

def reorder_df(dataframe):
    return dataframe[['Localizador','Data de check-in','Data de check-out','Nome acomodação','Estado','ADR']]

def Avg_Adr(dataframe):
    dataframe['ADR'] = (dataframe['Pago'] - dataframe['Extras com impostos']) / dataframe['noites']
    return dataframe

def transform_df(dataframe):
    dataframe = Avg_Adr(dataframe)
    dataframe['Data de check-in'] = transform_str_date(dataframe['Data de check-in'])
    dataframe['Data de check-out'] = transform_str_date(dataframe['Data de check-out'])
    dataframe_cleaned = reorder_df(dataframe)
    return dataframe_cleaned