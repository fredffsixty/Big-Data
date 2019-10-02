#!/usr/bin/env python
import sys

##
#
# calcola l'indice dell'ultima occorrenza di c in s come *prima occorrenza* nell'inversa di s
# e poi sottrae questa posizione dalla lunghezza totale della stringa
#
def lastIndexOf(s,c):
    return len(s) - 1 - s[::-1].index(c)

def main():

  # gestione dell'input
  if len(sys.argv) != 3:
    print('Errore negli argomenti!!\n\nUso: tail.py <stringa> <carattere>|<indice>')

  elif not sys.argv[2].isdigit():       # verifica che il secondo argomento non sia una stringa tutta numerica
                                        # e quindi cerca la sua ultima occorrenza nella string aprimo argomento
      print(sys.argv[1][lastIndexOf(sys.argv[1],sys.argv[2]):])
  else:
      i=int(sys.argv[2])                                    # converte il secondo argomento in un numero
      if i < -len(sys.argv[1]) or i >= len(sys.argv[1]):    # verifica che non sia fuori dagli indici consentiti
          print('Indice del carattere fuori dal range')
      else:
          print(sys.argv[1][i:])                            # stampa direttamente la sottostringa a partira dalla
                                                            # posizione individuata

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()