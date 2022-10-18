from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Todo


# # Create your views here.
# class HomePageView(TemplateView):
#     # model = Todo
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super(HomePageView, self).get_context_data(**kwargs)
#         context['todo'] = Todo.objects.all()
#         return context

def index(request):
    # if request.method == 'POST':
    #     if 'add' in request.POST:
    #         title = request.POST['title']
    #         description = request.POST['description']
    #         due_date = request.POST['due_date']
    #         todo = ToDo(title=title, description=description, due_date=due_date)
    #         todo.save()
    #         return redirect("/")

    #     if 'delete' in request.POST:
    #         todo = todo.id
    #         todo.delete()
    #         return redirect("/")

    #     if 'edit' in request.POST:
    #         todo = todo.id
    #         title = request.POST['title']
    #         description = request.POST['description']
    #         due_date = request.POST['due_date']
    #         todo.save()
    #         return redirect("/")
    todo = Todo.objects.all()
    context = {
        'todo_list': todo,
        }

    return render(request, 'home.html', context)

def add(request):
    title = request.POST['title']
    todo = Todo(title=title)
    todo.save()
    return redirect("/")

def update(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = not todo.complete
    todo.save()
    return redirect("/")

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("/")
