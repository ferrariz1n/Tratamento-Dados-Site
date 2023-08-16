#bibliotecas
import pandas as pd

data=pd.read_json("dados_compras.json")

    
def verificar_nulos():
    null_counts = data.isnull().sum()
    for column, count in null_counts.items():
    
        print(f"A coluna '{column}' possui {count} valores nulos.")

def contar_id():
    count_id= data['Item ID'].count()
    
    print(count_id)

def media_valor():
    sum_values = data['Valor'].sum()
    count_values = data['Valor'].count()
    media= sum_values/count_values

    print(media)
    
def valor_maximo():
    max_value = data['Valor'].max()
    
    print(max_value)

def valor_minimo():
    min_value = data['Valor'].min()
    
    print(min_value)
    return min_value

def produto_mais_caro():
    max_value = data['Valor'].max()
    expensive_product = data[data['Valor'] == max_value].iloc[0]
    print(expensive_product['Nome do Item'])

def distribuicao_genero():
    count_masc = (data['Sexo'] == 'Masculino').sum()
    count_fem = (data['Sexo'] == 'Feminino').sum()
    count_nda = (data['Sexo'] == 'Outro / Não Divulgado').sum()
    print(f'NDA: {count_nda}')
    print(f'Masculino: {count_masc}')
    print(f'Feminino: {count_fem}')

def gastos_por_genero():
    expenses_masc = data[data['Sexo'] == 'Masculino']['Valor'].sum()
    expenses_fem = data[data['Sexo'] == 'Feminino']['Valor'].sum()
    expenses_nda = data[data['Sexo'] == 'Outro / Não Divulgado']['Valor'].sum()
    print(expenses_masc)
    print(expenses_fem)
    print(expenses_nda)
