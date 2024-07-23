from django.shortcuts import render, redirect, get_object_or_404
from .models import Siswa
from .siswa import SiswaSerializer
from rest_framework import viewsets
from .forms import SiswaForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_siswa(request):
    if request.method == 'POST':
        form = SiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SiswaForm()
    return render(request, 'add_siswa.html', {'from': form})

def delete_siswa(request, id):
    siswa = get_object_or_404(siswa, id=id)
    if request.method =='POST':
        siswa.delete()
        return redirect('index')
    return render(request, 'delete_siswa.html',{'siswa': siswa})

class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer