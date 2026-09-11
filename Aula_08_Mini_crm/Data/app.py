from model import model_lead
import control

def add_lead():
    nome = input("Nome: ")
    email = input("Email: ")
    status = input("Status do fluxo de vendas: ")

    #validar os dados (Fazer quando possivel... é cheio de if essa merda)
    # agora, preciso modelar os dados
    #para isso, vamos usar o modelo.py
    #preciso modelar os dados como um dict
    print(model_lead(nome, email, status))

    #mandar para o .json
    #usar o control para enviar o dict pelo lead
    control.create_lead(model_lead(nome, email, status))

    print("lead adicionado com sucesso (pela func)")

def list_leads():
    leads = control.read_leads()
    print(leads)


def main():
    while (True):
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] Lista leads")
        print("[0] Sair do programa\n")

        opt = input("Escolha uma opção\n")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("saindo do programa")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    main()
