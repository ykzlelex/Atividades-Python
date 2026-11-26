programa
{
	
	funcao inicio()
	{
	    inteiro i, numero, maior, menor, soma=0
	    i=1
	    enquanto(i<=10){
	    		escreva("digite umn numero: ")
	    		leia(numero)
	    		se(i==1)
	    		{
	    			maior = numero
	    			menor = numero
	    		}
	    		se(numero>maior){
	    			maior= numero
	    		}se(numero<menor){
	    			menor = numero	}
	    }
	          i++
		escreva("media:", soma/10.0, "\n")
		escreva("maior:", maior, "\n")
		escreva("menor:", menor, "\n")
	    }
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 347; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */