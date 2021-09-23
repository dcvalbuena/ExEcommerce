# Generated by Django 3.2.7 on 2021-09-21 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_auto_20210916_1521'),
        ('Checkout_63530110', '0003_auto_20210921_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='articulo',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.producto'),
        ),
        migrations.AlterField(
            model_name='carritocompras',
            name='cantMinima',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carritocompras',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='carritocompras',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]