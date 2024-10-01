def segundoDigito(cpf):
  '''
  Função que verificará se o segundi digito verificador é valido.
  
  Para verificar deve-se somar o resultado das multiplicações dos nove primeiros números do cpf mais o primeiro dígito verificar da esquerda pra direita por 11 até 2
  Exemplo: 1*11 + 7*10 + 9*9 + 3*8 + 5*7 + 1*6 + 4*5 + 9*4 + 6*3 + 7*2
  
  Após, deve-se multiplicar esse resultado por 10 e divir por 11.
  Se o resto dessa divisão for igual o segundo dígito verificar, ele é válido.
  
  Assim, o CPF será válido.
  '''
  cpfTexto = str(cpf)
  contador = 0
  for i in range(10):
    contador += int(cpfTexto[i]) * (11 - i)
  digito2 = (contador * 10) % 11
  if digito2 == 10:
    digito2 = 0
  return digito2