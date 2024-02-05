# facedetection/consumers.py
import json
import cv2
import mediapipe as mp
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import FacialExpression

class FacialExpressionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        self.face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.2)
        self.cap = None  # VideoCapture will be initialized when the user starts the camera

    async def disconnect(self, close_code):
        if self.cap is not None:
            self.cap.release()

    async def receive(self, text_data):
        data = json.loads(text_data)

        if data['action'] == 'start_camera':
            if self.cap is None or not self.cap.isOpened():
                self.cap = cv2.VideoCapture(0)  # Use 0 for the default camera
                await self.send(text_data=json.dumps({'status': 'Camera started'}))
                await self.process_frames()

            else:
                await self.send(text_data=json.dumps({'status': 'Camera already started'}))

        elif data['action'] == 'stop_camera':
            if self.cap is not None and self.cap.isOpened():
                self.cap.release()
                await self.send(text_data=json.dumps({'status': 'Camera stopped'}))
            else:
                await self.send(text_data=json.dumps({'status': 'Camera not started'}))

    async def process_frames(self):
        while True:
            ret, frame = self.cap.read()
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_detection.process(rgb_frame)

            if results.detections:
                for detection in results.detections:
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, _ = frame.shape
                    bbox = (
                        int(bboxC.xmin * iw),
                        int(bboxC.ymin * ih),
                        int(bboxC.width * iw),
                        int(bboxC.height * ih)
                    )

                    # Save detected facial expression to the database
                    expression = 'Happy'  # Replace with actual facial expression detection logic
                    FacialExpression.objects.create(expression=expression)

            await self.send(text_data=json.dumps({'status': 'Frame processed'}))
