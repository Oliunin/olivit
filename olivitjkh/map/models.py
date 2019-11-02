from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    lic_num = models.IntegerField(max_length=8,db_column='lic_num')
    lic_date = models.DateField(db_column='lic_date')
    lic_status = models.CharField(max_length=20,db_column='lic_status')
    lic_entry_date = models.DateTimeField(db_column='lic_entry_date')
    comp_addr = models.CharField(max_length=100,db_column='comp_addr')
    comp_fias_code = models.CharField(max_length=36,db_column='comp_fias_code')
    comp_name = models.CharField(max_length=264, db_column='comp_name')
    comp_inn = models.IntegerField(max_length=12,db_column='comp_inn')
    comp_ogrn = models.IntegerField(max_length=13,db_column='comp_ogrn')
    comp_house_count = models.IntegerField(db_column='comp_house_count')
    timestamp = models.DateTimeField(blank=True,null=True,auto_now=True) #Вот тут вопросики: или пустой/или auto_now проверить как работает

    def __str__(self):
        return self.comp_name

class House(models.Model):
    house_addr=models.CharField(max_length=264,db_column='House_addr')
    House_fias_code=models.CharField(blank=True,null=True,max_length=36,db_column='House_fias_code')
    House_reg_inc=models.DateTimeField(blank=True,null=True,db_column='House_reg_inc')
    House_man_start=models.DateField(blank=True,null=True,db_column='House_man_start')
    House_man_end=models.DateField(blank=True,null=True,db_column='House_man_end')
    House_reg_exc=models.DateTimeField(blank=True,null=True,db_column='House_reg_exc')
    House_reg_exc_base=models.CharField(max_length=40,db_column='House_reg_exc_base')
    House_198data=models.CharField(max_length=12,db_column='House_198data')
    House_reg_pub=models.CharField(max_length=12,db_column='House_reg_pub')
    geo_lat = models.FloatField(db_column='geo_lat')
    geo_lon = models.FloatField(db_column='geo_lon')
    comp_id= models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.house_addr
