from django.db import models
from django.contrib.auth.models import User 

class Event(models.Model):
    # Define fields to represent your events or cards, e.g., title, description, image, etc.
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')  # Example field for an image
    # Add other fields as needed

    def __str__(self):
        return self.title  # Display the event title in the admin panel

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate the comment with a user
    text = models.TextField()  # Comment text
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Reference to the event or card
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the comment was created

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event}"
