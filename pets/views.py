from django.shortcuts import get_list_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Pet
from .forms import ContactForm
from django.core.mail import send_mail


def index_redirect(request):
    return redirect('/pets', request)


def about(request):
    return render(request, 'about.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        massage = form.cleaned_data.get('massage')

        subject = str(first_name) + " " + str(last_name) + " writes"

        massage = str(first_name) + " with the email, " + str(email) + ", sent the following message:\n\n" + str(
            massage)

        send_mail(subject, massage, email, ['step.kozbvb@gmail.com'])

        context = {'form': form}
        return render(request, 'pets_list.html', context)
    else:
        context = {'form': form}
        return render(request, 'contact.html', context)


class CatsListView(ListView):
    template_name = 'cats_list.html'
    queryset = Pet.objects.filter(Animal_kind='Cat')


class DogsListView(ListView):
    template_name = 'dogs_list.html'
    queryset = Pet.objects.filter(Animal_kind='Dog')


class PetListView(ListView):
    template_name = 'pets_list.html'
    queryset = Pet.objects.all()


class PetDetailView(DetailView):
    template_name = 'pets_detail.html'
    queryset = Pet.objects.all()

    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_list_or_404(Pet, id=id_)
