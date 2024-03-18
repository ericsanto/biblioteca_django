from django.db import models
from PIL import Image


class Category(models.Model):
    name = models.CharField('Nome', max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField('Autor', max_length=255)
    description = models.TextField(
        'Descrição')

    def __str__(self):
        return self.name


LANGUAGES = (
    ('PT-BR', 'PORTUGUÊS(BRASIL)'),
    ('EN-US', 'INGLÊS(ESTADOS UNIDOS)'),
    ('ES', 'ESPANHOL'),
    ('DE', 'ALEMÃO'),
    ('EN-GB', 'INGLÊS(REINO UNIDO)'),
    ('JA-JA', 'JAPONÊS'),
    ('RU',  'RUSSO'),
    ('ZH-TW', 'CHINÊS'),
)


class Book(models.Model):
    name = models.CharField('Nome', max_length=255)
    category = models.ForeignKey(
        Category, verbose_name='Categoria', on_delete=models.PROTECT)
    isbn = models.CharField('Número de identificação', max_length=255)
    publication_year = models.DateField('Ano de  publicação')
    edition = models.CharField('Edição', max_length=4)
    pages_number = models.CharField('Número de páginas', max_length=4)
    synopsis = models.TextField('Sinopse')
    language = models.CharField('Idioma',  choices=LANGUAGES, max_length=255)
    quantity = models.PositiveIntegerField('Quantidade disponível')
    author = models.ManyToManyField(Author)
    image = models.ImageField(
        verbose_name='Imagem', upload_to='imglivros/')
    image_detail = models.ImageField(
        blank=True, null=True, upload_to='img_detail_books/')
    pdf_books = models.FileField(
        'PDF', blank=True, null=True, upload_to='documents/')
    quantity_reserve = models.PositiveIntegerField(
        'Quantidade de reservas', default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)

            new_width = 250
            new_heigth = 300

            img = img.resize((new_width, new_heigth), Image.ADAPTIVE)
            img.save(self.image.path)


class History(models.Model):
    about = models.TextField('Sobre a Biblioteca', blank=True, null=True)
