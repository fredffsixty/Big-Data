#!/usr/bin/env python
import sys

##
#
# scandisce la lista e, per ogni elemento, analizza i successivi;
# se trova un elemento uguale all'elemento considerato, lo rimuove
#
def removeDuplicates(l):
    for i in l:
        for j in l[l.index(i)+1:]:
            if i==j:
                l.pop(l.index(j))

##
#
# scandisce list1 e list2 a partire dalla fine e confronta sempre gli ultimi elementi
# tra di loro, trasferendoli nella lista risultato e rimuovendoli dalle
# liste di input; si ottiene una lista ordinata all'inverso per cui alla fine
# si inverte l'ordine degli elementi nella lista risultato
#
def merge(list1, list2):
    out_list = []

    while len(list1) > 0 or len(list2) > 0:
        if len(list1) > 0 and len(list2) > 0:
            if list1[-1] >= list2[-1]:
                out_list.append(list1.pop())
            else:
                out_list.append(list2.pop())
        elif len(list1) > 0:
            out_list.append(list1.pop())
        else:
            out_list.append(list2.pop())

    out_list.reverse()
    return out_list

##
#
# Stampa il messaggio di errore passato come argomento insieme alle modalità di utilizzo dello script
#
def errorMessage(error_string):
    print(f'{error_string}\n\nUtilizzo: linear_merge.py [<tipo elementi>] \'<lista separata da spazi>\' \'<lista separata da spazi>\'')
    print('<tipo elementi>: --str|--tuple|--int|--float\ndefault: --str')
    exit()

##
#
# converte gli elementi della lista l secondo lo specificatore di tipo passato come secondo argomento
# crea una lista dal mapping della lista di ingresso attraverso una funzione anonima che valuta
# la stringa ottenuta dallo specificatore di tipo concatenato con ogni elemento in modo da formare la sintassi
# del costruttore relativo; ad es '--str' --> 'str(el)'
#
def convertToType(l,type_flag):

    return list(map(lambda el : eval(type_flag[2:]+'('+el+')'),l))

def main():

    if len(sys.argv) < 3 or len(sys.argv) > 4:  # verifica la lunghezza degli argomenti
        errorMessage('Argomenti non validi!')
    elif len(sys.argv) == 3:                    # caso dello specificatore di tipo omesso
        type_flag='--str'
        l1 = convertToType(sys.argv[1].split(' '),type_flag)    # converte la lista ottenuta dall'argomento di ingresso
        l2 = convertToType(sys.argv[2].split(' '),type_flag)    # separando i token rispetto allo spazio
    else:
        if sys.argv[1] not in {'--str','--tuple','--int','--float'}:    # verifica che lo specificatore di tipo
            errorMessage('Tipo degli elementi non valido!')             # sia corretto
        else:
            type_flag = sys.argv[1]
            l1 = convertToType(sys.argv[2].split(' '),type_flag)
            l2 = convertToType(sys.argv[3].split(' '),type_flag)

    result = merge(l1,l2)           # fusione

    removeDuplicates(result)        # rimozione duplicati

    result.sort()                   # ordinamento finale
    print(result)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()