"""
Criptografia de mensagem. Essa cifra, considera em girar as letras a 
partir de um seguinte número de posições. Sendo assim, a pessa que
recebe a mensagem, sabe quantas posições voltar, e portanto, terá a
mensagem original.

Sua tarefa é: dado um texto qualquer, realizar a rotação. 
Obs.: Não precisa considerar caracteres com acentos, como: á, à e etc...

alfabeto: abcdefghijklmnopqrstuvwxyz

Exemplo:
texto = Ola, meu nome eh Carlos! E o Seu?
rotacoes = 7
resultado = Vsh, tlb uvtl lo Jhysvz! L v zlb?

Sua implementação deve ter uma função que receba um número inteiro
positivo (a rotação) e um texto, e deve retornar o texto cifrado.

Exemplo:
teste(rotacoes, texto):
    ...
    return texto_cifrado
"""

def criptografia(rotacoes, texto):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_maiusculo = alfabeto.upper()
    
    texto_cifrado = []
    
    for caractere in texto:
        if caractere in alfabeto:
            nova_posicao = (alfabeto.index(caractere) + rotacoes) % len(alfabeto)
            texto_cifrado.append(alfabeto[nova_posicao])
        elif caractere in alfabeto_maiusculo:
            nova_posicao = (alfabeto_maiusculo.index(caractere) + rotacoes) % len(alfabeto)
            texto_cifrado.append(alfabeto_maiusculo[nova_posicao])
        else:
            texto_cifrado.append(caractere)
    
    return ''.join(texto_cifrado)

        