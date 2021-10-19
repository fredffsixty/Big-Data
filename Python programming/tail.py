#!/usr/bin/env python

'''
Script che restituisce la sottostringa ottenuta del primo argomento
da linea di comando a partire dal carattere o numero di posizione passato
come secondo argomento:

tail.py <stringa> <carattere>|<indice>
'''
import sys

def lastIndexOf(s,c):
  '''
  lastIndexOf(str,chr) --> int

  Restituisce l'indice dell'ultima occorrenza del carattere c
  nella stringa s ovvero -1 nel caso in cui c non sia presente in s
  '''
  return len(s) - 1 - s[::-1].index(c) if c in s else -1


def main():

  if len(sys.argv) != 3:
    print('Numero errato di argomenti: tail.py <stringa> <indice>|<carattere>')
  elif not sys.argv[1].isalpha() or\
        not(sys.argv[2].isdigit() or\
           (sys.argv[2].isalpha() and len(sys.argv[2]) == 1)):

    print('Tipo errato degli argomenti: tail.py <stringa> <indice>|<carattere>')
  else:
    idx = int(sys.argv[2]) if sys.argv[2].isdigit() else lastIndexOf(sys.argv[1],sys.argv[2])

    print(sys.argv[1][idx::] if idx in range(0,len(sys.argv[1])) else\
          'Indice non compreso nella stringa')


if __name__ == '__main__':
  main()