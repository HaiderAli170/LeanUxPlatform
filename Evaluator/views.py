from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import ForwardedData
from .models import EmotionData
from Evaluator.models import Notification
from MyAdmin.models import User
from django.shortcuts import render
import cv2
from django.contrib.auth.decorators import login_required
import math
import mediapipe as mp
from django.http import JsonResponse

import cv2

from django.http import HttpResponse
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .models import EmotionData
from django.conf import settings
import os

def generate_pdf_report(request):
    if request.method == "POST":
        project_id = request.POST.get("project_id", "34")
    emotion_data = EmotionData.objects.filter(projectid=project_id)
    static_image_path = 'static/images/emotions.PNG'

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="project_{project_id}_report.pdf"'
    width, height = letter
    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica-Bold", 12)
    p.drawString(250, 780, "LEAN UX PLATFORM")
    p.setFont("Helvetica", 10)
    p.drawString(50, 770, "UX Evaluator: Haider Ali")
    p.drawString(50, 760, "Project Name: Cust Project")
    # Heatmap Introduction and Explanation
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, 730, "Summary:")
    p.setFont("Helvetica", 9)
    text = p.beginText(50, 710)
    text.textLines("""
        
        A bar chart for face emotion detection quantifies and compares the occurrence of emotions like happiness,
        sadness, and anger by representing each with a distinct bar. The height of each bar reflects the frequency
        or intensity of the detected emotion, offering a clear visual comparison. This chart effectively summarize
        emotional responses from facial analysis in a concise and interpretable manner.
        
        In the context of UI (User Interface) design, emotions play a critical role in enhancing user experience
        by influencing perceptions, interactions, and satisfaction with the product. A well-designed UI
        anticipates and respond to users' emotional states, using visual cues, feedback mechanisms, and interactive
        elements to evoke positive emotions,such as happiness and trust, while minimizing frustration and confusion.
        Understanding and designing for emotions in UI can lead to more engaging, intuitive, and user-friendly applications
    """)
    p.drawText(text)
    # Adjust starting y-position as needed 
    p.drawImage(static_image_path, 30, 90, width=550, height=200)
    for data in emotion_data:
        image_path = data.get_chart_image()
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, 590, "Analysis")
        # Add text
        p.setFont("Helvetica", 10)
       
       
        p.drawString(50, 580, f"Website Name: {data.website_name}")
       
        p.drawString(50, 570, f"Website URL: {data.website_url}")
       
        p.drawString(50, 560, f"Description: {data.description}")
        p.drawString(230, 400, "Emotions Data of User InterFace  ")
         # Extra space before image
        p.drawImage(image_path, 50, 300, width=550, height=200)
      

        # Handle image
        image_path = data.get_chart_image()
      
        if not os.path.isabs(image_path):
            p.drawImage(image_path, 30, 510 - 20, width=5, height=5)
            image_path = os.path.join(settings.MEDIA_ROOT, image_path.lstrip('/'))
            

        if os.path.exists(image_path):
            print(f"Attempting to draw image at path: {image_path}")  # Console log for debugging


            p.drawImage(image_path, 30, 400, width=5, height=5)  # Adjust size/location as needed
            y_position -= 210  # Adjust space for next text block

    p.save()
    return response


def Dashboard(request):
    if request.user.is_anonymous:
        return redirect("/evaluator")
    return render(request,'dashboard.html')

