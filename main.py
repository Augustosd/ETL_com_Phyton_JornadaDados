#Análise exploratória dos dados
import pandas as pd

from ydata_profiling import ProfileReport

#Faz uma análise da panilha e monta automaticamente um report .html
df = pd.read_csv('data.csv')
profile = ProfileReport(df, title='Profile Report')
profile.to_file('output.html')

#Instalar Pandera ou Pydentic para fazer contrato
#Pandera grande volume de dados -> validação do dataframe
#Pydentic validação de pequenos volumes de dados -> Validação linha a linha

