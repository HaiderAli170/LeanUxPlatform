from django.contrib import admin
from Customer.models import Contact

from Evaluator.models import Evaluator

#Change "Requests" to the desired display name

# Rename the model in the admin panel
Contact._meta.verbose_name = "Request"
Contact._meta.verbose_name_plural = "Requests"

admin.site.register(Contact)








