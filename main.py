
import os;

user = {
    "nome": input("Nome: "),
    "idade": input("Idade: ")
}

bd = open("bd-chat.txt", "a", encoding="utf-8")
bd.write(user["nome"]);
bd.write(user["idade"] + "\n");

mensagens = [];


while True:
    os.system("cls");

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'] + "-" + m['texto'])
    print("-----------------------------------------------------------------------------------")

    print("'fim' encerra a sessão")
    texto = str(input("Digite sua mensagem: "))

    texto = str.lower(texto);

    if texto == "fim":
        break

    mensagens.append({
        "nome": user["nome"],
        "texto": texto
    }
    )
    bd.write(user["nome"] + ":" + texto + "\n");

