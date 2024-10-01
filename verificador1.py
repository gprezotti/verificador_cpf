def primeiroDigito(cpf):
  '''
  Função que verificará se o primeiro digito verificador é valido.
  
  Para verificar deve-se somar o resultado das multiplicações dos nove primeiros números do cpf da esquerda pra direita por 10 até 2
  Exemplo: 1*10 + 7*9 + 9*8 + 3*7 + 5*6 + 1*5 + 4*4 + 9*3 + 6*2
  
  Após, deve-se multiplicar esse resultado por 10 e divir por 11.
  Se o resto dessa divisão for igual o primeiro dígito verificar, ele é válido.
  
  Assim, deve-se passar para a segunda verificação
  '''
  cpfTexto = str(cpf)
  contador = 0
  for i in range(9):
    contador += int(cpfTexto[i]) * (10 - i)
  digito1 = (contador * 10) % 11
  if digito1 == 10:
    digito1 = 0
  return digito1