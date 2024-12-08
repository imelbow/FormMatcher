def test_get_form_contact(test_client):
    response = test_client.post(
        "/get_form",
        data={
            "email": "test@example.com",
            "phone": "+7 999 999 99 99"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"template_name": "Contact form"}


def test_get_form_registration(test_client):
    response = test_client.post(
        "/get_form",
        data={
            "user_email": "test@example.com",
            "birth_date": "2024-01-01",
            "phone_number": "+7 999 999 99 99"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"template_name": "Registration"}


def test_get_form_unknown(test_client):
    response = test_client.post(
        "/get_form",
        data={
            "unknown_field": "some text"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"unknown_field": "text"}


def test_get_form_partial_match(test_client):
    response = test_client.post(
        "/get_form",
        data={
            "email": "test@example.com",
            "phone": "+7 999 999 99 99",
            "extra_field": "some text"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"template_name": "Contact form"}
