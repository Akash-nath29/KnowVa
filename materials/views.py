from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Material
from .forms import MaterialUploadForm
from django.http import JsonResponse
from django.http import FileResponse

@login_required
def material_list(request):
    materials = Material.objects.all()
    return render(request, "materials/material_list.html", {"materials": materials})

@login_required
def upload_material(request):
    if request.method == "POST":
        form = MaterialUploadForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.uploaded_by = request.user
            material.save()
            return redirect("materials-list")
    else:
        form = MaterialUploadForm()
    return render(request, "materials/upload_material.html", {"form": form})

def home(request):
    materials = Material.objects.all()
    return render(request, "materials/home.html", {"materials": materials})


def material_detail(request, pk):
    material = get_object_or_404(Material, pk=pk)
    return render(request, "materials/material_detail.html", {"material": material})

def like_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.user in material.likes.all():
        material.likes.remove(request.user)
    else:
        material.likes.add(request.user)
        material.dislikes.remove(request.user)  # Remove dislike if previously disliked
    return JsonResponse({'likes': material.total_likes(), 'dislikes': material.total_dislikes()})

def dislike_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.user in material.dislikes.all():
        material.dislikes.remove(request.user)
    else:
        material.dislikes.add(request.user)
        material.likes.remove(request.user)  # Remove like if previously liked
    return JsonResponse({'likes': material.total_likes(), 'dislikes': material.total_dislikes()})