equipe1 = input("Digite o nome da sua equipe: ")
equipe2 = input("Digite o nome da outra equipe: ")

resolvidos1 = 0
resolvidos2 = 0
erros_enc1 = 0
erros_enc2 = 0
erros_cor1 = 0
erros_cor2 = 0
horario1 = 0
horario2 = 0
pontuacao1 = 0
pontuacao2 = 0

resolvidos = int(input(f"Quantos algoritmos foram resolvidos por sua equipe [{equipe1}]? "))
if resolvidos + 1:
    resolvidos1 += resolvidos
    pontuacao1 = resolvidos1 * 10
    print(f"Foram resolvidos {resolvidos1} algorítmos | Pontuação: {pontuacao1} ")
resolvidos = int(input(f"Quantos algoritmos foram resolvidos pela equipe adversária [{equipe2}?] "))
if resolvidos + 1:
    resolvidos2 += resolvidos
    pontuacao2 = resolvidos2 * 10
    print(f"Foram resolvidos {resolvidos2} algorítmos | Pontuação: {pontuacao2} ")

erros_enc = int(input(f"Quantos erros foram encontrados pela sua equipe [{equipe2}]? "))
if erros_enc1 + 1:
    erros_enc += erros_enc1
    pontuacao2 = pontuacao2 - (erros_enc * 5)
    print(f"Foram encontrados {erros_enc} erros na equipe adversária | Pontuação adversária: {pontuacao2} ")
erros_enc = int(input(f"Quantos erros foram encontrados pela equipe adversária? [{equipe1}]? "))
if erros_enc + 1:
    erros_enc += erros_enc2
    pontuacao1 = pontuacao1 - (erros_enc * 5)
    print(f"A equipe adversária encontrou {erros_enc} erros na sua equipe | Sua Pontuação: {pontuacao1}")

erros_cor = int(input(f"Quantos erros foram corrigidos pela sua equipe [{equipe1}]? "))
if erros_cor1 + 1:
    erros_cor += erros_cor1
    pontuacao1 = pontuacao1 + erros_cor * 5
    print(f"Foram corrigidos {erros_cor} algorítmos pela sua equipe | Pontuação: {pontuacao1}")
erros_cor = int(input(f"Quantos erros foram corrigidos pela equipe adversária [{equipe2}]? "))
if erros_cor2 + 1:
    erros_cor += erros_cor2
    pontuacao2 = pontuacao2 + erros_cor * 5
    print(f"Foram corrigidos {erros_cor} algorítmos pela equipe adversária | Pontuação: {pontuacao2}")

horario1 = int(input(f"Sua equipe [{equipe1}] atrasou a entrega dos algorítmos em quantos minutos? [Digite 0 para negar atraso] "))
pontuacao1 = pontuacao1 - horario1
print(f"Sua equipe atrasou {horario1} minutos, então, perdeu {horario1} pontos | Pontuação: {pontuacao1}")

horario2 = int(input(f"A equipe adversária [{equipe2}] atrasou a entrega dos algorítmos em quantos minutos? [Digite 0 para negar atraso] "))
pontuacao2 = pontuacao2 - horario2
print(f"Sua equipe atrasou {horario2} minutos, então, perdeu {horario2} pontos | Pontuação: {pontuacao2}")

print(f"\n===============\nPONTUAÇÃO FINAL\n---------------\n{equipe1}: {pontuacao1}\n---------------\n{equipe2}: {pontuacao2}\n===============\n")
if pontuacao1 > pontuacao2:
    print(f"A equipe [{equipe1}] é a vencedora!\n")
elif pontuacao2 > pontuacao1:
    print(f"A equipe [{equipe2}] é a vencedora!\n")