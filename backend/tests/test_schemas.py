"""Preverjanje sprejemnih kriterijev validacij zahtevkov."""
import pytest
from pydantic import ValidationError

from app.schemas import BuildingCreate, RegisterRequest, UnitIn


@pytest.mark.parametrize("field", ["name", "address"])
def test_building_requires_nonempty_fields(field):
    data = {"name": "Blok A", "address": "Glavna 1"}
    data[field] = "   "
    with pytest.raises(ValidationError):
        BuildingCreate(**data)


def test_building_trims_whitespace():
    item = BuildingCreate(name="  Blok A  ", address="  Glavna 1  ")
    assert (item.name, item.address) == ("Blok A", "Glavna 1")


def test_unit_rejects_empty_label():
    with pytest.raises(ValidationError):
        UnitIn(label="  ")


def test_unit_trims_label():
    assert UnitIn(label="  Stanovanje 7 ").label == "Stanovanje 7"


def registration_data():
    return {
        "code": "TEST-KODA",
        "full_name": "Test Uporabnik",
        "email": "test@example.com",
        "password": "geslo1234",
    }


def test_registration_accepts_valid_data():
    assert RegisterRequest(**registration_data()).email == "test@example.com"


def test_registration_rejects_short_password():
    data = registration_data()
    data["password"] = "abc123"
    with pytest.raises(ValidationError):
        RegisterRequest(**data)


def test_registration_rejects_invalid_email():
    data = registration_data()
    data["email"] = "not-an-email"
    with pytest.raises(ValidationError):
        RegisterRequest(**data)


def test_registration_rejects_empty_invitation_code():
    data = registration_data()
    data["code"] = ""
    with pytest.raises(ValidationError):
        RegisterRequest(**data)
