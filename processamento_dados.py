
def proporcao_genero(dados):
    total = len(dados)
    mulheres = 0
    
    for linha in dados:
        genero = linha['Gender'].strip().lower()
        if genero == 'female':
            mulheres += 1
            
    return (mulheres / total) * 100 if total > 0 else 0

def media_idade(dados):
    idades = [int(linha['Age']) for linha in dados if linha['Age'].strip().isdigit()]
    return sum(idades) / len(idades) if idades else 0

def media_renda(dados):
    rendas = [int(linha['MonthlyIncome']) for linha in dados if linha['MonthlyIncome'].strip().isdigit()]
    return sum(rendas) / len(rendas) if rendas else 0
    