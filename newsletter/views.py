from django.shortcuts import render

def follow_us(request):
    
    context = {
        'page_title': 'Follow Us',  
    }
    
    return render(request, 'newsletter/follow_us.html', context)