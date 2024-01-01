from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

# Create your models here.
class User(AbstractUser):
    #   classe qui contient les différents types de l'utilisateur
    class Types(models.TextChoices):
        #   TYPE = 'TYPE STOCKE EN BDD', 'Type affiché à la selection du choix'
        ADMIN = 'ADMIN', 'Admin'
        EDUCATEUR = 'EDUCATEUR', 'Educateur'
        PSYCHOLOGUQE = 'PSYCHOLOGUE', 'Psychologue'
        UTILISATEUR = 'UTILISATEUR', 'Utilisateur'
    
    #   Par défaut si le type n'est pas spécifié c'est un Utilisateur de base
    type = models.CharField(max_length=50, choices=Types.choices, default=Types.UTILISATEUR)


#   model managers, pour retourner seulement les instances de leur types quand on fait des query
class EducateurManager(models.Manager):
    def get_queryset(self):
        return super(EducateurManager, self).get_queryset().filter(type=User.Types.EDUCATEUR)
    
class PsychologueManager(models.Manager):
    def get_queryset(self):
        return super(PsychologueManager, self).get_queryset().filter(type=User.Types.PSYCHOLOGUQE)
    
class AdminManager(models.Manager):
    def get_queryset(self):
        return super(AdminManager, self).get_queryset().filter(type=User.Types.ADMIN)
    
class UtilisateurManager(models.Manager):
    def get_queryset(self):
        return super(UtilisateurManager, self).get_queryset().filter(type=User.Types.UTILISATEUR)


#   proxy models pour chaque type
class Educateur(User):
    #   utiliste son propre manager pour afficher les résultat des query
    objects = EducateurManager()
    class Meta:
        proxy = True
    #   override la méthode d'enregistrement de l'utilisateur
    def save(self, *args, **kwargs):
        #   si l'utilisateur n'existe pas (n'a pas de primary key)
        if not self.pk:
            self.type = User.Types.EDUCATEUR
        # to fix password not hashing
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args,**kwargs)
        # Ajouter a son propre groupe pour les permission
        educateur_group = Group.objects.get(name='educateur') 
        educateur_group.user_set.add(self)
        

class Psychologue(User):
    objects = PsychologueManager()
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PSYCHOLOGUQE
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args,**kwargs)
        psychologue_group = Group.objects.get(name='psychologue') 
        psychologue_group.user_set.add(self)
        

class Utilisateur(User):
    objects = UtilisateurManager()
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.UTILISATEUR
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args,**kwargs)
        utilisateur_group = Group.objects.get(name='utilisateur') 
        utilisateur_group.user_set.add(self)
        return 

class Admin(User):
    objects = AdminManager()
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.ADMIN
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        return super().save(*args,**kwargs)


class Cours(models.Model):
    prof = models.ForeignKey(Educateur, on_delete=models.CASCADE, related_name='prof_du_cours')
    titre = models.CharField(max_length=50)
    contenu = models.TextField()

class Rapport(models.Model):
    psy = models.ForeignKey(Psychologue, on_delete=models.CASCADE, related_name='psy_du_raport')
    etudiant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='etudiant_du_rapport')
    contenu = models.TextField()





