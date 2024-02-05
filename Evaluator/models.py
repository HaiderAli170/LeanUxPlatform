from django.db import models
from datetime import datetime
from MyAdmin.models import User
import base64,uuid
class Evaluator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    bio = models.TextField(blank=True, null=True)
    # Add other fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class ForwardedData(models.Model):
    id = models.AutoField(primary_key=True,default=1)
    username = models.CharField(max_length=100)
    website_name = models.CharField(max_length=100)
    website_url = models.URLField()
    description = models.CharField(max_length=100,null=True)
    due_date = models.DateField(default=datetime.now)
    assigned_evaluator = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.username} - {self.website_name} - {self.due_date}"
    

class EmotionData(models.Model):
    projectid = models.AutoField(primary_key=True)
    
    website_name = models.CharField(max_length=100,null=True)
    website_url = models.URLField(null=True)
    description = models.CharField(max_length=100,null=True)
    project = models.ForeignKey(ForwardedData, on_delete=models.CASCADE,default=1)
    chart_image = models.BinaryField()

    def get_chart_image(self):
        image_data = base64.b64encode(self.chart_image).decode('utf-8')
        return f'data:image/png;base64,{image_data}'

    def __str__(self):
        return f"Emotion Chart - {self.project_id}"
    
class PieChart(models.Model):
    pie_chart_image = models.BinaryField()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    related_url = models.URLField()

    def __str__(self):
        return self.message
    
class FacialExpression(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    expression = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user_id} - {self.expression} at {self.timestamp}"




class GazeData(models.Model):
    gaze_x = models.FloatField()
    gaze_y = models.FloatField()
    head_x = models.FloatField()
    head_y = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)





class EyeTrackingData(models.Model):
    video_file = models.FileField(upload_to='videos/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'EyeTrackingData #{self.id}'
