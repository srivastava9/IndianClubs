from django.db import models

from django.template.defaultfilters import slugify


class State(models.Model):
    name = models.CharField(max_length=255, verbose_name="State")
    slug = models.SlugField(default="state_slug")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(State, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# class League(models.Model):
#     name = models.CharField(max_length=255, verbose_name="League")

#     def __str__(self):
#         return self.name


class Club(models.Model):
    Name = models.CharField(
        max_length=200, verbose_name="Club Name")
    State = models.ForeignKey(
        to=State, on_delete=models.CASCADE, related_name="clubs")
    League = models.CharField(
        max_length=200, verbose_name="League Name")
    City = models.CharField(max_length=200, verbose_name="City")

    def __str__(self):
        return f'{self.Name}-{self.State}'

    class Meta:
        verbose_name_plural = "Clubs"
