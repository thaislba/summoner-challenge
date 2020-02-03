import pandas as pd
from pandas import DataFrame
import sys
import numpy as np

class DataPrep:
    
    def removeColumn(df, column):
        try:
            return df.drop([column], axis=1)
        except KeyError as e:
            print('O parametro esperado é o nome da coluna existente no dataframe e não o índice.')
            print(repr(e))
            sys.exit(1)

    def mergeDataframes(df1, df2, column):
        return pd.merge(df1, df2, on=column)
    
    def mergeDataframesOuter(df1, df2, column):
        return pd.merge(df1, df2, on='NAME', how='outer')


def getData(url):
   return pd.read_csv(url, index_col=0)

def calculateDPS(df):
    try:
        df['DPS'] = df['ATTACK_SPEED'] * df['ATTACK_DAMAGE']      
        return df
    except Exception as e:
        print("[!] Erro desconhecido!")
        print(repr(e))
        sys.exit(1)

def main():
    dataset_1 = getData('https://raw.githubusercontent.com/Datenworks/developer-code-challenge/master/summoner_challenge/files/dataset_1.csv')
    dataset_2 = getData('https://raw.githubusercontent.com/Datenworks/developer-code-challenge/master/summoner_challenge/files/dataset_2.csv')
    print(dataset_1, '\n \n', dataset_2)    

    dataset_1 = DataPrep.removeColumn(dataset_1, 'ARMOR')
    dataset_2 = DataPrep.removeColumn(dataset_2, 'MAGIC_RESIST')

    dffinal = DataPrep.mergeDataframesOuter(dataset_1, dataset_2, 'NAME')
    dffinal = dffinal.replace(np.nan, 0)

    dffinal = calculateDPS(dffinal)
    print(dffinal.sort_values(by='DPS', ascending=False))

    sys.exit(0)

if __name__ == '__main__':
    main()
