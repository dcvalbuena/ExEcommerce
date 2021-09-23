# Generated by Django 3.2.7 on 2021-09-20 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Checkout_63530110', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('dcto', models.FloatField()),
                ('cantMinima', models.IntegerField()),
                ('pagado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='InfoEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('departamento', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkout_63530110.carritocompras')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkout_63530110.carritocompras')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkout_63530110.producto')),
            ],
        ),
    ]
