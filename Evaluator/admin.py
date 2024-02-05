from django.contrib import admin
from Evaluator.models import ForwardedData,EyeTrackingData,EmotionData
# Register your models here.
admin.site.register(ForwardedData)

admin.site.register(EmotionData)
admin.site.register(EyeTrackingData)