# Generated by Django 3.2.9 on 2022-04-29 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='类型名称')),
            ],
            options={
                'verbose_name': '技能类型设置',
                'verbose_name_plural': '技能类型设置',
            },
        ),
        migrations.CreateModel(
            name='EmployeeSummary',
            fields=[
            ],
            options={
                'verbose_name': '个人技能统计',
                'verbose_name_plural': '个人技能统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('performance.workloadrecord',),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='类型名称')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_type', to='person.skilltype', verbose_name='技能')),
            ],
            options={
                'verbose_name': '技能设置',
                'verbose_name_plural': '技能设置',
                'ordering': ['type__name', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('skill', models.ManyToManyField(related_name='employee_skill', to='person.Skill', verbose_name='掌握技能')),
            ],
            options={
                'verbose_name': '个人技能掌握',
                'verbose_name_plural': '个人技能掌握',
            },
        ),
    ]
