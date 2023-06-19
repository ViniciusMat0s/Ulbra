idade = float(input("Qual a sua idade? "))
herança_familiar = float(input("Você tem quantos parentes com cardiopatia? "))
sexo = input("Qual o seu sexo? [M] para masculino e [F] para feminino, digite com letra maiúscula. ")
percentual_gordura = float(input("Qual seu percentual de gordura? (Digite sem o sinal de porcentagem). "))
tabagismo = float(input("Quantos cigarros você fuma por dia? "))
sedentarismo = float(input("Você pratica quantos minutos de exercício na semana? "))
colesterol = float(input("Como está seu colesterol? "))
pressão_sis = float(input("Qual sua pressão arterial sistótica (em mmHg)? "))
pressão_dia = float(input("Qual sua pressão arterial diastólica (em mmHg)? "))

if idade >= 10 and idade <= 20:
    pts_idade = 1
elif idade >= 21 and idade <= 30:
    pts_idade = 2
elif idade >= 31 and idade <= 40:
    pts_idade = 3
elif idade >= 41 and idade <= 50:
    pts_idade = 4
elif idade >= 51 and idade <= 60:
    pts_idade = 6
elif idade > 60:
    pts_idade = 8
else:
    pts_idade = -1000
    print("VALOR DE IDADE INVÁLIDO.")

if (herança_familiar == 0) or (herança_familiar > -1 and herança_familiar < 1):
    pts_herança = 1
elif herança_familiar == 1:
    pts_herança = 2
elif herança_familiar == 2:
    pts_herança = 3
elif herança_familiar == 3 or herança_familiar == 4 or herança_familiar == 5: 
    pts_herança = 7
else:
    pts_herança = -1000
    print("VALOR DE CARDIOPATIA INVÁLIDO.")

if (sexo == "M" and percentual_gordura < 12) or (sexo == "F" and percentual_gordura < 16):
    pts_percentual = 0
elif (sexo == "M" and percentual_gordura >= 12 and percentual_gordura <= 15.99) or (sexo == "F" and percentual_gordura >= 16 and percentual_gordura <= 19.99):
    pts_percentual = 1
elif (sexo == "M" and percentual_gordura >= 16 and percentual_gordura <= 19.99) or (sexo == "F" and percentual_gordura >= 20 and percentual_gordura <= 24.99):
    pts_percentual = 2
elif (sexo == "M" and percentual_gordura >= 20 and percentual_gordura <= 21.99) or (sexo == "F" and percentual_gordura >= 25 and percentual_gordura <= 32.99):
    pts_percentual = 3
elif (sexo == "M" and percentual_gordura >= 22 and percentual_gordura <= 29.99) or (sexo == "F" and percentual_gordura >= 33 and percentual_gordura <= 39.99):
    pts_percentual = 5
elif (sexo == "M" and percentual_gordura > 30) or (sexo == "F" and percentual_gordura > 40):
    pts_percentual = 7
else:
    pts_percentual = -1000
    print("VALOR DE PERCENTUAL DE GORDURA INVÁLIDO.")

if tabagismo == 0:
    pts_tabagismo = 0
elif tabagismo > 0 and tabagismo <= 10:
    pts_tabagismo = 1
elif tabagismo > 10 and tabagismo <= 20:
    pts_tabagismo = 2
elif tabagismo > 20 and tabagismo <= 30:
    pts_tabagismo = 4
elif tabagismo > 30 and tabagismo <= 40:
    pts_tabagismo = 6
elif tabagismo > 40:
    pts_tabagismo = 10
else:
    pts_tabagismo = -1000
    print("VALOR DE CIGARROS INVÁLIDO.")

if sedentarismo > 240:
    pts_sedentarismo = 0
elif sedentarismo >= 120 and sedentarismo <= 240:
    pts_sedentarismo = 1
elif sedentarismo >= 80 and sedentarismo <= 119:
    pts_sedentarismo = 2
elif sedentarismo >= 60 and sedentarismo <= 79:
    pts_sedentarismo = 3
elif sedentarismo >= 31 and sedentarismo <= 59:
    pts_sedentarismo = 6
elif sedentarismo < 30:
    pts_sedentarismo = 8
else:
    pts_sedentarismo = -1000
    print("VALOR DE MINUTOS DE EXERCÍCIO INVÁLIDO.")

if colesterol < 180:
    pts_colesterol = 1
elif colesterol > 180 and colesterol <= 205:
    pts_colesterol = 2
elif colesterol > 205 and colesterol <= 230:
    pts_colesterol = 3
elif colesterol > 230 and colesterol <= 255:
    pts_colesterol = 4
elif colesterol > 255 and colesterol <= 280:
    pts_colesterol = 5
elif colesterol > 280:
    pts_colesterol = 7
else:
    pts_colesterol = -1000
    print("VALOR DE COLESTEROL INVÁLIDO.")

