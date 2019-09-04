from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse(''' hello <a  href="about" >facebook</a>''')


def analyze(request):
    djtext=request.POST.get('text','default')
    c=request.POST.get('check','off')
    check_new_line=request.POST.get('check_new_line','off')
    extra_space=request.POST.get('extra_space','off')
    l=[]
    param={'punc':djtext,'sentance':l}
    if extra_space=='on':
        analyze=''
        for j,i in enumerate(djtext):

            if not (djtext[j]==' ' and djtext[j+1]==' '):
                analyze=analyze+i
        l.append('After removing extra space  ='+analyze)
        #return render(request,'analyze.html',param)


    if(check_new_line=='on'):
        analyze=''
        for i in djtext:
            if i!='\n' and i!='\r':
                analyze=analyze+i
        l.append("after removing the new line  ="+analyze)
        #param={'punc':djtext,'sentence':analyze}
        #return render(request,'analyze.html',param)

    if(c=='on'):
        analyze=''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in djtext:
            if i not in punctuations:
                analyze=analyze+i

        l.append('After removing the punctuations  ='+analyze)



    if(param):
        for i in param:
            print(param[i])
        return render(request,'analyze.html',param)
    else:
        return HttpResponse("Error NO selection made!!! ")
