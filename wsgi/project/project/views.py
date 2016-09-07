from django.http import HttpResponse

# Create your views here.

def root_page (request):
    return HttpResponse ("""Home Page !!""")
