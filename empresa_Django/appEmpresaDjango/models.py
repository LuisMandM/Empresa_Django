from django.db import models


# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Actualización")

    def __str__(self):
        return f"{self.nombre}({self.telefono})"

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ["-created"]


class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Actualización")

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ["-created"]


class Empleado(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidad = models.ManyToManyField(Habilidad)
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    antiguedad = models.IntegerField(verbose_name="Antiguedad", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Actualización")

    def __str__(self):
        return f"{self.nombre} --- {self.antiguedad}"

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["-created"]
