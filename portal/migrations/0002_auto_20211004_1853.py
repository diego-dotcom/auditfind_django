# Generated by Django 3.2.7 on 2021-10-04 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='seccion',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='seccion', to='portal.seccion'),
            preserve_default=False,
        ),
    ]
