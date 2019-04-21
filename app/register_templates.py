"""Register HTML templates on specific urls.
"""

from flask import render_template, url_for

def register_api_overview(flask_app):
    """Register an overview page of all available API versions.
    """

    registered_blueprints = [api_version for api_version in flask_app.iter_blueprints()
                             if api_version.url_prefix is not None]

    @flask_app.route('/')
    def api_overview(api_versions=registered_blueprints):
        """Register the API overview page on '/'.
        """
        url_for('static', filename='api_overview_style.css')
        return render_template('api_overview.html', api_versions=api_versions)
    