from verificador1 import primeiroDigito
from verificador2 import segundoDigito

def cpfValido(cpf):
  '''
  Verifica todos as exceções para o CPF ser inválido, como os digitos verificadores não serem validos, ou o CPF for uma sequencia de dígitos repetidos
  
  Também manda uma mensagem de erro casa o usuário digite um CPF com um número de dígitos diferente de 11
  '''
  cpfTexto = str(cpf)
  tamanho = len(cpfTexto)
  if tamanho != 11:
    print("Por favor digite um CPF com 11 números (sem pontos e hífens)!")
    return
  
  
  if primeiroDigito(cpf) != int(cpfTexto[9]):
    print("CPF inválido!")
  elif segundoDigito(cpf) != int(cpfTexto[10]):
    print("CPF inválido")
  elif cpfTexto == cpfTexto[0] * tamanho:
    print("Esse CPF não é válido pois é composto somente por dígitos iguais!")
  else:
    print("Esse CPF é válido!")