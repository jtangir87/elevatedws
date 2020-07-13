from django.shortcuts import render
from django.template.loader import get_template
from django.http import JsonResponse
from django.core.mail import send_mail
# Create your views here.


def contact_us(request):
    data = dict()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        template = get_template('pages/contact_us.txt')
        context = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        content = template.render(context)
        send_mail(
            "EWS Contact Us",
            content,
            "{}<{}>".format(name, email),
            ['office@ggrcleaners.com'],
            fail_silently=False,
        )
        data["form_is_valid"] = True
    else:
        data["form_is_valid"] = False
    return JsonResponse(data)
