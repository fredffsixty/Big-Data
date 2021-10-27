#!/usr/bin/env python
import sys

'''
Script che fonde due liste di elementi passate da linea di comando e separate da virgole e restituisce
la lista ordinata senza duplicati ed opzionalmente in ordine inverso:

linear_merge.py [-r] <lista1> <lista2>
'''

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
# liste di input; il risultato viene privato dei duplicati chiamando removeDuplicates();
# si ottiene una lista ordinata all'inverso per cui alla fine
# si inverte l'ordine degli elementi nella lista risultato se si vuole una lista ordinata
# convenzionalmente
#
def merge(list1, list2, rev=False):
    out_list = list1 + list2

    removeDuplicates(out_list)      # rimozione duplicati
    out_list.sort()                 # ordinamento

    if rev:
        out_list.reverse()          # inversione, se richiesta

    return out_list

##
#
# Stampa il messaggio di errore passato come argomento insieme alle modalità di utilizzo dello script
#
def errorMessage(error_string):
    print(f'{error_string}\n\nUtilizzo: linear_merge.py [-r] <lista separata da virgole> <lista separata da virgole>')
    exit()

def main():

    to_reverse = False                           # Flag che indice se il risultato finale dev'essere invertito

    if len(sys.argv) < 2 or len(sys.argv) > 4\
        or (len(sys.argv) == 4 and sys.argv[1] != '-r'):  # verifica la lunghezza e correttezza degli argomenti
        errorMessage('Argomenti non validi!')
    elif len(sys.argv) == 3:           # caso in cui la lista non dev'essere invertita
        l1 = sys.argv[1].split(',')    # converte la lista ottenuta dall'argomento di ingresso
        l2 = sys.argv[2].split(',')    # separando i token rispetto allo spazio
    else:
        to_reverse = True
        l1 = sys.argv[2].split(',') # analogo discorso, ma con secondo argomento impostato a '-r'
        l2 = sys.argv[3].split(',')

    result = merge(l1,l2,rev=to_reverse) # fusione con rimozione dei duplicati e eventuale inversione

    print(result)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()