from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail

class SendFormEmail(View):

    def  get(self, request):

        # Get the form data 
        full_name = request.GET.get('full_name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        # Send Email
        send_mail(
            'Subject - Django Email Testing', 
            'Hello ' + full_name + ',\n' + message, 
            'sender@example.com', # Admin
            [
                email,
            ]
        ) 

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('home') 