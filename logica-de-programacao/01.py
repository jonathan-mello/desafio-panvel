"""

Para a parte de programa abaixo, com m=3 e n=3, qual seria a saída?

leia (m,n)
para i de 1 ate m faça
    para j de 1 ate n faça
        se (i=j) entao
            matriz[i,j] <- 1
        senao
            matriz [i,j] <- 0
        fimse
    fimpara
fimpara
"""

"""
RESOLUÇÃO

Considerando que em uma matriz existem os caracteres "i" para representar a linha e "j" para representar a coluna,
o exercício determina a criação de uma matriz 3x3 passando condições para os seus valores de acordo com as posições
dos elementos. Os valores que vão compor a matriz serão 0 ou 1.

Ao iniciar a resolução da matriz, o elemento será ij[1x1]. Isso significa que a linha ("i") e a coluna ("j") estarão
na posição 1. Logo, atendem a primeira condição estipulada no exercício "se (i=j) então o valor será 1".

1 x x
x x x
x x x

Já no segundo elemento, a linha continuará sendo a primeira (i = 1) mas a coluna será a segunda (j = 2). Isso significa
que, por não atender a primeira condição do exercício, automaticamente cairá no bloco else onde o valor será 0.

1 0 x
x x x
x x x

Resolvendo o restante do exercício teremos:

1 0 0
0 1 0
0 0 1
"""

