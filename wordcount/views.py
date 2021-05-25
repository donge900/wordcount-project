from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist= fulltext.split()

    aantal = len(wordlist)

    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word]+=1
        else:
            #add to dict
            worddict[word]=1

    sortedwords=sorted(worddict.items(), key=operator.itemgetter(1),reverse=True)

    return render(  request,'count.html',
                    {'tekstinvoer':fulltext,'count':aantal,'sortedwords':sortedwords})
