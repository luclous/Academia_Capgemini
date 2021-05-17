import math
from datetime import datetime
def exibir_menu():
    print('''Escolha uma opção:

    1. Cadastrar um anúncio
    2. Listar anúncios cadastrados
    3. Procurar dados por nome de cliente
    ''')

def cadastrar(anuncios):
    identificador = input('Nome do anúncio:  ')
    nome = input('Cliente:  ')
    inicio = str(input('Insira a data de início neste formato dd/mm/aaaa:  '))
    fim = str(input('Insira a data de término neste formato dd/mm/aaaa: '))
    investimento = float(input('Investimento por dia: '))
    anuncios.append((identificador, nome, inicio, fim, investimento))

    inicio = datetime.strptime(inicio, "%d/%m/%Y").date()
    fim = datetime.strptime(fim, "%d/%m/%Y").date()
    data_inicio_dias = inicio.toordinal()
    data_termino_dias = fim.toordinal()
    dias = data_termino_dias - data_inicio_dias
    dias = dias + 1

    visualizacoes_iniciais = investimento * dias
    cliques = math.floor((visualizacoes_iniciais * 0.12))
    compartilhamentos = math.floor((cliques * 0.15))
    visualizacoes_finais = visualizacoes_iniciais + compartilhamentos * 40

def listar(anuncios):
    for anuncio in anuncios:
        identificador, nome, inicio, fim, investimento = anuncio
        print(f'Cliente: {nome}, data de início: {inicio}, data de término: {fim}, investimento: {investimento}, nome do anúncio: {identificador}')

def buscar(anuncios):
    identificador_desejado = input('Nome do cliente:  ')
    for anuncio in anuncios:
        identificador, nome, inicio, fim, investimento = anuncio
        if nome == identificador_desejado:
            print(f'Cliente: {nome}, data de início: {inicio}, data de término: {fim}, investimento: {investimento}, nome do anúncio: {identificador}')
            break
    else:
        print(f'Cliente {identificador_desejado} não encontrado!')

def main():
    anuncios = []

    while True:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(anuncios)
        elif opcao == 2:
            listar(anuncios)
        elif opcao == 3:
            buscar(anuncios)
        else:
            print('Opção inválida')

main()
