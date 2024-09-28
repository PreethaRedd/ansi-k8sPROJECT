from flask import Flask, render_template
from uuid import uuid4


def create_app():
    app = Flask(
        __name__,
        template_folder='routes/templates',
    )
    app.config.from_mapping({
        'SECRET_KEY': uuid4().hex
    })

    from example.routes import content
    app.register_blueprint(content.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app