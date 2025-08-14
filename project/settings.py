import flask, os

project = flask.Flask(
    import_name = "project",
    template_folder = 'templates',
    instance_path = os.path.abspath(os.path.join(__file__, '..', 'instance')),
    static_url_path= '/static_base'
)

PATH = os.path.abspath(__file__ + "/../..")
TASK_PATH = os.path.join(PATH, "course_app/static/task_material/")
PROFILE_PATH = os.path.join(PATH, "login_app/static/profile/")