from django.db import models

class Area(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    firma = models.ImageField(upload_to='firmas/')
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__( self ):
        return self.nombre

class Tonner(models.Model):
    ESTADO_T = [
        ('R', 'Recargando'),
        ('L', 'Libre'),
        ('O', 'Ocupado'),
    ]


    nombre = models.CharField(max_length=50)
    cantidad = models.PositiveBigIntegerField()
    Numero_Tonner = models.CharField(max_length=20)
    Estado = models.CharField(max_length=1, choices=ESTADO_T, default='L')
    imagen = models.ImageField()
    
    def __str__(self):
        return f"{self.nombre} {self.Estado}"

    def is_recargando(self):
        return self.Estado == 'R'

    def is_libre(self):
        return self.Estado == 'L'

    def is_ocupado(self):
        return self.Estado == 'O'

class Retiro_Tonner(models.Model):
    r_tonner = models.ForeignKey(Tonner, on_delete=models.SET_NULL, null=True, blank=True)
    r_persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad_disponible = models.PositiveIntegerField(default=1)  
    cantidad_retirada = models.PositiveIntegerField()
    fecha_retiro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.r_persona} - {self.r_tonner}"
