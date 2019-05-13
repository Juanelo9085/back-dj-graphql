from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

# Query, recuperar usuario


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, first_name, last_name, email, password):
        user = get_user_model()(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

# Query, recuperar usuario


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