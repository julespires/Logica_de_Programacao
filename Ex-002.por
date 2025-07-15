/*
 * Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boasvindas para ela:
 * Ex:
 * Qual é o seu nome? João da Silva
 * Olá João da Silva, é um prazer te conhecer!
 * Autor:Jules do Nascimento Pires
 * Ex-002
 * Data:15/07/2025
 */
programa
{
	
	funcao inicio()
	{
	     // Variável
		cadeia nome

          // Entrada do nome
		escreva("Qual é o seu nome?")
		leia(nome)

		limpa()

          // Resultado
		escreva("Olá, " + nome + " é um prazer te conhecer!")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 402; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */