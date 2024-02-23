from django.db import models


class Category(models.Model):
    name = models.CharField('Nome', max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

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


class Author(models.Model):
    name = models.CharField('Autor', max_length=255)


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
    synopsis = models.CharField('Sinopse', max_length=500)
    language = models.CharField('Idioma',  choices=LANGUAGES, max_length=255)
    quantity = models.PositiveIntegerField('Quantidade disponível')
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name
