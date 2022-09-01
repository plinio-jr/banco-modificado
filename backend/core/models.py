from django.db import models

class Usuario(models.Model):
    email = models.CharField(max_length=110)
    nome = models.CharField(max_length=110)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.email, self.nome, self.senha

class Produto (models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    quantidade = models.Field(max_length=3)
    peso = models.FloatField(max_length=5)
    preco = models.FloatField(max_length=4)
    lista = models.ForeignKey(
        Usuario, on_delete=models.PROTECT, related_name="codigo"
    )

    def __str__(self):
        return self.nome, self.categoria, self.quantidade, self.peso, self.preco

class Lista (models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    codigo = models.CharField(max_length= 10)


    def __str__(self):
        return self.titulo, self.descricao

class Mercado (models.Model):
    nome = models.CharField(max_length=150)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome, self.rua, self.bairro, self.cidade
