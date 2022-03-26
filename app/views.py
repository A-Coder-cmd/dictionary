from django.shortcuts import render ,HttpResponse
import requests

# Create your views here.
def home(request):

    return render(request,'home.html')

def result(request):
    djtext = request.GET.get('text','default') # geting the text from form 
    
    if djtext == 'default':
        return HttpResponse("Oops! it's like you haven't given the word ")

    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + djtext.lower()
    response = requests.get(url).json() 
    result = response[0]

    # varibale of data from response.
    word = result["word"]
    meanings = result["meanings"][0]
    POS = meanings["partOfSpeech"]
    defination = meanings["definitions"][0]["definition"]
    example = meanings["definitions"][0]["example"]
    pronounciation = result["phonetics"][0]["audio"]

    context = {
        'word':word,
        'POS':POS,
        'definition':defination,
        'example':example,
        'pronounciation':pronounciation,
    }

    return render(request,'result.html',context)