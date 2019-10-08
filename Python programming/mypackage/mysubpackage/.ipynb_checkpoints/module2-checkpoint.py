"""
Il modulo module2 è caricato da subpackage
"""

def myMethod(*args,**kwargs):
    """
    myMethod(*args,lang=en,newline=False) -- stampa un messaggio di saluto ad args in 
    inglese e senza andare a capo dopo ogni saluto.
    
    lang=it saluta in italiano
    newline=True va a acapo dopo ogni saluto
    """
    # valori di defalut degli argomenti
    saluto = 'Hello'
    separatore = ', '
    
    result = ''

    try:
        if len(kwargs) >2:
            raise SyntaxError('Invalid arguments')
        else:
            for k in kwargs.keys():
                if k not in {'lang','newline'}:
                    raise SyntaxError('Invalid arguments')
                elif k == 'lang':
                    if kwargs[k] == 'it':
                        saluto = 'Ciao'
                elif k == 'newline':
                    if kwargs[k] == True:
                        separatore = '\n'
                elif (k == 'lang' and kwargs[k] != 'en') or (k == 'newline' and kwargs[k] != False):
                    raise SyntaxError('Invalid arguments')
    except SyntaxError:
        return None
        raise
    else:
        for people in args:
            if args.index(people) == len(args) -1:
                result += f'{saluto} {people}! \n'
            else:
                result += f'{saluto} {people}! {separatore}'
        return result
