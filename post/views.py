from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Autor
# Create your views here.

def index(request):
  posts = Post.objects.all()
  autors = Autor.objects.all()
  for obj in posts:
    print(obj.titulo)
  for obj in autors:
    print(obj.nombre)
  return HttpResponse ("lista de posts")

def storage(request, titulo, cuerpo, nombre,correo):
  post = Post(titulo=titulo, cuerpo=cuerpo)
  autor = Autor(nombre=nombre, correo=correo)
  post.save()
  autor.save()
  return HttpResponse ("guardamos los datos")
  
def consultar(requets,id):
  post= Post.objects.get(id=id)
#  autor= Autor.objects.get(id=id)
  print (post)
#  print (autor)
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

def consultas (request):
  posts=Post.objects.all()
  post=Post.objects.get(id= 12)
  filtro=Post.objects.filter(titulo='titulo')
#  return HttpResponse("consultas")
  
  limite=Post.objects.all()[:20]
  return render(request, "index.html",{
    'posts':posts,
    'filtro':filtro,
    'post':post,
    'limite':limite
  })