
idade = int(input('Digite a idade do aluno: '))
vagas = int(input('Digite o número de vagas disponíveis: '))
valor_base = float(input('Digite o valor base do ingresso: '))
cupom = input('Digite o cupom de desconto (ou pressione Enter para continuar): ')

def validar_inscricao(idade_aluno, vagas_disponiveis):
    # Verifica a idade minima
    if idade_aluno < 16:
        return "Inscrição Negada: Idade mínima é 16 anos."
    
    if vagas_disponiveis <= 0:
        return "Inscrição Negada: Evento lotado."
    
    return "Inscrição Permitida."

def calcular_valor_ingresso(valor_base, cupom):
    if cupom == "ALUNO10":
        valor_final = valor_base * 0.9 # Aplica o desconto
    else:
        valor_final = valor_base
        
    return valor_final

def realizar_checkout(idade, vagas, valor_base, cupom):
    status = validar_inscricao(idade, vagas)
    if status == "Inscrição Permitida.":
        valor_pago = calcular_valor_ingresso(valor_base, cupom)
        vagas = vagas - 1
        return {
            "sucesso": True,
            "mensagem": "Inscrição realizada!",
            "valor_pago": valor_pago,
            "vagas_restantes": vagas
        }
    else:
        return {
            "sucesso": False,
            "mensagem": status,
            "valor_pago": 0,
            "vagas_restantes": vagas
        }

print(realizar_checkout(idade, vagas, valor_base, cupom))