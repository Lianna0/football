from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=40, unique=True)
    country = models.CharField(max_length=40)
    club = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(default=20)

    POSITION_CHOICES = (
        ('LB', 'Left back'),
        ('RB', 'Right back'),
        ('CB', 'Center back'),
        ('GK', 'Goalkeeper'),
        ('DM', 'Defensive midfielder'),
        ('CM', 'Central midfielder'),
        ('LW', 'Left wing'),
        ('RW', 'Right wing'),
        ('STR', 'Striker')
    )

    position = models.CharField(max_length=4, choices=POSITION_CHOICES)

    FOOT_CHOICES = (
        ('both-footed', 'both-footed'),
        ('left', 'left'),
        ('right', 'right')
    )

    foot = models.CharField(max_length=15, choices=FOOT_CHOICES)

    def __str__(self):
        return f"{self.id} {self.name}"

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'


class Club(models.Model):
    name = models.CharField(max_length=40, unique=True)

    LEAGUE_CHOICES = (
        ('Premier League', 'Premier League'),
        ('Bundesliga', 'Bundesliga'),
        ('La Liga', 'La Liga'),
        ('Serie A', 'Serie A'),
        ('Ligue 1', 'Ligue 1')

    )

    league = models.CharField(max_length=20, choices=LEAGUE_CHOICES)
    stadium = models.CharField(max_length=100)
    stadium_image = models.ImageField('Stadium Image', upload_to='media/')

    def __str__(self):
        return f"{self.id} {self.name}"


    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'