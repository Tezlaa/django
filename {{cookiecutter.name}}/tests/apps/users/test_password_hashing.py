import uuid

import pytest

from apps.users.models import User

pytestmark = [pytest.mark.django_db]


def test():
    user = User.objects.create(username=str(uuid.uuid4()))
    user.set_password("l0ve")

    user.save()  # act

    assert user.password.startswith("bcrypt")
