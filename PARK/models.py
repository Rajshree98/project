from django.db import models

# Create your models here.
class User(models.Model):
          DOMAIN_CHOICES=(
                    ('Clothing','Clothing'),
                    ('Toiltries','Toiltries',),
                    ('Footware','Footware',),
                    ('Study Material','Study Material',),
                    ('Grocery','Grocery',),
          )
          domain = models.CharField(max_length=2,choices=DOMAIN_CHOICES)

         

          def User(self):
                    return self.domain in (self.Clothing,self.Clothing)

