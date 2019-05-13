import graphene
from graphene_django import DjangoObjectType

from .models import Category
from .models import personData
from .models import Address
from .models import serviceProvider
from users.schema import UserType


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class personDataType(DjangoObjectType):
    class Meta:
        model = personData

class AddressType(DjangoObjectType):
    class Meta:
        model = Address

class serviceProviderType(DjangoObjectType):
    class Meta:
        model = serviceProvider

# ========== Queries ==========
class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()
'''
class Query(graphene.ObjectType):
    people = graphene.List(personDataType)

    def resolve_people(self, info, **kwargs):
        return personData.objects.all()
'''
# ========== Mutations ==========

class createPerson(graphene.Mutation):
    id = graphene.Int()
    user = graphene.Field(UserType)
    first_name = graphene.String()
    last_name = graphene.String()
    dt_birth = graphene.Date()
    phone = graphene.String()
    gender = graphene.String()

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        dt_birth = graphene.Date()
        phone = graphene.String()
        gender = graphene.String()

    def mutate(self, info, first_name, last_name, dt_birth, phone, gender):
        user = info.context.user or None

        person = personData(
            user = user,
            first_name = first_name, 
            last_name = last_name,
            dt_birth = dt_birth,
            phone = phone,
            gender = gender
        )
        person.save()
        
        return createPerson(
            user = person.user,
            first_name = person.first_name,
            last_name = person.last_name,
            dt_birth = person.dt_birth,
            phone = person.phone,
            gender = person.gender,
        )

class createAddress(graphene.Mutation):
    id = graphene.Int()
    user = graphene.Field(UserType)
    country = graphene.String()
    geodiv = graphene.String()
    sub_geodiv = graphene.String()
    geoplace = graphene.String()
    address = graphene.String()
    num = graphene.Int()
    postal_code = graphene.Int()

    class Arguments:
        country = graphene.String()
        geodiv = graphene.String()
        sub_geodiv = graphene.String()
        geoplace = graphene.String()
        address = graphene.String()
        num = graphene.Int()
        postal_code = graphene.Int()

    def mutate(self, info, country, geodiv, sub_geodiv, geoplace, address, num, postal_code):
        user = info.context.user or None

        address = Address(
            user = user,
            country = country,
            geodiv = geodiv,
            sub_geodiv = sub_geodiv,
            geoplace = geoplace,
            address = address,
            num = num,
            postal_code = postal_code
        )
        address.save()
        
        return createAddress(
            user = address.user,
            country = address.country,
            geodiv = address.geodiv,
            sub_geodiv = address.sub_geodiv,
            geoplace = address.geoplace,
            address = address.address,
            num = address.num,
            postal_code = address.postal_code
        )

class createServiceProvider(graphene.Mutation):
    id = graphene.Int()
    user = graphene.Field(UserType)
    category = graphene.String()
    description = graphene.String()

    class Arguments:
        category = graphene.String()
        description = graphene.String()

    def mutate(self, info, category, description):
        user = info.context.user or None

        provider = serviceProvider(
            category = category,
            description = description,
        )
        provider.save()
        
        return createServiceProvider(
            category = provider.category,
            description = provider.description,
        )

class Mutation(graphene.ObjectType):
    create_person = createPerson.Field()
    create_address = createAddress.Field()
    create_serviceProvider = createServiceProvider.Field()