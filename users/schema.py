from graphene_django import DjangoObjectType
import graphene
from django.contrib.auth import get_user_model
# from .models import Profile
#
# class ProfileType(DjangoObjectType):
#     class Meta:
#         model = Profile
#
# class Query(graphene.ObjectType):
#     profiles = graphene.List(ProfileType)
#
#     def resolve_profiles(self, info):
#         return Profile.objects.all()
#
# class CreateProfile(graphene.Mutation):
#     id = graphene.Int()


# class CreateLink(graphene.Mutation):
#     id = graphene.Int()
#     url = graphene.String()
#     description = graphene.String()
#
#     #2
#     class Arguments:
#         url = graphene.String()
#         description = graphene.String()
#
#     #3
#     def mutate(self, info, url, description):
#         link = Link(url=url, description=description)
#         link.save()
#
#         return CreateLink(
#             id=link.id,
#             url=link.url,
#             description=link.description,
#         )
#
#
# #4
# class Mutation(graphene.ObjectType):
#     create_link = CreateLink.Field()


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    me = graphene.Field(UserType)
    
    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
