from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAutor = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.authorUser.username

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAutor = pRat *3 + cRat
        self.save()

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автор"


class Category(models.Model):
    name = models.CharField(max_length = 255,unique = True)


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey("Author", on_delete = models.CASCADE)
    ARTICLE = 'AR'
    NEWS = 'NW'
    CATEGORY_CHOICES = (
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость')
    )
    categoryType = models.CharField(max_length=2,choices=CATEGORY_CHOICES,default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=False)
    postCategory = models.ManyToManyField(Category,through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'


    def  like(self):
      self.rating += 1
      self.save()


    def dislike(self):
      self.rating -= 1
      self.save()


    def preview(self):
      return self.text[0:123] +'...'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dataCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def  like(self):
      self.rating +=1
      self.save()

    def dislike(self):
      self.rating -= 1
      self.save()





