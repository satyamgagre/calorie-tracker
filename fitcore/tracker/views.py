from django.shortcuts import render, get_object_or_404, redirect
from .models import Food, Consume

def index(request):
    if request.method == "POST":
        food_consume = request.POST['food_consumed']
        consume_item = Food.objects.get(name=food_consume)
        user = request.user
        consume = Consume(user=user, food_consume=consume_item)
        consume.save()

    foods = Food.objects.all()
    consume_food = Consume.objects.filter(user=request.user)

    return render(request, 'tracker/index.html', {
        'foods': foods,
        'consume_food': consume_food
    })

def delete_consume(request, id):
    consume_food = get_object_or_404(Consume, id=id, user=request.user)
    if request.method == 'POST':
        consume_food.delete()
        return redirect('/')
    return render(request, 'tracker/delete.html', {'consume_food': consume_food})
