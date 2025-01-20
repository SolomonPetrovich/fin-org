from django.db import models
import uuid


class FinancialOrganization(models.Model):
    #I know using TextField for some fields is not the best practice, but I did it for simplicity
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    first_director = models.TextField()
    board_of_directors = models.TextField()
    chairman_of_the_board = models.TextField()
    board_members = models.TextField()  
    other_executives = models.TextField()  
    director = models.TextField()
    chief_accountant = models.TextField()
    bin = models.TextField()
    address = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField()
    website = models.URLField()
    license = models.TextField()
    branches = models.TextField()  

    def __str__(self):
        return self.name
    

class FinancialOrganizationNews(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(FinancialOrganization, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField()