# I Have make
from django.http import HttpResponse
from django.shortcuts import render


# pipeline views
def index(request):
   return render(request, 'index.html')
    # return HttpResponse("<h1>Hello from index</h1>")

def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))

def analyze (request):
    # Getting text
    djtext=request.GET.get('text','default')

    # check box
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspace=request.GET.get('extraspace','off')
    charcount=request.GET.get('charcount','off')

    print(djtext)
    print(removepunc)
    if removepunc == 'on':
        # analyzed=djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        analyzed=""

        for char in djtext:
            if char not in punctuations:
                analyzed=   analyzed    +   char
        param = {'purpose': 'Remove Puntuations', 'analyzed_text': analyzed}
        # analyze the text
        return render(request,'analyze.html',param)
    elif(fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
        param = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request,'analyze.html',param)
    elif(newlineremover == "on"):
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed=analyzed + char.upper()
        param = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif (extraspace == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char.upper()
        param = {'purpose': 'Extra Space remove', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    # elif (charcount == "on"):
    #     analyzed = ""
    #     count=0
    #     for  char in djtext:
    #         count=count+1
    #         analyzed = analyzed + char.upper() + count
    #     param = {'purpose': 'Extra Space remove', 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', param)



    else:
        return HttpResponse("Error")
# def capitalizedfirst(request):
#     return HttpResponse("capitalizedfirst")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremove(request):
#     return HttpResponse("spaceremove")
#
# def charcount(request):
#     return HttpResponse("charcount")

