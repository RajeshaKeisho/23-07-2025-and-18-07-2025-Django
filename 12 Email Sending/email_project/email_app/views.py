from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormDataForm
def send_email(request):
    subject = 'Test Email Subject with an attachment'
    from_email = 'rajarajesha@gmail.com'
    to_email = ['pyweb.rajesha.coding@gmail.com']

    html_content = render_to_string('email_template.html', {'username': 'Rajesha'})

    email = EmailMultiAlternatives(subject, 'Text Content Here', from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    email.extra_headers['X-Mailer'] = 'Django Email'

    try:
        email.send()
        return HttpResponse("Email sent successfully.")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {str(e)}")
    

# def form_view(request):
#     if request.method == 'POST':
#         form = FormDataForm(request.POST, request.FILES)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             attachment = request.FILES['attachment']
            
#             subject = 'Form Submission Received'
#             message = "Thank you for your submission."
#             from_email = 'rajarajesha@gmail.com'
#             to_email = [email]
#             email = EmailMessage(subject, message, from_email, to_email)
#             email.attach(attachment.name, attachment.read(), attachment.content_type)

#             try:
#                 email.send()
#                 return render(request, 'success.html')
#             except Exception as e:
#                 return render(request, 'error.html', {'error': str(e)})
#     else:
#         form = FormDataForm()
#     return render(request, 'form.html', {'form': form})

def form_view(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            attachment = form.cleaned_data['attachment']

            # Prepare the email
            subject = 'Form Submission'
            message = 'Thank you for your submission!'
            from_email = 'rajarajesha@gmail.com'
            to_email = [email]

            email = EmailMessage(subject, message, from_email, to_email)
            email.attach(attachment.name, attachment.read(), attachment.content_type)  # Use attach instead of attach_file

            # Send the email
            try:
                email.send()
                return render(request, 'success.html')
            except Exception as e:
                return render(request, 'error.html', {'error_message': str(e)})
    else:
        form = FormDataForm()
    return render(request, 'form.html', {'form': form})  

