
def test_login(app):
    app.session.login(username='administrator', password='3911')
    assert app.session.is_logged_in_as("administrator")