# ex1

emails_internos = {}
emails_externos = {}

while True: #esse recebe os e-mails
    receber_email = input("cadastre seu e-mail: ")
    if "@fiap" in receber_email:

        save_email = emails_internos[receber_email] = emails_internos
        print(save_email)
    else:
        save_email = emails_externos[receber_email] = emails_externos
        print(save_email)

        #esse separa os emails
        email = receber_email
        username, dominio = email.split("@")
        print(username)
        print(dominio)

        #contagem de e-mails
    contagem_in = len(emails_internos)
    contagem_ex = len(emails_externos)

    print(f"e-mails internos: {contagem_in}" , f"emials externos: {contagem_ex}")