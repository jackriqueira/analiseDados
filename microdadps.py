import pandas as pd
base_path = 'C:/Users/Doguinhos/ambiente_virtual/projetos/microdados_enem/DADOS/'
microdadosEnem = pd.read_csv(base_path + 'MICRODADOS_ENEM_2018.csv', sep=";", encoding='ISO-8859-1')


microdadosEnem.columns.values
novasColunasSelecionadas = ['NU_INCRICAO','NU_NOTA_MT','NU_NOTA_REDACAO', 'Q001', 'Q001']
microdadosEnemSelecionado = microdadosEnem.filter(items=novasColunasSelecionadas)
microdadosEnemSelecionado.head()
microdadosEnemSelecionado.dropna()
