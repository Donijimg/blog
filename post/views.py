from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
  posts = Post.objects.all()
  for obj in posts:
    print(obj.titulo)
  return HttpResponse ("lista de posts")

def storage(request, titulo, cuerpo):
  post = Post(titulo=titulo, cuerpo=cuerpo)
  post.save()
  return HttpResponse ("guardamos los datos")
  
def consultar(requets,id):
  post= Post.objects.get(id=id)
  print (post)
  return HttpResponse (f"titulo: {post.titulo}, cuerpo:{post.cuerpo}, fecha: {post.fecha}")

def modificar(request, titulo,id):
  post=Post.objects.get(id=id)
  post.titulo=titulo
  post.save()
  return HttpResponse("post actualizado")

def eliminar(request,id):
  post=Post.objects.get(id=id)
  post.delete()
  return HttpResponse("post eliminado")



