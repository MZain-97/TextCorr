# I have Created this file.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def analyse(request):
    djtext = request.POST.get('text', 'default')
    djAnalyser = request.POST.get('djAnalyser', 'default')
    Fullcap = request.POST.get('Fullcap', 'off')
    removeline = request.POST.get('removeline', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    countchar = request.POST.get('countchar', 'off')
    if djAnalyser == "on":
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        Analysed = ""
        for char in djtext:
            if char not in punctuation:
                Analysed = Analysed + char
        parsm = {'purpose': 'Removed punctuation', 'Analyziedtext': Analysed}
        djtext = Analysed
        # return render(request, 'analyse2.html', parsm)

    if Fullcap == "on":
        Analysed = ""
        for char in djtext:
            Analysed = Analysed + char.upper()
        parsm = {'purpose': 'Captalized the words', 'Analyziedtext': Analysed}
        djtext = Analysed
        # return render(request, 'analyse2.html', parsm)

    if removeline == "on":
        Analysed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                Analysed = Analysed + char
        parsm = {'purpose': 'Remove new lines', 'Analyziedtext': Analysed}
        djtext = Analysed
    # return render(request, 'analyse2.html', parsm)
    if spaceremover == "on":
        Analysed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                Analysed = Analysed + char
        parsm = {'purpose': 'Remove Extra Spaces', 'Analyziedtext': Analysed}
    if djAnalyser != "on" and Fullcap != "on" and  removeline != "on" and spaceremover != "on":
        return HttpResponse("<h1>Go Back and Check th Error</h1>")

    return render(request, 'analyse2.html', parsm)
