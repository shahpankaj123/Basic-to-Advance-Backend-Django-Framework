from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from unittest import result



def pdf_conveter(templates_src,content={}):
    template=get_template(templates_src)
    html=template.render(content)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("cp1252")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None