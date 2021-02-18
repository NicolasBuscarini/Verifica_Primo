def main():
    
    def maiorPrimo(n):
        c = n        
        while c > 1 and ePrimo(c)==False:           #Testa de um em um em ordem decrescente
            c = c - 1                               #Se der True em algum Restornara o numero testado
        return c                                    #O numero testado é um numero primo mais proximo do numero digitado.

    def ePrimo(c):      

        primo = True                                # O valor começa como True Por causa do numero 2 que tambem é primo    
        div = 2

        while c>div:                                #Testa todos os numero até o numero digitado
    
            if c % div == 0:
                primo = False                       #Quando qualquer um dos numeros testados der resto 0 entao primo tem valor Falso
            div = div + 1                           #O numero com valor falso não é um primo
    
        return primo 

    x = int(input("Digite um número inteiro maior ou igual a 2: "))
    
    if (maiorPrimo(x))<=1:                          # 1 e 0 NÃO é primo!
        print("Não existe um número primo menor ou igual ao número digitado!")
        
    else:
        print("O  maior número primo menor ou igual ao número digitado é: ", maiorPrimo(x))

main()

    
        
