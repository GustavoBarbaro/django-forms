from django.db import models

# Create your models here.

# lembrando que cada classe aqui significa uma nova tabela no BD

class Size (models.Model):
    title = models.CharField(max_length=100)

    #isso aqui eh pra ajudar a mostrar o titulo direto na lista quando acessar o painel de admin
    def __str__(self):
        return self.title


class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    
    #fazer a conexao com a outra tabela
    size = models.ForeignKey(Size, on_delete=models.CASCADE)