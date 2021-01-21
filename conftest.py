import pytest

from other_app.tests.factories import UserFactory, OtherAppFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def other_app():
    return OtherAppFactory()
