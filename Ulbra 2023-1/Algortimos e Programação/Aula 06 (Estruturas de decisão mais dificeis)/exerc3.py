3# O departamento que controla o índice de poluição do meio ambiente mantém 3 grupos de indústrias que são altamente poluentes do meio ambiente. O índice de poluição aceitável varia de 0.05 até 0.25. Se o índice sobe para 0.3 as indústrias do primeiro grupo são intimadas a suspenderem suas atividades, se o índice cresce para 0.4 as do primeiro e segundo grupo são intimadas a suspenderem suas atividades e se o índice atingir 0.5 todos os 3 grupos devem ser notificados a paralisarem suas atividades. Faça um programa que lê o índice de poluição medido e emite a notificação adequada aos diferentes grupos de empresas.
poluicao = float(input("Digite o índice de poluição: "))
if poluicao >= 0.05 and poluicao <= 0.25:
    print("Índice de poluição aceitável.")
elif poluicao >= 0.26 and poluicao <= 0.39:
    print("As indústrias do primeiro grupo serão intimadas e deverão suspender suas atividades.")
elif poluicao >= 0.40 and poluicao <= 0.49:
    print("As indústrias do primeiro e segundo grupo serão intimadas e deverão suspender suas atividades.")
elif poluicao >= 0.50:
    print("As indústrias de todos os grupos serão notificadas a paralisarem suas atividades.")
else:
    print("Inválido.")