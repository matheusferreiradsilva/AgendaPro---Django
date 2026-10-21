from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('meuapp', '0002_agendamento_data_hora'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='agendamento',
            constraint=models.UniqueConstraint(
                fields=('profissional', 'data_hora'),
                name='unique_profissional_data_hora',
            ),
        ),
    ]
