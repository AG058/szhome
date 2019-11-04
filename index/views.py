import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
# def index(request):
#     return render(request, 'index2.html')

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            data = str(file.read(), encoding='utf-8-sig')
            data = data.split('\r\n')

            info = [ '<br>'.join(d.split(',')[1:-1]) for d in data if d]
            data = [ (d.split(',')[0],d.split(',')[-1]) for d in data if d]


            Dict = {}
            idx = 0
            for i, j in data:
                Dict[i] = info[idx] + "<br><a href='" + j + "'>url</a>"
                idx += 1

            return render(request, 'index.html', {'Dict':json.dumps(Dict)})

        return redirect('/')

