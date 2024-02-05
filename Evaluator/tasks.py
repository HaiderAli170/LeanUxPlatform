from celery import shared_task
from .models import GazeData

@shared_task
def process_gaze_data(gaze_x, gaze_y, head_x, head_y):
    # Create a new GazeData instance and save it to the database
    GazeData.objects.create(gaze_x=gaze_x, gaze_y=gaze_y, head_x=head_x, head_y=head_y)