import getpass

while True:
 print("**********************************************")
 print("********* Banco - Caixa Eletrônico ***********")
 print("**********************************************")
 account_typed = input("Digite sua conta: ")
 password_typed = getpass.getpass("Digite sua senha: ")
 print(account_typed)
 print(password_typed)


account_list = {
    '0001-02' : {
        'password': '123456',
        'name': 'Fulano Freire',
        'value': 1000
    },
'0002-02' : {
        'password': '123456',
        'name': 'Fulano Silva',
        'value': 2050
    }
}

if account_typed in account_list and password_typed == account_list[account_typed]['password']:
    print('Conta Válida')
    print("**********************************************")
    print("********* Banco - Caixa Eletrônico ***********")
    print("**********************************************")
    print("1 - Saldo")
    option_typed = input('Escolha uma das opções acima:')
    if option_typed == '1':
        #print('Seu saldo é: ' + account_list[account_typed]['value'])
        print('Seu saldo é %s' % account_list[account_typed]['value'])

else:
    print('conta Inválida')
