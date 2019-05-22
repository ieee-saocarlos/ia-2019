#soma dos pares fibonaccci
termo1 = 1
termo2 = 1
termo3 = 2
tamanhoseq = int(input('Digite o numero de termos da sequencia de fibonacci: ', ))
i=3
somadosparessequencia =[]
#print (termo3)
while i <= tamanhoseq:
    fn = termo2 + termo3
    termo2 = termo3
    termo3 = fn
    i = i + 1

    if (fn % 2) == 0:
        somadosparessequencia.append(fn)

    print ("\n" + str(i)) #testedoandamentodasequencia
print (2 + sum(somadosparessequencia))

