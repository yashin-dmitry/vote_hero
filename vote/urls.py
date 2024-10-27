from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
    path('<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),
    path('<int:pk>/vote/for/', views.CharacterVoteForView.as_view(), name='character_vote_for'),
    path('<int:pk>/vote/against/', views.CharacterVoteAgainstView.as_view(), name='character_vote_against'),
    path('create/', views.CharacterCreateView.as_view(), name='character_create'),
    path('<int:pk>/update/', views.CharacterUpdateView.as_view(), name='character_update'),
    path('<int:pk>/delete/', views.CharacterDeleteView.as_view(), name='character_delete'),
]

