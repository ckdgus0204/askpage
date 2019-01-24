from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Me,Ask,Comment
from .forms import MeForm, CommentForm,AskForm


# Create your views here


def base(request):
  return render(request, 'mysite/base.html')

def me_new(request):
  if request.method == 'ME':
      form = MeForm(request.ME)
      if form.is_valid():
          me = form.save()
          return redirect('mysite:me_index')
  else:
      form =MeForm()    #생성

  return render(request,'mysite/me_new.html',{
      'form':form,
  })

def me_detail(request,me_id):#read를 한다 객체를 가져온다
  me = Me.objects.get(id=me_id)
  
  return render(request,'mysite/me_detail.html', {
      "me":me,
  })

def me_index(request):
  me_all=Me.objects.all()  #모든객체 가져와
  return render(request, 'mysite/me_index.html',{
      'me_all':me_all,
  })

def me_edit(request,me_id):
  me=get_object_or_404(Me,id=me_id)  #이걸 포스트에 담겠다

  if request.method == 'ME':
      form = MeForm(request.ME,instance=me)
      if form.is_valid():
          me = form.save()
          return redirect(me)
  else:
      form =MeForm(instance=me)    #생성

  return render(request,'mysite/me_new.html',{
      'form':form,
  })
def me_delete(request,me_id):
  me = get_object_or_404(Me,id=me_id)
  me.delete()
  return redirect('mysite:me_index')

def ask_new(request):
  if request.method == 'ASK':
      form = AskForm(request.ASK)
      if form.is_valid():
          ask = form.save()
          return redirect('mysite:ask_index')
  else:
      form =AskForm()    #생성

  return render(request,'mysite/ask_new.html',{
      'form':form,
  })

def ask_detail(request,ask_id):#read를 한다 객체를 가져온다
  ask = Ask.objects.get(id=ask_id)
  comment_form=CommentForm()
  
  return render(request,'mysite/ask_detail.html', {
      "ask":ask,
      "comment_form":comment_form,
  })

def ask_index(request):
  ask_all=Ask.objects.all()  #모든객체 가져와
  return render(request, 'mysite/ask_index.html',{
      'ask_all':ask_all,
  })

def ask_edit(request,ask_id):
  ask=get_object_or_404(Ask,id=ask_id)  #이걸 포스트에 담겠다

  if request.method == 'ASK':
      form = AskForm(request.ASK,instance=ask)
      if form.is_valid():
          ask = form.save()
          return redirect(ask)
  else:
      form =AskForm(instance=ask)    #생성

  return render(request,'mysite/ask_new.html',{
      'form':form,
  })
def ask_delete(request,ask_id):
  ask = get_object_or_404(Ask,id=ask_id)
  ask.delete()
  return redirect('mysite:ask_index')

def add_comment_to_ask(request,ask_id):
  ask=get_object_or_404(Ask,id=ask_id)
  if request.method == "ASK":
      form = CommentForm(request.ASK)
      if form .is_valid() :
          comment = form.save(commit=False)
          comment.ask = ask
          comment.save()
  return redirect(ask)
def comment_delete(request,comment_id):
  comment = get_object_or_404(Comment, id=comment_id)
  comment.delete()
  return redirect(comment.ask)
  