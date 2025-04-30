from django.db import models

class Client(models.Model):
    # Tupla de gêneros
    GENDER_CHOICES = [
        ("male", "Masculino"),
        ("female", "Feminino"),
        ("non_binary", "Não-Binário"),
        ("other", "Outro")
    ]

    # Tupla de estados civis
    MARITAL_STATUS_CHOICES = [
        ("single", "Solteiro(a)"),
        ("married", "Casado(a)"),
        ("divorced", "Divorciado(a)"),
        ("widowed", "Viúvo(a)"),
        ("separated", "Separado(a)"),
    ]

    # Campos do modelo
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    maritalStatus = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, default='single', verbose_name="Estado civil")
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    def __str__(self):
        return self.name



class AdressInfo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="addresses")
    street = models.CharField(max_length=30)
    number = models.IntegerField()
    complement = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipCode = models.IntegerField()

    def __str__(self):
        return f"{self.street}, {self.number}"
