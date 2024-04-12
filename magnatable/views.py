from django.shortcuts import render
from .models import QRQC

def home(request):
    quality_issues = QRQC.objects.exclude(general_status='Green')
    completed_quality_issues = QRQC.objects.filter(general_status='Green')
    context={
        'completed_issues':completed_quality_issues,
        'quality_issues': quality_issues,
    }
    print(completed_quality_issues)
    return render(request, 'qrqc_home.html', context)