if pressão_sis < 120:
    pts_pressãosis = 1
elif pressão_sis >= 120 and pressão_sis < 140:
    pts_pressãosis = 2
elif pressão_sis >= 140 and pressão_sis < 160:
    pts_pressãosis = 3
elif pressão_sis >= 160 and pressão_sis < 180:
    pts_pressãosis = 4
elif pressão_sis >= 180 and pressão_sis < 200:
    pts_pressãosis = 6
elif pressão_sis > 200:
    pts_pressãosis = 8
else:
    pts_pressãosis = -1000
    print("VALOR DE PRESSÃO ARTERIAL SISTÓLICA INVÁLIDO.")

if pressão_dia < 70:
    pts_pressãodia = 1
elif pressão_dia >= 70 and pressão_dia <= 76:
    pts_pressãodia = 2
elif pressão_dia >= 77 and pressão_dia <= 82:
    pts_pressãodia = 3
elif pressão_dia >= 83 and pressão_dia <= 93:
    pts_pressãodia = 4
elif pressão_dia >= 94 and pressão_dia <= 105:
    pts_pressãodia = 6
elif pressão_dia >= 106:
    pts_pressãodia = 8
else:
    pts_pressãodia = -1000
    print("VALOR DE PRESSÃO ARTERIAL DIASTÓLICA INVÁLIDO.")

#RISCO CARDIOVASCULAR

total = pts_idade + pts_herança + pts_percentual + pts_tabagismo + pts_sedentarismo + pts_colesterol + pts_pressãosis + pts_pressãodia

if total >= 5 and total <= 11:
    print(f"PONTUAÇÃO TOTAL: {total}\n\nIdade: {pts_idade}\nCardiopatia: {pts_herança}\nPercentual de gordura: {pts_percentual}\nCigarros/dia: {pts_tabagismo}\nTempo de exercício: {pts_sedentarismo}\nColesterol: {pts_colesterol}\nPressão Arterial Sistólica: {pts_pressãosis}\nPressão Arterial Diastólica: {pts_pressãodia}\n\nRisco bem abaixo da média.")
elif total >= 12 and total <= 17:
    print(f"PONTUAÇÃO TOTAL: {total}\n\nIdade: {pts_idade}\nCardiopatia: {pts_herança}\nPercentual de gordura: {pts_percentual}\nCigarros/dia: {pts_tabagismo}\nTempo de exercício: {pts_sedentarismo}\nColesterol: {pts_colesterol}\nPressão Arterial Sistólica: {pts_pressãosis}\nPressão Arterial Diastólica: {pts_pressãodia}\n\nRisco abaixo da média.")
elif total >= 18 and total <= 24:
    print(f"PONTUAÇÃO TOTAL: {total}\n\nIdade: {pts_idade}\nCardiopatia: {pts_herança}\nPercentual de gordura: {pts_percentual}\nCigarros/dia: {pts_tabagismo}\nTempo de exercício: {pts_sedentarismo}\nColesterol: {pts_colesterol}\nPressão Arterial Sistólica: {pts_pressãosis}\nPressão Arterial Diastólica: {pts_pressãodia}\n\nRisco médio habitual.")
elif total >= 25 and total <= 31:
    print(f"PONTUAÇÃO TOTAL: {total}\n\nIdade: {pts_idade}\nCardiopatia: {pts_herança}\nPercentual de gordura: {pts_percentual}\nCigarros/dia: {pts_tabagismo}\nTempo de exercício: {pts_sedentarismo}\nColesterol: {pts_colesterol}\nPressão Arterial Sistólica: {pts_pressãosis}\nPressão Arterial Diastólica: {pts_pressãodia}\n\nRisco moderado.")
elif total >= 32 and total <= 40:
    print(f"PONTUAÇÃO TOTAL: {total}\n\nIdade: {pts_idade}\nCardiopatia: {pts_herança}\nPercentual de gordura: {pts_percentual}\nCigarros/dia: {pts_tabagismo}\nTempo de exercício: {pts_sedentarismo}\nColesterol: {pts_colesterol}\nPressão Arterial Sistólica: {pts_pressãosis}\nPressão Arterial Diastólica: {pts_pressãodia}\n\nRisco perigoso.")
elif total >= 41 and total <= 63:
    print(f"PONTUAÇÃO TOTAL: {total}\n\nIdade: {pts_idade}\nCardiopatia: {pts_herança}\nPercentual de gordura: {pts_percentual}\nCigarros/dia: {pts_tabagismo}\nTempo de exercício: {pts_sedentarismo}\nColesterol: {pts_colesterol}\nPressão Arterial Sistólica: {pts_pressãosis}\nPressão Arterial Diastólica: {pts_pressãodia}\n\nPerigo urgente - Procure seu médico.")
else:
    print("Você inseriu algum valor errado, operação finalizada.")