
def IRA_sem_T(disciplinas):
    # função para cálculo do IRA sem trancamento parcial
   numerador = 0 
   denominador =  0
   i = 1
   while i <= disciplinas:
        media = float(input("Média: "))
        ch = int(input("Carga Horária: "))
        periodo = int(input("Periodo: "))
        numerador = media * ch * periodo + numerador
        denominador = periodo * ch + denominador
        i+=1

   total = (numerador / denominador) * 1000
   total_int = int(total)
   print("IRA Individual:", total_int )
   
   
   

disciplinas = int(input("Quantas disciplinas você cursou neste semestre? "))
trancadas = input("Fez trancamento parcial? (Responda apenas 'sim' ou 'não') ")

T = trancadas.upper()
if  T == "NÃO":
    IRA_sem_T(disciplinas)

else:
   """ Não terminado!!!!
   Acredito que será preciso criar outra função para calcular o IRA com trancamento parcial.
   As informações sobre o cálculo do IRA estão em https://prograd.ufc.br/pt/perguntas-frequentes/ira/"""
   
