from flask import Blueprint, render_template, redirect, url_for, request
from example.forms import ExampleForm
from markupsafe import escape


bp = Blueprint('content', __name__, url_prefix='/content', template_folder='templates/content')


@bp.route('/user-input', methods=['GET', 'POST'])
def get_input():
    form = ExampleForm()

    if form.validate_on_submit():
        first_name = escape(form.first_name._value())
        last_name = escape(form.last_name._value())
        hobby = escape(form.hobby._value())
        return redirect(url_for(
            'content.display_input',
            first_name=first_name,
            last_name=last_name,
            hobby=hobby
        ))

    return render_template('get_input.html', form=form)


@bp.route('/display-input')
def display_input():
    first_name = escape(request.args.get('first_name', ''))
    last_name = escape(request.args.get('last_name', ''))
    hobby = escape(request.args.get('hobby', ''))

    return render_template('display_input.html', first_name=first_name, last_name=last_name, hobby=hobby)