/*
 * Faça um programa que receba quatro números inteiros, calcule e mostre a soma desses números.
 * Autor:Jules do Nascimento Pires
 * Ex-004
 * Data:14/07/2025
 */
programa
{
	
	funcao inicio()
	{
	     // Variáveis
		inteiro num1, num2, num3, num4

          // Entrada de dados
		escreva("Primeiro valor:")
		leia(num1)
		escreva("Segundo valor:")
		leia(num2)
		escreva("Terçeiro valor:")
		leia(num3)
		escreva("Quarto valor:")
		leia(num4)

          // Limpa a tela
          limpa()
		
          // Cálculo da soma
		inteiro soma = num1 + num2 + num3 + num4

          // Mostra o resultado
		escreva("Soma dos valores:" + soma)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 560; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */