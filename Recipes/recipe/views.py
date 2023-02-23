from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Recipe
from .serializers import RecipeSerializer


class RecipeView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RecipeSerializer

    def get_queryset(self):
        recipes = self.request.user.recipes.all()
        return recipes

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
