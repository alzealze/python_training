def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group()
    app.session.logout()
