import csv

from Aula_09_Mini_crm_v2.Data.control import DATA_DIR, read_leads
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

    print(f"## | {"Nome":<10} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["e-mail"]:<10} ")

def search_leads():
    print("Buscando...")
    query = input("Buscar por: ").strip()
    if not query:
        print("but it refused")
        return

    #Com a query digitada (busca)... Preciso enviar para o control
    # o control irá comparar a query com os dados do leaads.json
    # e irá retornar os resultados da busca
    found_leads = control.read_leads_search(query)

    print(f"## | {"Nome":<10} | E-mail")
    for i, lead in enumerate(found_leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["e-mail"]:<10} ")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possivel exportar o CSV")
    else:
        print(f"Exportado para {path_csv}")


def main():
    while (True):
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] Lista leads")
        print("[3] Buscar")
        print("[4] Exportar CSV")
        print("[0] Sair do programa\n")

        opt = input("Escolha uma opção\n")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("saindo do programa")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    main()
