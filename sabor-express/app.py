import os 

restaurants = [
    {
        'nome': 'China In Box', 
        'categoria': 'Chinesa', 
        'ativo': False
     },
    {
        'nome': 'Pizza Suprema' ,
        'categoria': 'Italiana',
        'ativo': True
     }] # Dicionário de restaurantes já cadastrados. 

def showMenu():
    print("""
      
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
        
    """) # https://fsymbols.com/

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def returnMenu():
    input('\nDigite uma tecla para voltar ao menu. ')
    main()

def writeSubtitle(string):
    os.system('cls')
    line = '=' * (len(string))
    print(line)
    print(f'{string}')
    print(line)

def choiceOption():
    try:
        option = int(input('Escolha uma opção: '))
        print(f'\nOpção escolhida: {option}\n')

        if option == 1:
            newRestaurant()
        elif option == 2:
            printRestaurants()
        elif option == 3:
            setState()
        elif option == 4:
            exitApp()
        else:
            invalidOption()
    except:
        invalidOption()

def newRestaurant():
    writeSubtitle('Cadastro de novo restaurante...')
    name = input('Digite o nome do restaurante: ')
    category = input(f'Digite o nome da categoria do restaurante {name}: ')
    newRestaurant = {'nome': name, 'categoria': category, 'ativo': False}
    restaurants.append(newRestaurant)
    print(f'O restaurante: {name} foi cadastrado com sucesso!')
    returnMenu()

def setState():
    writeSubtitle('Alternando estado do restaurante...')

    name = input('Digite o nome do restaurante: ')
    find = False

    for restaurant in restaurants:
        if name == restaurant['nome']:
            find = not find
            restaurant['ativo'] = not restaurant['ativo']
            message = 'Restaurante ativado com sucesso!' if restaurant['ativo'] else 'Restaurante desativado com sucesso!'
            print(message)
    if not find: 
        print('Restaurante não encontrado.')

    returnMenu()

def printRestaurants():
    writeSubtitle('Listando restaurantes...')
    print(f'{'Nome'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurant in restaurants:
        text = f'- {restaurant['nome'].ljust(20)} | {restaurant['categoria'].ljust(20)} | {'Ativado' if restaurant['ativo'] else 'Desativado'}'
        print(text)

    returnMenu()

def exitApp():
    os.system('cls') # Função build-in do Python que limpa o histórico do terminal
    writeSubtitle('Encerrando o app...')

def invalidOption():
    print('Opção inválida!')
    returnMenu()

def main():
    os.system('cls')
    showMenu()
    choiceOption()

if __name__ == '__main__':
    main()
