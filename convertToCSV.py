import json
import csv


with open("response1.json", "r") as inputfile:
    datas = json.load(inputfile)
    
# Abrir um arquivo CSV para escrita
with open('response1.csv', 'w', newline='', encoding='utf-8') as file:
    # Criar um objeto escritor CSV
    csv_writer = csv.writer(file)
    print('criar o arquivo')
    
    # Escrever a linha de cabeçalho
    header = ['prompt', 'completion']
    csv_writer.writerow(header)
    print('criar o header')
    
    # Escrever as linhas de dados
    for data in datas['situacoes']:
        row = [data['prompt'], data['completion']]
        csv_writer.writerow(row)