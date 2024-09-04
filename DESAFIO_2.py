def verificar_ocorrencia_a(texto):

  texto_minusculo = texto.lower()
  contador = texto_minusculo.count('a')
  encontrado = contador > 0
  return encontrado, contador
texto_entrada = input("Digite uma string: ")
resultado, quantidade = verificar_ocorrencia_a(texto_entrada)
if resultado:
  print(f"A letra 'a' foi encontrada {quantidade} vezes na string.")
else:
  print("A letra 'a' não foi encontrada na string.")
