from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from .models import Character

class CharacterListView(ListView):
    model = Character
    template_name = 'vote/character_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset

class CharacterDetailView(DetailView):
    model = Character
    template_name = 'vote/character_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj

class CharacterVoteForView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        character = Character.objects.get(pk=self.kwargs['pk'])
        character.votes_for += 1
        character.save()
        messages.success(self.request, f'Спасибо, что проголосовали за {character.name}')
        return reverse_lazy('character_detail', kwargs={'pk': character.pk})

class CharacterVoteAgainstView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        character = Character.objects.get(pk=self.kwargs['pk'])
        character.votes_against += 1
        character.save()
        messages.success(self.request, f'Спасибо, что проголосовали против {character.name}')
        return reverse_lazy('character_detail', kwargs={'pk': character.pk})

class CharacterCreateView(CreateView):
    model = Character
    template_name = 'vote/character_form.html'
    fields = ['name', 'description', 'image']
    success_url = reverse_lazy('character_list')

class CharacterUpdateView(UpdateView):
    model = Character
    template_name = 'vote/character_form.html'
    fields = ['name', 'description', 'image']

class CharacterDeleteView(DeleteView):
    model = Character
    template_name = 'vote/character_confirm_delete.html'
    success_url = reverse_lazy('character_list')
