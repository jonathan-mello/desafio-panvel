"""
Dois cachorros (Bob e Rex) e um gato (Oli) estão em uma linha. Os
cachorros se movem de forma igualitária (para frente e para trás). O
gato, está se alimentando. O cachorro que chegar no ponto antes,
consegue pegar o gato distraído, caso os dois cachorros cheguem no
ponto do gato no mesmo momento, eles começam a brigar e o gato
consegue fugir.

Sua tarefa é: Dado os pontos atuais dos animais, descobrir quem irá
sair vitorioso.

Exemplos: Segue abaixo alguns exemplos

BOB -> B
REX -> R
OLI -> O

1. ---B--R--O----------
2. ----B--R-O----------
3. -----B--RO----------

Rex pegará o gato.

1. ---R-------O--B-----
2. ----R-------O-B-----
3. -----R-------OB-----

Bob pegará o gato

1. --------R--O--B-----
2. ---------R-O-B------
3. ----------ROB-------

Bob e Rex chegarão ao mesmo tempo, portanto, Oli conseguirá fugir.

Sua implementação deve ter uma função que recebe 3 números inteiros
sempre positivos, e deve retornar uma string com o nome do animal.
Exemplo:
def teste(rex, bob, oli):
    ...
    return "nome"

"""

def animal(rex, bob, oli):
    
    if not (isinstance(rex, int) and isinstance(bob, int) and isinstance(oli, int)):
        return "Todos os parâmetros precisam receber valores inteiros!"
    elif rex < 0 or bob < 0 or oli < 0:
        return "Todos os parâmetros precisam receber valores inteiros positivos!"
    
    else:
        distancia_rex = abs(rex - oli)
        distancia_bob = abs(bob - oli)
    
        if distancia_rex < distancia_bob:
            return "rex"
        elif distancia_bob < distancia_rex:
            return "bob"
        else:
            return "oli"
