from django.shortcuts import render
from django.template.loader import get_template
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import ConsultationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q


from blog.models import BlogPost

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
            ['info@elevatedwebsystems.com'],
            fail_silently=False,
        )
        data["form_is_valid"] = True
    else:
        data["form_is_valid"] = False
    return JsonResponse(data)


def consultation_form(request):
    if request.method == "POST":
        form = ConsultationForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            template = get_template("pages/consultation_email.txt")
            context = {
                'name': data["name"],
                'email': data["email"],
                'phone': data["phone"],
                "description": data["description"]
            }

            content = template.render(context)
            send_mail(
                "EWS Consultation",
                content,
                "{}<{}>".format(data["name"], data["email"]),
                ['info@elevatedwebsystems.com'],
                fail_silently=False,
            )
            messages.success(
                request, "Thank you! We will contact soon to setup your consultation!")
            return HttpResponseRedirect('/')
        else:
            form = ConsultationForm(request.POST)
    else:
        form = ConsultationForm()

    return render(request, 'pages/consultation_form.html', {'form': form})


def website_service(request):
    # blogs = BlogPost.objects.filter(
    #     Q(categories__name="Web Design") | Q(categories__name="Web Development")).distinct()[:3]
    blogs = BlogPost.objects.all()[:3]
    return render(request, "pages/services/websites.html", {"blogs": blogs})
