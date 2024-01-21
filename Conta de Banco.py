class Banco:
  def __init__(self, conta, usuario, senha):
    self.conta = conta
    self.usuario = usuario
    self.senha = senha

class Pessoa:
  def __init__(self, nome, idade, sexo):
    self.nome = nome
    self.idade = idade
    self.sexo = sexo

if __name__ == "__main__":
  pessoa1 = Pessoa("João", 20, "M")
  pessoa2 = Pessoa("Alice", 21, "F")
  pessoa3 = Pessoa("Bianca", 25, "F")

  usuario1 = Banco("0009235", pessoa1.nome, 257895)
  usuario2 = Banco("0009236", pessoa2.nome, 874563)
  usuario3 = Banco("0009237", pessoa3.nome, 345678)

  print(
      f'''
    {pessoa1.nome} possui {pessoa1.idade} anos e é do sexo {pessoa1.sexo}
    criou a conta {usuario1.conta}

    {pessoa2.nome} possui {pessoa2.idade} anos e é do sexo {pessoa2.sexo}
    criou a conta {usuario2.conta}

    {pessoa3.nome} possui {pessoa3.idade} anos e é do sexo {pessoa3.sexo}
    criou a conta {usuario3.conta}
      '''
  )