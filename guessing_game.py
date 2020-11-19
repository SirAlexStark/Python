import random
def validacao ():

   print('************************************************************************************************')
   print("Olá seja bem vindo ao jogo da adivinhação, minha tarefa é acertar o número que você escolher")
   print("***********************************************************************************************")

   numero_secreto = int(input("Qual é o número secreto ? "))
   chute = random.randrange(10, 20)
   maior = chute > numero_secreto
   menor = chute < numero_secreto


   total_tentativas = 1


   while (total_tentativas <= 5):

     chute = random.randrange(10, 20)
     valida = input("O número secreto é o {}, acertei ?".format(chute)).lower()
     if(numero_secreto < 10 or numero_secreto > 20):
            print("Você deve digitar um Número entre 10 e 20")
            continue
     
     acertei = numero_secreto == chute
     print(total_tentativas)
     

     if (acertei and valida == "sim"):
          print("Acertei, fim de jogo")
          break

     elif maior:
          print("Poxa meu chute foi acima do Numero secreto")
          total_tentativas = total_tentativas + 1

     elif menor:
          print("Poxa meu chute foi abaixo do numero secreto")
          total_tentativas = total_tentativas + 1

     if(total_tentativas == 5):
         print("Desisto, perdi o jogo")


       

if(__name__ == '__main__'):
    validacao()





 

    




























