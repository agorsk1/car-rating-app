
import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    """"
    User factory for testing purposes

    default values:
    username - user1, user2 etc. (Sequence)

    !IMPORTANT
    If you will use email as username you must create extra factory for that.
    """
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f'user{n}')
