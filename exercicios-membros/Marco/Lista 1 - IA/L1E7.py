# Exercicio 7 - Lista 1 : determine qual letra mais se repete e quantas vezes essa letra se repetiu dentro da Lista
continuar="sim"
while continuar == "sim":
	stri=input("Digite uma string a ser modificada\n")
	st=stri

	# Retirar espacos e pontuacao p/ saber quantas letras tem na string
	pontos=[" ",",",".","!","?",":",";","'"]
	for i in pontos:
		n_st=st.split(i)
		st="".join(n_st)

	# Pedir o numero de letras p/ uppar e ver se ha esse numero disponivel
	num_m= int(input("Forneca um numero inteiro para ser as primeiras letras a ficarem maisculas:\n"))
	if (num_m>len(st)):
	    num_m= int(input("Forneca outro numero inteiro, o numero e maior que o numero de letras na string.\n"))

	# Percorrer a string, verificando com o banco se o caracter é uma letra. Caso seja, uppa-la.
	# Caso não seja, so somar "o nao letra" e aumentar o range do while em uma unidade, p/ ser possivel encontrar a prox letra a uppar.
	stri=stri.lower()
	i=0
	flag=0
	letras =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	new_stri=""
	while i<num_m:
		for j in range (len(letras)):
			if stri[i]==letras[j]:
				flag=1
		if flag!=0:
			new_stri = new_stri + stri[i].upper()
		elif flag==0:
			new_stri = new_stri + stri[i] 
			num_m=num_m+1
			
		flag=0
		i=i+1

	# Ate aqui, programa aumenta o range sempre que ha um "nao letra"; ele para quando uppar o numero de pedido de letras.
	# Logo, a partir desse ponto, se preciso, necessario adicionar a new_stri o resto da stri, mas de forma minuscula. 
	if num_m<len(stri):
		new_stri=new_stri+stri[num_m:] 

	print("A nova string, sera:",new_stri)
	continuar = input("Deseja modificar outra string [sim/nao]?\n")
