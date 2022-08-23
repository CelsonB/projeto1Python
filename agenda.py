AGENDA={

}
AGENDA['Guilherme'] = {
    'telefone':'9942-2636',
    'email':'guilherme@solyd.com.br',
    'endereço':'ernani batista rosas',

}
AGENDA['Maria'] = {
    'telefone':'9942-2636',
    'email':'guilherme@solyd.com.br',
    'endereço':'ernani batista rosas',

}



def mostrar_contatos(contato):
    print('-------------mostrar contatos---------')
    try:
        for item in contato:
            buscar_contato(item,contato)
    except ValueError as error:
        print('contato invalido')

def buscar_contato(contato, agenda):
    try:
        print("Nome:", contato)
        print("Telefone:", agenda[contato]['telefone'])
        print("Email:", agenda[contato]['email'])
        print("Endereço:", agenda[contato]['endereço'])
        print('-----------------------------------')
    except ValueError as error:
        print('contato invalido')

def excluir_contato(contato):
    try:
        for item in AGENDA:
            if(contato==item):
                AGENDA.pop(item)
                return
        print('contato inexistente')
    except ValueError as error:
        print('contato invalido')

def editar_contato(nome,campo,alt):
    try:
        AGENDA[nome][campo]=alt
    except ValueError as error:
        print('algum campo é invalido')

def adicionar_contato(nome,telefone,email,endereço):
    try:
        AGENDA[nome]={
            'telefone':telefone,
            'email':email,
            'endereço':endereço,
    }
    except ValueError as error:
        print('algum campo é invalido')
    print("contato {} adicionado com sucesso".format(nome))
def imprimir_menu():
    op=1;
    while(op!='0'):
        print('1 - mostrar todos os contatos')
        print('2 - buscar contato')
        print('3 - incluir contato')
        print('4 - editar contato')
        print('5 - excluir contato')
        print('0 - Sair do programa')
        op = input('Escolha uma opção: ')
        if op == '1':
            mostrar_contatos(AGENDA)
        elif op == '2':
            buscar_contato(input('digite quem deseja procurar: '),AGENDA)
        elif op == '3':
            adicionar_contato(
            input('digite o nome: '),
            input('digite o telefone: '),
            input('digite o email: '),
            input('digite o telefone: '))
        elif op == '4':
            editar_contato(input('digite o nome: '),input('digite a alteração: '))
        elif op == '5':
            excluir_contato(input('digite o contato que deseja exluir: '))

imprimir_menu()
#mostrar_contatos(AGENDA)
#buscar_contato('Guilherme',AGENDA)
#excluir_contato('Guilherme')
#mostrar_contatos(AGENDA)
#editar_contato('Guilherme','telefone','999')
#adicionar_contato('Celson','99991111','celson@alunos.utpr.udbr','ernani 2 ')
#mostrar_contatos(AGENDA