
def gerar_relatorio_texto(proporcao_mulheres, media_idade, media_renda, arquivo_saida):
    with open(arquivo_saida, 'w') as arquivo:
        arquivo.write("Relatório de diversidade\n")
        arquivo.write(f"Proporção de mulheres: {proporcao_mulheres:.2f}%\n")
        arquivo.write(f"Média idade: {media_idade:.2f} anos\n")
        arquivo.write(f"Média renda: {media_renda:.2f} USD\n")
