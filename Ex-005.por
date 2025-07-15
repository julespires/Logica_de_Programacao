/*
 * Faça um programa que receba três notas, calcule e mostre a média aritmética.
 * Autor:Jules do Nascimento Pires
 * Ex-005
 * Data:14/07/2025
 */

programa
{
     // Utilização da biblioteca Matematica
	inclua biblioteca Matematica --> mat
	
	funcao inicio()
	{

	     // Variáveis
		real nota1, nota2, nota3

          // Entrada de dados
		escreva("Primeira nota:")
		leia(nota1)
		escreva("Segunda nota:")
		leia(nota2)
		escreva("Terçeira nota:")
		leia(nota3)

          // Limpa a tela
          limpa()
          
          // Cálculo da média
		real media = (nota1 + nota2 + nota3) / 3

          // Resultado
		escreva("Média aritimética das notas:" + (mat.arredondar(media, 3)))
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 501; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */