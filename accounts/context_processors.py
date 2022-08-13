import imp
from django.conf import settings
from foodOnline_main.settings import GOOGLE_API_KEY
from vendor.models import Vendor
from django.conf import settings
def get_vendor(request):
    try:
        vendor = Vendor.objects.get(user = request.user)
    except:
        vendor = None

    return dict(vendor = vendor)
    
def google_api(request):
    return {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}