def generate_pdf(request):
    if request.method == "POST":
        project_id = request.POST.get("project_id", "34")
    emotion_data = EmotionData.objects.filter(projectid=project_id)
    static_image_path = 'static/images/heatmap.PNG'

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="project_{project_id}_report.pdf"'
    width, height = letter
    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica-Bold", 12)
    p.drawString(250, 780, "LEAN UX PLATFORM")
    p.setFont("Helvetica", 10)
    p.drawString(50, 770, "UX Evaluator: Haider Ali")
    p.drawString(50, 760, "Project Name: Cust Project")
    # Heatmap Introduction and Explanation
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, 730, "Summary:")
    p.setFont("Helvetica", 9)
    text = p.beginText(50, 710)
    text.textLines("""
        A heatmap is a graphical representation of data where values are depicted by color. 
        It provides insights into the user behavior and helps in understanding how users interact with the UX elements.
        
        In UX evaluation, heatmaps play a crucial role in identifying areas of interest and user focus on a screen.
        They are particularly useful in assessing user interaction patterns and visual engagement.

        The heatmap used in this evaluation is generated from real-time user interaction data captured during the UX testing phase.
        It visually represents areas where users have spent most of their time and interacted the most, 
        indicating key focal points and elements that draw user attention.

        This real-time data is valuable in understanding user preferences, improving UX design, 
        and making data-driven decisions for enhancing user experience.
    """)
    p.drawText(text)
    # Adjust starting y-position as needed 
    p.drawImage(static_image_path, 30, 200, width=550, height=240)
    for data in emotion_data:
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, 560, "Heatmap Data Summary:")
        # Add text
        p.setFont("Helvetica", 10)
       
       
        p.drawString(50, 540, f"Red: High intensity")
       
        p.drawString(50, 530, f"Blue: Medium intensity")
       
        p.drawString(50, 520, f"Green: Low intensity")
        p.drawString(50, 510, "Dull colors: Areas to ignore ")
        p.setFont("Helvetica-Bold", 12)
        p.drawString(230, 490, "Heat Map in Web Analysis")
         # Extra space before image
      

        # Handle image
        image_path = data.get_chart_image()
      
        if not os.path.isabs(image_path):
            p.drawImage(image_path, 30, 510 - 20, width=5, height=5)
            image_path = os.path.join(settings.MEDIA_ROOT, image_path.lstrip('/'))
            

        if os.path.exists(image_path):
            print(f"Attempting to draw image at path: {image_path}")  # Console log for debugging


            p.drawImage(image_path, 30, 400, width=5, height=5)  # Adjust size/location as needed
            y_position -= 210  # Adjust space for next text block

    p.save()
    return response

# def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    p = canvas.Canvas(response)

    # Header and User Information
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, 800, "Lean UX Platform Evaluation")
    p.setFont("Helvetica", 10)
    p.drawString(100, 780, "UX Evaluator: Haider Ali")
    p.drawString(100, 760, "Project Name: Cust Project")
    # Heatmap Introduction and Explanation
    p.drawString(100, 730, "Heatmap Introduction:")
    p.setFont("Helvetica", 9)
    text = p.beginText(100, 710)
    text.textLines("""
        A heatmap is a graphical representation of data where values are depicted by color. 
        It provides insights into the user behavior and helps in understanding how users interact with the UX elements.
        
        In UX evaluation, heatmaps play a crucial role in identifying areas of interest and user focus on a screen.
        They are particularly useful in assessing user interaction patterns and visual engagement.

        The heatmap used in this evaluation is generated from real-time user interaction data captured during the UX testing phase.
        It visually represents areas where users have spent most of their time and interacted the most, 
        indicating key focal points and elements that draw user attention.

        This real-time data is valuable in understanding user preferences, improving UX design, 
        and making data-driven decisions for enhancing user experience.
    """)
    p.drawText(text)

    # Dummy heatmap data (customize this part with your logic)
    p.setFont("Helvetica-Bold", 10)
    p.drawString(100, 550, "Heatmap Data Summary:")
    p.setFont("Helvetica", 9)
    p.drawString(100, 530, "Red: High intensity")
    p.drawString(100, 510, "Blue: Medium intensity")
    p.drawString(100, 490, "Green: Low intensity")
    p.drawString(100, 470, "Dull colors: Areas to ignore")
    p.drawString(100, 460, "Cust University Website Heat Map")
    link_text = "kindly click Here to see Video "
    p.drawString(100, 450, link_text)  # Draw the link text
    
    # Define the URL you want to link to
    # url = "http://127.0.0.1:8000/evaluator/startProject/"
    
    # Get the text width for positioning
    # text_width = p.stringWidth(link_text, "Helvetica", 9)
    
    # Add a URL link over the text
    # The rectangle area is (x, y, x + width, y + height)
    # p.linkURL(url, (100, 440, 100 + text_width, 460), relative=1)

    image_path = os.path.join(settings.BASE_DIR, 'static/images/heatmap.png')
    p.drawImage(image_path, 50, 90, width=550, height=200)
    p.showPage()
    p.save()

    return response
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect

