/*
 * Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.
 * Autor:Jules do Nascimento Pires
 * Ex:006
 * Data:14/07/2025
 */
programa
{
     // Utilização da biblioteca Matemática
     inclua biblioteca Matematica -->mat
	
	funcao inicio()
	{
	     // Variáveis 
		real nota1, nota2, nota3
		inteiro peso1, peso2, peso3

          // Entrada de dados
		escreva("Primeira nota:")
		leia(nota1)
		escreva("Primeiro peso:")
		leia(peso1)

		escreva("Segunda nota:")
		leia(nota2)
		escreva("Segundo peso:")
		leia(peso2)
		
		escreva("Terçeira nota:")
		leia(nota3)
		escreva("Terçeiro peso:")
		leia(peso3)

          // Limpa
		limpa()

          // Cálculo da média ponderada
		real media = (nota1 * peso1 + nota2 * peso2  + nota3 * peso3) / (peso1 + peso2 + peso3)

          // Mostra o resultado
		escreva("Média ponderada das notas:" + mat.arredondar(media, 3))
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 231; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */