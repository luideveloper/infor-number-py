import requests
import time

def main():
    print("\x1b[2J\x1b[1;1H")
    print("Digite a abaixo o número que deseja obter informações.\n")
    number = input('> Número: ')
    inforNumber(number)

def inforNumber(x): 
    # Cada api key tem um limite de requesições.
    # Cadastre uma conta em https://veriphone.io/ para obter um novo token quando este expirar.
    api_key = "C6842096CF2A49CCB676933E644E4966" 
    request = requests.get(' https://api.veriphone.io/v2/verify?phone=+{}&key={}'.format(x,api_key))
    address_data = request.json()

    if address_data['status'] == "success":
        print('\n✅ Informmações:\n') 

        print('• Número: {}'.format(address_data['international_number']))

        if address_data['phone_valid'] == True:
            print("• Número válido: Verdadeiro")
        elif address_data['phone_valid'] == False:
            print("• Número válido: Falso")
        else:
           print ("\n❌ ocorreu um erro de execução do programa")

        print('• Tipo do número: {}'.format(address_data['phone_type']))
        print('• Estado: {}'.format(address_data['phone_region']))
        print('• País: {}'.format(address_data['country']))
        print('• DDD internacional: +{}'.format(address_data['country_prefix']))

        if address_data['carrier'] == "":
            print("• Operadora: Não identificada")
        elif address_data['phone_valid'] == False:
            print('• Operadora: {}'.format(address_data['carrier']))
        else:
           print ("\n❌ ocorreu um erro de execução do programa")
        
        time.sleep(6)
        loop()

    else:
        print ("\n❌ ocorreu um erro de execução do programa")

def loop():
    print("\x1b[2J\x1b[1;1H")
    print("Escolha uma opção:")
    print("\n[ 1 ] Executar novamente o programa")
    print("[ 2 ] Sair do programa")
    option = int(input("\nOpção: "))

    if option == 1:
        print("\x1b[2J\x1b[1;1H")
        main()
    elif option == 2:
        print("\x1b[2J\x1b[1;1H")
        exit()
    else:
        print("\x1b[2J\x1b[1;1H")
        print("Opção inválida")
