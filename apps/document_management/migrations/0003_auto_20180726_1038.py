# Generated by Django 2.0.6 on 2018-07-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_management', '0002_auto_20180726_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='belong',
            field=models.PositiveSmallIntegerField(choices=[(1, '文档'), (2, 'Shell脚本'), (3, 'Python脚本'), (4, 'Bat脚本'), (5, 'Bat脚本')], verbose_name='隶属'),
        ),
    ]
