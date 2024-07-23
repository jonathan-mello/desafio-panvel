"""
Analise os trechos de código abaixo, escritos em uma linguagem de programação hipotética, 
fazendo uso dos comandos “while-do” (enquanto-faça) e “do-while” (faça-enquanto) e supondo 
que a, b e c foram declaradas anteriormente. Quais são os valores de a, b e c, após o 
término de cada trecho, se as variáveis a, b e c forem inicializadas com 3, 0 e 3, respectivamente, 
antes de cada trecho?

while (c < a) do {
    a=a-1
    b=b+1
    c=c+b
}

do {
    a=a-1
    b=b+1
    c=c+b
} while (c < a)
"""

"""
RESOLUÇÃO:

A = 3
B = 0
C = 3

PRIMEIRO TRECHO:
Como "C" não é menor que "A", logo, nenhuma instrução será executada para os valores iniciais de A, B e C.
Então a resposta é:
A=3
B=0
C=3

SEGUNDO TRECHO:
A = 3 - 1
B = 0 + 1
C = 3 + 1

Resolvendo:

A = 2
B = 1
C = 4

"C" é menor que "A"? NÃO. Logo:

A = 2
B = 1
C = 4

"""