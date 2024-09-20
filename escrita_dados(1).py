
import csv

def gerar_relatorio_csv(proporcao_mulheres, media_idade, media_renda, arquivo_saida):
 with open(arquivo_saida, mode='w', newline='') as arquivo:
     writer = csv.writer(arquivo)
     writer.writerow(['Métrica', 'Valor'])
     writer.writerow(['Proporção de mulheres', f'{proporcao_mulheres:.2f}%'])
     writer.writerow(['Média idade', f'{media_idade:.2f} anos'])
     writer.writerow(['Média renda', f'{media_renda:.2f} USD'])
