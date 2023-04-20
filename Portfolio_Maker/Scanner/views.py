from django.shortcuts import render,HttpResponse
from rake_nltk import Rake
import nltk

# Create your views here.
def scanner_page(request):
    return render(request,'Scanner.html')

def keyword(request):
    if request.method=='POST':
      text=request.POST["text"]
      if text=='':
          err={
             'msg':"Please provide a job description",
             'ttl':"Description requierd",
             'log':False
          }
          return render(request,'Error.html',err)
      else:
        r = Rake()
        #text='''BM Coder, a software development company located in Ahmedabad, is seeking motivated and enthusiastic individuals for our internship program. As an intern, you will work alongside our experienced developers and gain valuable hands-on experience in software development.''' 
        r.extract_keywords_from_text(text)
        key=r.get_ranked_phrases()
        return render(request,'keywords.html',{'key':key})
    else:
        return render(request,'Scan_Keyword.html')

def rate(request):
    return render(request,'Scan_Rate.html')