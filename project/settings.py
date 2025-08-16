import flask, os
from flask import request, redirect, url_for
from flask_login import current_user

project = flask.Flask(
    import_name = "project",
    template_folder = 'templates',
    instance_path = os.path.abspath(os.path.join(__file__, '..', 'instance')),
    static_url_path= '/static_base'
)

@project.before_request
def check_auth():
    if request.endpoint:
        if 'static' in request.endpoint:
            return
    else:
        return

    public_paths = ['/', '/login', '/registration']
    if not current_user.is_authenticated and request.path not in public_paths:
        return redirect(url_for('core.render_home'))