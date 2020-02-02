# Generated by Django 2.2.3 on 2019-08-24 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoobReads', '0005_auto_20190819_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='ibn',
            new_name='isbn',
        ),
        migrations.AddField(
            model_name='libro',
            name='autores',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='libro',
            name='calificacion_promedio',
            field=models.CharField(default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]