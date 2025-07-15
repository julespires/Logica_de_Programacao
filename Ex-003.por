/*
 * Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
 * Ex:
 * Nome do Funcionário: Maria do Carmo
 * Salário: 1850,45
 * O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.
 * Autor:Jules do Nascimento Pires
 * Ex-003
 * Data:15/07/2025
 */

programa
{
	
	funcao inicio()
	{
	     // Variáveis
		cadeia nome
		real salario

          // Entrada de dados
		escreva("Nome do Funcionário:")
		leia(nome)
		escreva("Salário R$:")
		leia(salario)

          // Limpa a tela
          limpa()
          
          // Resultado
		escreva("o funcionário " + nome + " tem um salário de R$ " + salario)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 568; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */