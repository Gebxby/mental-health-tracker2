from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306315516',
        'name': 'Gabriel S.A. Fenanlampir',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
