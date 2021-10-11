from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = ''.join(reversed(user_text))
    return render(request, 'reverse.html', {'usertext': user_text,
         'reversedtext': reversed_text})
