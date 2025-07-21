import flask, os

project = flask.Flask(
    import_name = "project",
    template_folder = 'templates',
    instance_path = os.path.abspath(os.path.join(__file__, '..', 'instance')),
    static_url_path= '/static_base'
)