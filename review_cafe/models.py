from django.db import models
from datetime import datetime

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table ='cafe_reviews'

    def __str__(self):
        return self.id




# id	INT (Primary Key)	Unique identifier for each review
# user_id	INT (Foreign Key)	The customer who wrote the review
# product_id	INT (Foreign Key)	The product being reviewed
# rating	INT	Rating out of 5
# review_text	TEXT	The content of the review
# created_at	DATETIME	When the review was written