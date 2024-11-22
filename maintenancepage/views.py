from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def send_email(objet, message_content , exp, dest, request):
    try:
      send_mail(objet, message_content , exp, [dest])
    #   messages.success(request, "Email envoyé avec succès !")
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'envoi de l'e-mail : {str(e)}")

def maintenancepage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        objet = "contact l'agence"

        agency_email = "contact@agence.com"

        send_email(objet=objet, message_content=message, dest=agency_email, exp=email, request=request)
    return render(request, 'maintenancepage.html')