def send_email(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        evaluator_name = request.POST.get('evaluator_name')
        website_name = request.POST.get('website_name')
        report_message = request.POST.get('report_message')
        
        # Construct the email body
        email_body = f"""
        New UI Report Submission
        Project Name: {project_name}
        Evaluator Name: {evaluator_name}
        Website Name: {website_name}
        Report Message: {report_message}
        """
        
        # Send the email
        send_mail(
            'UI Report Submission',
            email_body,
            'haiderium@gmail.com', # Your email
            ['haiderium@gmail.com'], # Recipient's email
            fail_silently=False,
        )
        
        # Redirect or respond after sending the email
        return redirect('success_url_name')  # Redirect to a new URL
        # or
        # return HttpResponse('Email sent successfully.')  # Send a simple response
    else:
        # If not a POST request, redirect to the form or show an error
        return HttpResponse('Invalid request', status=400)


def reportSelection(request):
    return render(request,'selectionReport.html')
def reportdetailform(request):
    return render(request,'heuristicForm.html')
def evaluatorLogin(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user= authenticate(request,username=username, password=password )
        if user is not None:
            login(request,user)
            return redirect('/evaluator/dashboard')
        else:
            messages.error(request, 'Invalid Credentials!!')
            messages.error(request, 'Please check your username or password')
            return render(request,'evaluatorLogin.html')
    return render(request,'evaluatorLogin.html')

def GazeData(request):
    return render(request, 'gazedata.html')
    
def logoutUser(request):
    logout(request)
    return render(request,'evaluatorLogin.html')


def showprofile(request):
    return render(request, 'user.html')

def showProject(request):
    return render(request, 'forwarded_request.html')
def feedback(request):
    return render(request, 'feedback.html')
def cloud(request):
    return render(request, 'cloud.html')
def StartProject(request):
    return render(request,'gazeData.html')


def view_forwarded_request(request):
    # Assuming you have user authentication and evaluator is the logged-in user
    evaluator = request.user
    forwarded_requests = ForwardedData.objects.filter(assigned_evaluator=evaluator)

    return render(request, 'newProject.html', {'forwarded_requests': forwarded_requests})


def view_notifications(request):
    # Retrieve notifications for the current user
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'notifications.html', {'notifications': notifications})




















from django.views.decorators.csrf import csrf_exempt # used for views that receive data from external sources, such as POST requests from webhooks.
from . tasks import process_gaze_data # Importing the Celery task responsible for processing gaze data asynchronously.
from . models import GazeData 
import matplotlib.pyplot as plt  # creating visualizations, particularly heatmaps.
import seaborn as sns # It enhances the aesthetics and readability of Matplotlib plots.
import pandas as pd #convert database query results to a DataFrame.
from io import BytesIO #to create an in-memory binary stream for storing the heatmap image.
import base64 # for encoding the heatmap image.

def generate_heatmap(request):
    # Retrieve data from the GazeData model
    gaze_data = GazeData.objects.all()

    # Convert queryset to a DataFrame
    df = pd.DataFrame(list(gaze_data.values()))

    # If timestamp is not already in datetime format, convert it
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Create a heatmap for gaze_x
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df[['gaze_x']].transpose(), cmap='viridis', annot=True, fmt=".0f", ax=ax)
    ax.set_title('Gaze X Heatmap')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Gaze X')

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    # Encode the image as base64
    heatmap_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Render the template with the heatmap image
    return render(request, 'heatmap_template.html', {'heatmap_image': heatmap_image})

@csrf_exempt
def receive_gaze_data(request):
    if request.method == 'POST':
        try:
            data = request.json()
            gaze_x = float(data.get('gaze_x'))
            gaze_y = float(data.get('gaze_y'))
            head_x = float(data.get('head_x'))
            head_y = float(data.get('head_y'))

            # Trigger the Celery task to process and save the gaze data
            process_gaze_data.delay(gaze_x, gaze_y, head_x, head_y)

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Unsupported method'})
    


