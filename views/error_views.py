from flask import Blueprint, render_template


error_views =Blueprint('error', __name__)

@error_views.errorhandler(404)
def  error_foun_error(error):
    return render_template('error/404.html')
