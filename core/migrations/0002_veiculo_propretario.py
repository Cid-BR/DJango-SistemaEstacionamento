# Generated by Django 2.0.7 on 2018-07-06 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='propretario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa'),
            preserve_default=False,
        ),
    ]
