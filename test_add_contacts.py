# -*- coding: utf-8 -*-
from group import Contact
from application import ApplicationCont
import pytest


@pytest.fixture
def appcont(request):
    """Создаем, разрушаем, возвращаем фикстуру"""
    fixturecont = ApplicationCont()
    request.addfinalizer(fixturecont.destroycont)
    return fixturecont


def test_add_contact(appcont):
    appcont.login(username="admin", password="secret")
    appcont.create_contact(Contact(firstname="Aleksandr", lastname="Zemskov", mobile="89201234567", nickname="alze"))
    appcont.logout()
