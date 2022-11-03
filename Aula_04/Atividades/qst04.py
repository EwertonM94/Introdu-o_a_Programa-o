num1=float(input("Digite a nota da sua primeira avaliação: "))
num2=float(input("Digite a nota da sua segunda avaliação: "))
M=(num1+num2)/2
if M>=6:
    print(f'Você está aprovado, parabéns! Sua média é {M}')
elif M < 4:
    print(f"Você reprovou sem direito a prova final, sua media foi {M}")
else:
    print(f'Você precisa fazer a prova final, sua média é {M}')    