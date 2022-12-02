
def somma(n1, n2):
    return n1 + n2

def sottrazione(n1,n2):
    return n1 - n2

def moltiplicazione(n1, n2):
    return n1 * n2

def divisione(n1, n2):
    return n1 / n2

operzione = {
    "+" : somma,
    "-" : sottrazione,
    "*" : moltiplicazione,
    "/" : divisione
}




def calcola(numero1):

    num1 = numero1
    for o in operzione:
        print(o + " ", end='')

    simbolo_operazione = input("\nscegliere l'operazione\n")

    num2 = float(input("inserire secondo numero\n"))

    risultato = operzione[simbolo_operazione](num1, num2)
    print(f"\nil risultato di {num1} {simbolo_operazione} {num2} = {risultato}")
    continua = input("altre operazioni: Y or NEW\n").lower()
    if continua == 'y':
        print(f"\nvalore attuale: {risultato}")
        calcola(risultato)
    elif continua == 'new':
        print("\nnuova operazione\n\n")
        nuovo_num = float(input("inserisci primo numero: "))
        calcola(nuovo_num)
    else:
        print("\nend".upper())


                    #start
numero1 = float(input("inserisci un numero\n"))
calcola(numero1)