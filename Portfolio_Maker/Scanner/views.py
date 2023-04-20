from django.shortcuts import render,HttpResponse
#from rake_nltk import Rake
# Create your views here.
def scanner_page(request):
    return render(request,'Scanner.html')

def keyword(request):
    if request.method=='POST':
      r = Rake()
      text='''BM Coder, a software development company located in Ahmedabad, is seeking motivated and enthusiastic individuals for our internship program. As an intern, you will work alongside our experienced developers and gain valuable hands-on experience in software development.''' 
      r.extract_keywords_from_text(text)
      print(r.get_ranked_phrases_with_scores())
      return HttpResponse("hi")
    else:
        return render(request,'Scan_Keyword.html')

def rate(request):
    return render(request,'Scan_Rate.html')