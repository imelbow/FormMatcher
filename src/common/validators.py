import re
from datetime import datetime

import phonenumbers
import validators


class FieldValidator:
    @staticmethod
    def validate_email(value: str) -> bool:
        return bool(validators.email(value))

    @staticmethod
    def validate_phone(value: str) -> bool:
        try:
            value = value.replace(" ", "")
            if value.startswith('+'):
                phone_number = phonenumbers.parse(value)
            else:
                phone_number = phonenumbers.parse(value, "RU")

            return (
                    phonenumbers.is_valid_number(phone_number) and
                    phonenumbers.number_type(phone_number) in [
                        phonenumbers.PhoneNumberType.MOBILE,
                        phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE
                    ]
            )
        except phonenumbers.NumberParseException:
            return False

    @staticmethod
    def validate_date(value: str) -> bool:
        if re.match(r'^\d{2}\.\d{2}\.\d{4}$', value):  # Format dd.mm.yyyy
            try:
                datetime.strptime(value, '%d.%m.%Y')
                return True
            except ValueError:
                return False
        elif re.match(r'^\d{4}-\d{2}-\d{2}$', value):  # Format yyyy-mm-dd
            try:
                datetime.strptime(value, '%Y-%m-%d')
                return True
            except ValueError:
                return False
        return False

    @classmethod
    def determine_field_type(cls, value: str) -> str:
        if cls.validate_email(value):
            return "email"
        if cls.validate_date(value):
            return "date"
        if cls.validate_phone(value):
            return "phone"
        return "text"
