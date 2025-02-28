
import os;

user = {
    "nome": input("Nome: "),
    "data": input("Data ex: 10/09/1932: ")
}

bd = open("bd-chat.txt", "a", encoding="utf-8")
bd.write("\n" + user["nome"]);
bd.write(user["data"] + "\n");

mensagens = [];


#mostrar as mensagens já registradas
def pergunta_registros():
    print("-----------------------------------------------------------------------------------")
    ver_registros = str(input("Ver registros anteriores?[yes][no] "));
    if ver_registros == "yes":
        os.system("cls");
        with open("bd-chat.txt", "r", encoding="utf-8") as bd:
            for line in bd:
                print(line.strip())

    while str.lower(ver_registros) != "yes" or "no":
        print("-----------------------------------------------------------------------------------")
        ver_registros = str.lower(str(input("Ver registros anteriores?[yes][no] ")));
        if ver_registros == "yes":
            os.system("cls");
            with open("bd-chat.txt", "r", encoding="utf-8") as bd:
                for line in bd:
                    print(line.strip())

        if ver_registros =="no":
            break




pergunta_registros();





while True: 
    os.system("cls");

    #mostrar a mensagem enviada antes de mandar outra
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'] + ": " + m['texto'])
    print("-----------------------------------------------------------------------------------")

    print("Para encerrar a sessão digite 'fim' ")
    print("Sua mensagem deverá ficar registrada, que seja uma boa mensagem.")
    texto = str(input("Digite sua mensagem: "))

    texto = str.lower(texto);

    if texto == "fim":
        break

    mensagens.append({
        "nome": user["nome"],
        "texto": texto
    }
    )
    bd.write(user["nome"] + ": " + texto + "\n");

