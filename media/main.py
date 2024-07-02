#Programa:Calculadora de Média
#Programa desenvolvido por: Jhonnata de Souza Farias

from calc_media import Media

nota1=int(input("Digite sua nota1: "))
while nota1<0 or nota1>10:
    print('!|A nota não pode ser menor que 0 ou maior que 10|!')
    nota1=float(input('!|Tente novamente: !'))
if nota1>=5:
    print("==>|Esta nota esta no AZUL|")
elif nota1==10:
    print("==>|Parabens, esta nota esta no AZUL|")
else:
    print("==>|Esta nota esta no VERMELHO|")

nota2=int(input("Digite sua nota2: "))
while nota2<0 or nota2>10:
    print('!|A nota não pode ser menor que 0 ou maior que 10|!')
    nota2=float(input('!|Tente novamente: !'))
if nota2>=5:
    print("==>|Esta nota esta no AZUL|")
elif nota2==10:
    print("==>|Parabens, esta nota esta no AZUL|")
else:
    print("==>|Esta nota esta no VERMELHO|")
            
nota3=int(input("Digite sua nota3: "))
while nota3<0 or nota3>10:
    print('!|A nota não pode ser menor que 0 ou maior que 10|!')
    nota3=float(input('!|Tente novamente: |!'))
if nota3>=5:
    print("==>|Esta nota esta no AZUL|")
elif nota3==10:
    print("==>|Parabens, esta nota esta no AZUL|")
else:
    print("==>|Esta nota esta no VERMELHO|")
    if nota3>=5:
        print("==>|Esta nota esta no AZUL|")

resultado = Media.calcular(nota1,nota2,nota3)
print('Sua Média é:', resultado)