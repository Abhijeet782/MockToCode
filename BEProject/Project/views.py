from django.shortcuts import render,HttpResponse
from Project.Process import main
import time
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.

def index(request):

    if request.method == 'POST' and request.FILES['uploadfile']:

        images = os.listdir("Media")
        if len(images) > 0:
            for file in images:
                os.remove("Media/" + file)

        myfile = request.FILES['uploadfile']
        print(myfile)
        fs = FileSystemStorage()
        #print(myfile.name,myfile)
        filename = fs.save(myfile.name, myfile)
        print(filename)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        context = {'response': 'Your file '+filename+' has been Uploaded Successfully'}
        return render(request, 'Project/index.html',context)

    return render(request,'Project/index.html')



def output(request):

    response=main.main()
    if response=='Failure':
        context = {'error': 'Your Image should be inside Square or Rectangle'}
        return render(request, 'Project/index.html',context)
    else:
        return render(request,'Project/OutputHTML/output.html')

