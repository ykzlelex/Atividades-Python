programa
{
	
	funcao inicio()
	{
	inteiro numero, i
	escreva("digite um numero entre 1 e 10: ")
	leia(numero)
	enquanto(numero<1 ou numero>10) {
		escreva("valor invalido! digite entre 1 e 10: ")
		leia(numero)
	i=1
	enquanto(i<=10) {
		escreva("numero, "x", i, "=", numero*i, "\n")
	i=i+1
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 287; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */