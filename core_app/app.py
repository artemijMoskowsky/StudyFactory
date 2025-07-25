import flask

core_app = flask.Blueprint(
    name = "core",
    import_name = "core_app",
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "core_static"
)