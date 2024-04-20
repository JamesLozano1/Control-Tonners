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
        ('Recargando', 'Recargando'),
        ('Disponible', 'Disponible'),
        ('En Uso', 'En Uso'),
    ]


    nombre = models.CharField(max_length=50)
    cantidad = models.PositiveBigIntegerField()
    Numero_Tonner = models.CharField(max_length=20)
    Estado = models.CharField(max_length=10, choices=ESTADO_T, default='L')
    imagen = models.ImageField()
    
    def __str__(self):
        return f"{self.nombre} - {self.Estado}"

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


class Tabla_T_Toners(models.Model):
    MARCA_I = [
        ('N/A','N/A'),
        ('HP','HP'),
        ('SAMSUNG','SAMSUNG'),
        ('KYOSERA','KYOSERA'),
        ('EPSON','EPSON'),
    ]

    T_TONER = [
        ('105A','105A'),
        ('30A','30A'),
        ('83A','83A'),
        ('136A','136A'),
        ('175A','175A'),
        ('17A','17A'),
        ('19A','19A'),
        ('85A','85A'),
        ('226A','226A'),
        ('D1015','D1015'),
        ('TINTA','TINTA'),
        ('N/A','N/A'),
    ]

    oficina = models.CharField(max_length=50)
    activo = models.CharField(max_length=30)
    n_impresoras = models.PositiveIntegerField()
    referencia = models.CharField(max_length=100)
    marca = models.CharField(max_length=7, choices=MARCA_I, default='N/A')
    t_toner = models.CharField(max_length=5, choices=T_TONER, default='N/A')
    otro_toner = models.CharField(max_length=5, choices=T_TONER, default='N/A')
    cantidad_t = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.oficina} {self.marca}"
    

class Generar_Reporte(models.Model):
    nombre = models.CharField(max_length=20)
    # toners = models.ForeignKey(Tonner.)