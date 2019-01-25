from django.shortcuts import render
from core.forms import EntityForm
from core.models import Entity
from datetime import date

def index(request):

    entity = Entity(
        date_type_text=date.today(),
        date_type_date=date.today()
    )

    post_params = request.POST

    if request.method == 'POST':
        form = EntityForm(request.POST)
        if form.is_valid():
            entity = Entity(
                date_type_text=form.cleaned_data['date_type_text'],
                date_type_date=form.cleaned_data['date_type_date'],
            )

    form = EntityForm(instance=entity)

    return render(request, 'index.html', {
        'post_params': post_params,
        'form': form
    })
