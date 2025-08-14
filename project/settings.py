import flask, os
from flask import request, redirect, url_for
from flask_login import current_user

project = flask.Flask(
    import_name = "project",
    template_folder = 'templates',
    instance_path = os.path.abspath(os.path.join(__file__, '..', 'instance')),
    static_url_path= '/static_base'
)


PATH = os.path.abspath(__file__ + "/../..")
TASK_PATH = os.path.join(PATH, "course_app/static/task_material/")
PROFILE_PATH = os.path.join(PATH, "login_app/static/profile/")

@project.before_request
def check_auth():
    if request.endpoint != None:
        if 'static' in request.endpoint:
            return

    public_paths = ['/', '/login', '/registration']
    if not current_user.is_authenticated and request.path not in public_paths:
        return redirect(url_for('core.render_home'))

