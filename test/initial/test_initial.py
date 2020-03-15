import pytest

def test_login_status_code(response_login_view):
    assert response_login_view.status_code == 200

def test_logout_status_code(response_logout_view):
    assert response_logout_view.status_code == 302

def test_login_template(response_login_view):
    template_names = [template.name for template in response_login_view.templates]
    assert "initial/login.html" in template_names
    assert "base.html" in template_names