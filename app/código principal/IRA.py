Disciplinas = [] # Disciplinas cursadas
DisciT = [] # Disciplinas trancadas

Media = [] # Média das disciplinas

Ch = [] # Carga Horária das cursadas
ChT = [] # Carga Horária das trancadas

Periodo = [] 

disci = int(input("Em quantas disciplinas você se matriculou neste semestre?"))
trancadas = input("Fez trancamento parcial? (Responda apenas 'sim' ou 'não') ")
U = trancadas.upper()
# ----------------------------------------------
numerador = 0
denominador = 0
i = 1

while i <= disci:
  disciplina = input("Nome da disciplina: ")
  Disciplinas.append(disciplina) # disciplina é salva na lista Disciplinas

  if U == "NÃO": # Média só será pedida inicialmente se o aluno não tiver feito trancamento parcial
    media = float(input("Média: "))
    Media.append(media) # média é salva na lista Média

  ch = int(input("Carga Horária: "))
  Ch.append(ch) # carga horária é salva na lista Ch

  periodo = int(input("Periodo: "))
  Periodo.append(periodo) # período é salvo na lista Período

  numerador = media * ch * periodo + numerador 
  denominador = periodo * ch + denominador

  i+=1

IRA_sem_T = (numerador / denominador) # IRA sem trancamento parcial
# ----------------------------------------

if  U == "NÃO": # Se aluno não fez trancamento parcial:
  IRA = float(IRA_sem_T)
  print(f"IRA Individual:{IRA:.4f}" ) # IRA arredondado para 4 casas decimais
# -----------------------------------------------

if U == "SIM": # Se aluno fez trancamento parcial:
  qtd = int(input("Quantas disciplinas foram trancadas neste semestre ?"))
  z = 1
  while z <= qtd:
    print(Disciplinas)
    d = int(input("Informe o número da posição da disciplina trancada \n *Obs: a primeira posição começa com 0 "))
    D = Disciplinas[d] # A variável D recebe a disciplina trancada informada pelo aluno 
    DisciT.append(D) # A disciplina trancada é armazenada pela lista DisciT
    Disciplinas.pop(d) # A disciplina trancada é retirada da lista Disciplinas

    ChT.append(Ch[d]) # A carga horária da disciplina trancada é adicionada na lista ChT
    Ch.pop(d) # Carga horária da disciplina trancada é removida da lista Ch

    Periodo.pop(d) # O período da disciplina trancada é removida da lista Periodo

    z+= 1

  print("Informe as médias das disciplinas cursadas: ")
  for disc in Disciplinas:
    print(f"Disciplina: {disc}")
    media = float(input("Média: "))
    Media.append(media) # Média da disciplina trancada é armazenada na lista Media

  #---- Calculo do IRA quando alguém tranca ----

  T = sum(ChT) # Somatório das cargas horárias trancadas
  C = sum(Ch) + sum(ChT) # Soma do somatório das cargas horárias cursadas e das trancadas 

  somatorio1 = [Periodo[i] * Ch[i] * Media[i] for i in range(len(Periodo))] 
  # Lista somatório1 recebe a multiplicação entre os períodos, cargas horárias e médias, multiplicação
  # feita em índice por índice

  somatorio2 = [Periodo[i] * Ch[i] for i in range(len(Periodo))]
  #Lista somatório2 recebe a multiplicação entre os períodos e cargas horárias, multiplicação
  # feita em índice por índice
  Num = sum(somatorio1) # Somatório dos resultados de somatório1
  Den = sum(somatorio2) # Somatório dos resultados de somatório2 
  
  IRA_com_T = (1 - ((0.5 * T)/ C )) * ((Num)/(Den)) # IRA com trancamento parcial

  IRA = float(IRA_com_T)
  print(f"IRA individual: {IRA:.4f} ") # IRA arredondado para 4 casas decimais