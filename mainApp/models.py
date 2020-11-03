from django.db import models


class Products(models.Model):
    prod_id = models.IntegerField(verbose_name='prod_id', primary_key=True)
    prod_name = models.TextField(verbose_name='prod_name')
    cat_name = models.TextField(verbose_name='cat_name')
    sub_cat_name = models.TextField(verbose_name='sub_cat_name')
    pic_name = models.TextField(verbose_name='pic_name')
    prod_description = models.TextField(verbose_name='prod_desc', default=None)
    prod_price = models.FloatField(verbose_name='prod_price', default=None)

    def __str__(self):
        return self.prod_name


class Category(models.Model):
    cat_name = models.TextField(verbose_name='cat_name')
    cat_pic_name = models.TextField(verbose_name='cat_pic_name')
    cat_ru_name = models.TextField(verbose_name='cat_ru_name', default=None)

    def __str__(self):
        return self.cat_name


class SubCategory(models.Model):
    sub_cat_name = models.TextField(verbose_name='sub_cat_name')
    cat_name = models.TextField(verbose_name='cat_name')
    sub_cat_pic_name = models.TextField(verbose_name='sub_cat_pic_name')

    def __str__(self):
        return self.sub_cat_name
