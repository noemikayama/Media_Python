print("\n\n ===============================================================================================================================\n\n")
print("\n\t\t * Calculadora de Médias da Componente Curricular Algoritmos de Programação, Projetos e Computação * \n\n")
alunos = []
acima_de_5 = 0
num_alunos = int(input("\n\n Insira quantos alunos deseja analisar: "))
for i in range(num_alunos):
   notas = []

   nome = input("\n\n Nome completo: ")
 

   prova_teorica = []
   T1 = float(input("\n Nota no T1: "))
   T2 = float(input("\n Nota no T2: "))
   prova_teorica.append(T1)
   prova_teorica.append(T2)


   projeto = []
   P1 = float(input("\n\n Nota do P1: "))
   P2 = float(input("\n Nota do P2: "))
   projeto.append(P1)
   projeto.append(P2)


   medias = []
   MT = 0.4*T1 + 0.6*T2
   MP = (P1 + P2)/2
   medias.append(MT)
   medias.append(MP)


   if (MT >= 5 and MP >= 5):
       MF = 0.3*MP + 0.7*MT
   elif (MT <= MP):
       MF = MT
   else:
       MF = MP


   if (MF >= 5):
       acima_de_5 = acima_de_5 + 1


   notas.append(nome)
   notas.append(prova_teorica)
   notas.append(projeto)
   notas.append(medias)
   notas.append(MF)
   alunos.append(notas)


n = 1


while (n > 0):
   print("\n\n ===================================================================================================================== \n\n")
   print("\n\t\t\t * MENU * ")
   print("\n\t 1 - Boletim com o nome de cada aluno, sua Média Teórica (MT), Média Prática (MP) e Média Final (MF)")
   print("\n\t 2 - Buscar aluno e mostrar informações")
   print("\n\t 3 - Exibir aluno com maior média final (MF)")
   print("\n\t 4 - Exibir aluno com menor média final (MF)")
   print("\n\t 5 - Percentual de alunos com média final (MF) superior a 5.0")

   menu = int(input("\n\n Qual opção deseja selecionar? : "))

   while (menu < 1 or menu > 5):
       print("\n Opção inválida! Selecione um número entre 1-5!")
       menu = int(input("\n\n Qual opção deseja selecionar? : "))


   if (menu == 1):
       for i in range(num_alunos):
           print(f"\n\n\t Boletim de {alunos[i][0]}")
           print(f"\n - Média Teórica (MT): {alunos[i][3][0]:.1f}")
           print(f"\n - Média Prática (MP): {alunos[i][3][1]:.1f}")
           print(f"\n - Média Final (MF): {alunos[i][4]:.1f}")
  
   if (menu == 2):
       pesquisa_nome = input("\n\n Digite o nome completo do aluno que deseja pesquisar: ")
       encontrado = False


       for i in range(num_alunos):
           if (pesquisa_nome.lower() == alunos[i][0].lower()):
               print("\n\n Este aluno está na lista de alunos!")
               encontrado = True
               print(f"\n\n\t\t * Notas de {alunos[i][0]} * ")
               print(f"\n - T1: {alunos[i][1][0]}")
               print(f"\n - T2: {alunos[i][1][1]}")
               print(f"\n - Média Teórica (MT): {alunos[i][3][0]:.1f}")
               print(f"\n - P1: {alunos[i][2][0]}")
               print(f"\n - P2: {alunos[i][2][1]}")
               print(f"\n - Média Prática (MP): {alunos[i][3][1]:.1f}")
               print(f"\n - Média Final (MF): {alunos[i][4]:.1f} \n\n")
               break
       if (encontrado == False):
           print("\n\n Aluno(a) não encontrado(a) \n\n")


   if (menu == 3):
       nota_maxima = 0
       for i in range(num_alunos):
           if(alunos[i][4] > nota_maxima):
               nota_maxima = alunos[i][4]
       for i in range(num_alunos):
           if (nota_maxima == alunos[i][4]):
               print(f"\n A MF (Média Final) máxima é {nota_maxima:.1f} e é do aluno(a) {alunos[i][0]} \n\n")


   if (menu == 4):
       nota_minima = 10
       for i in range(num_alunos):
           if(alunos[i][4] < nota_minima):
               nota_minima = alunos[i][4]
       for i in range(num_alunos):
           if (nota_minima == alunos[i][4]):
               print(f"\n A MF (Média Final) mínima é {nota_minima:.1f} e é do aluno(a) {alunos[i][0]} \n\n")


   if (menu == 5):
       percentual = acima_de_5 / num_alunos * 100
       print(f"\n\n O percentual de alunos com Média Final (MF) acima de 5.0 é de: {percentual:.1f}% \n\n ")

   n = int(input("\n\n Digite qualquer tecla para voltar ao menu ou 0 para encerrar o programa: "))

print("\n\n\t\t\t * FIM DO PROGRAMA * \n\n")
