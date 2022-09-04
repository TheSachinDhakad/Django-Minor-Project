
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
def About(request):
    return HttpResponse("this is about page")
def Contact(request):
    return HttpResponse("this is contact page")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
            return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)














# # i have created this file
# from django.http import HttpResponse
# from django.shortcuts import render
# def index(request):
#     # return HttpResponse('''<h1>sachin</h1> <a href="https://www.google.com/" target="_blank" >go to google</a>''')
#
#     return render(request,'index.html')
# def About(request):
#     return HttpResponse("this is about page")
# def Contact(request):
#     return HttpResponse("this is contact page")
# def analyze(request):
#     # return HttpResponse("this is analyze page")
#     djtext = request.POST.get('text' , 'default')
#     # print(djtext)
#     removepuc = request.POST.get('removepuc' , 'off')
#     fullcaps = request.POST.get('fullcaps' , 'off')
#     newlineremover = request.POST.get('newlineremover' , 'off')
#     extraspaceremover = request.POST.get('extraspaceremover' , 'off')
#     # print(removepuc)
#
#
#     if removepuc=='on':
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         # analyzed = djtext
#         params = {'purpose':'Remove punchtuation' , 'analyzed_text':analyzed}
#         djtext = analyzed
#         # return render(request,'analyze.html',params)
#     if fullcaps=='on':
#         analyzed = ""
#         for char in djtext:
#             analyzed = analyzed+ char.upper()
#         params = {'purpose': 'Change to upper case', 'analyzed_text': analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
#
#     if extraspaceremover == "on":
#         analyzed = ""
#         for index , char in enumerate(djtext):
#             if not(djtext[index]=="  " and djtext[index+1]=="  "):
#                 analyzed = analyzed+char
#             params = {'purpose': 'extra space remove', 'analyzed_text': analyzed}
#             djtext=analyzed
#             # return render(request, 'analyze.html', params)
#     if newlineremover=="on":
#         analyzed = ""
#         for char in djtext:
#             if char != "\n" and char!="\r":
#                 analyzed = analyzed +char
#         params = {'purpose': 'extra space remove', 'analyzed_text': analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
#     # else:
#     #     return HttpResponse("error")
#     return render(request, 'analyze.html', params)


