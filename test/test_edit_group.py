from model.group import Group


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group("Б40_edit", "python_edit", "comment_edit"))
    app.session.logout()
