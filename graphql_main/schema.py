import graphene
from graphene_django import DjangoObjectType
from main.models import Category, Post


class CategoryModelType(DjangoObjectType):
    class Meta:
        model = Category


#  Работает как serializer
class PostModelType(DjangoObjectType):
    class Meta:
        model = Post

# Работает как viewset
class Query(graphene.ObjectType):
    category_model = graphene.List(CategoryModelType)
    post_model = graphene.List(PostModelType)

    def resolve_category_model(self, info):
        return Category.objects.all()
    
    def resolve_post_model(self, info):
        return Post.objects.all()
    

# Работает как routers
schema = graphene.Schema(query=Query)
