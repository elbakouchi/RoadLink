from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import View
from django.db import models

from weasyprint import HTML


def html_to_pdf_view(request):
    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    html_string = render_to_string('mission/bon-mission.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # THIS IS THE PLACE WHERE I GET STUCK
        all = {
            "Name": "obj.name",
            "Email": "obj.email",
            "Address": "obj.address",
            "DOB": "obj.dob",
            "Gender": "obj.gender",
        }
        pdf = render_to_pdf('mission/bon-mission.html', all)
        return HttpResponse(pdf, content_type='application/pdf')
