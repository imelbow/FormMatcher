import pytest
from src.common.validators import FieldValidator

validator = FieldValidator()


@pytest.mark.parametrize("email,expected", [
    ("test@example.com", True),
    ("invalid.email", False),
    ("test@test@.com", False),
    ("test.email@domain.com", True),
])
def test_validate_email(email, expected):
    assert validator.validate_email(email) == expected


@pytest.mark.parametrize("phone,expected", [
    ("+7 999 999 99 99", True),
    ("7 999 999 99 99", True),
    ("+79999999999", True),
    ("+1 234 567 8900", True),
    ("+44 7911 123456", True),
    ("+49 170 1234567", True),
    ("+7 9999999999", True),
    ("+7 abc def gh ij", False),
    ("invalid", False),
])
def test_validate_phone(phone, expected):
    assert validator.validate_phone(phone) == expected


@pytest.mark.parametrize("date,expected", [
    ("01.01.2024", True),
    ("2024-01-01", True),
    ("01/01/2024", False),
    ("invalid", False),
])
def test_validate_date(date, expected):
    assert validator.validate_date(date) == expected