def view_gaze_data(request):
    gaze_data = GazeData.objects.all()
    return render(request, 'view_gaze_data.html', {'gaze_data': gaze_data})



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import EyeTrackingData  # Assuming you have a model for storing the data
from django.core.files.base import ContentFile
import base64
@csrf_exempt
@require_POST
def save_video(request):
    try:
        # Get the video data from the request
        video_data = request.POST.get('videoData')

        # Decode the base64-encoded video data
        video_content = base64.b64decode(video_data)
        print('Video Content:', video_content)

        # Create a ContentFile from the decoded data
        video_file = ContentFile(video_content)

        # Save the video file to the database using your model
        EyeTrackingData.objects.create(video_file=video_file)

        return JsonResponse({'success': True, 'message': 'Video saved successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})






from django.shortcuts import render
import cv2
from keras.models import model_from_json
import numpy as np


json_file = open("evaluator/emotiondetector.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("evaluator/emotiondetector.h5")

# Load the face cascade
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

# Labels for emotions
labels = {0: 'angry', 1: 'happy', 2: 'sad', 3: 'surprise'}

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0




import numpy as np
from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators import gzip
from keras.models import model_from_json
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from .models import EmotionData

# Your existing code for emotion detection and webcam setup

# Global variable to store emotion data
emotion_data = {'angry': 0, 'happy': 0, 'sad': 0, 'surprise': 0}

def detect_emotion(frame):
    global emotion_data
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (p, q, r, s) in faces:
        image = gray[q:q+s, p:p+r]
        image = cv2.resize(image, (48, 48))
        img = extract_features(image)
        pred = model.predict(img)
        prediction_label = labels[pred.argmax()]

        # Update emotion data
        emotion_data[prediction_label] += 1

        cv2.rectangle(frame, (p, q), (p+r, q+s), (255, 0, 0), 2)
        cv2.putText(frame, f'Emotion: {prediction_label}', (p-10, q-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

    return frame

@gzip.gzip_page
def face_recognition(request):
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')


def generate_frames():
    webcam = cv2.VideoCapture(0)

    while True:
        success, frame = webcam.read()

        if not success:
            break

        # Perform live emotion detection
        frame = detect_emotion(frame)

        # Convert the frame to JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield the frame in a multipart response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    webcam.release()

# def generate_bar_chart(request):
#     global emotion_data

#     # Create a bar chart
#     emotions = list(emotion_data.keys())
#     counts = list(emotion_data.values())

#     plt.bar(emotions, counts)
#     plt.xlabel('Emotions')
#     plt.ylabel('Count')
#     plt.title('Emotion Detection Results')
    
#     # Save the chart to an image
#     image_stream = BytesIO()
#     plt.savefig(image_stream, format='png')
#     plt.close()

#     # Save the image to the database
#     image_data = image_stream.getvalue()
    
#     forwarded_data_instances = ForwardedData.objects.all()

#     for forwarded_data_instance in forwarded_data_instances:
#         emotion_data_instance = EmotionData(
#             website_name=forwarded_data_instance.website_name,
#             website_url=forwarded_data_instance.website_url,
#             description=forwarded_data_instance.description,
#             chart_image=image_data
#         )
#         emotion_data_instance.save()

    

#     return JsonResponse({'status': 'success'})



def show_chart(request):
    emotion_data = EmotionData.objects.all()  # Assuming you want to display the latest stored chart
    
    return render(request, 'show_chart.html', {'emotion_data': emotion_data})

def face(request, forwarded_data_id):
    # Retrieve the ForwardedData instance based on the provided ID
    forwarded_data = get_object_or_404(ForwardedData, id=forwarded_data_id)

    # Pass the website URL to the template
    context = {
        'forwarded_data_id': forwarded_data_id,
        'website_url': forwarded_data.website_url,
    }

    return render(request, 'face.html', context)

# def show_chart(request, project_id):
#     emotion_chart = get_object_or_404(EmotionData, project_id=project_id) # Assuming you want to display the latest stored chart
#     context = {'emotion_chart': emotion_chart}
#     return render(request, 'show_chart.html', context)

# Assuming you've imported necessary modules
from django.http import JsonResponse
from io import BytesIO
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
from django.http import JsonResponse

# Assuming you've imported other necessary modules

def generate_bar_chart(request):
    global emotion_data

    # Set the backend to Agg
    plt.switch_backend('Agg')

    # Retrieve the ForwardedData instance based on the provided ID
    forwarded_data_id = request.GET.get('forwarded_data_id')

    # Retrieve the ForwardedData instance based on the provided ID
    forwarded_data_instance = get_object_or_404(ForwardedData, id=forwarded_data_id)

    # Create a bar chart for the specified ForwardedData instance
    emotions = list(emotion_data.keys())
    counts = list(emotion_data.values())

    plt.bar(emotions, counts)
    plt.xlabel('Emotions')
    plt.ylabel('Count')
    plt.title('Emotion Detection Results')

    # Save the chart to an image
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Save the image to the database for the specified ForwardedData instance
    image_data = image_stream.getvalue()

    emotion_data_instance = EmotionData(
        website_name=forwarded_data_instance.website_name,
        website_url=forwarded_data_instance.website_url,
        description=forwarded_data_instance.description,
        chart_image=image_data
    )
    emotion_data_instance.save()

    return JsonResponse({'status': 'success'})


