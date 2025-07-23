import flask

course_app = flask.Blueprint(
    name = "course_app",
    import_name = "course_app",
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "/static_course/"
)