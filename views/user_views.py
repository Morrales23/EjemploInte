from flask import Blueprint, render_template

from forms.users_forms import createUserForm

user_views = Blueprint('user', __name__)

@user_views.route('/users/create/')
def create_user():
    form = createUserForm()
    return render_template('create_user.html', form=form)
