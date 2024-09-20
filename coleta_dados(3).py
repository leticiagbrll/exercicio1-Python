
import csv

def dados_diversidade(arquivo_csv):
  with open(arquivo_csv, mode='r', encoding='utf-8-sig') as arquivo:
    reader = csv.DictReader(arquivo)
    dados = [row for row in reader]
    return dados
  