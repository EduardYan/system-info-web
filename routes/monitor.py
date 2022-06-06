"""
Routes to use.
"""


from flask import (
    Blueprint,
    render_template,
)
from helpers.utils import get_monitor


monitor = Blueprint('monitor', __name__)

@monitor.route('/')
def home():
    """
    Initial route
    """

    # getting the monitor
    monitor = get_monitor()

    return render_template(
        'index.html',
        monitor = monitor,
        active = 'Home'
    )


@monitor.route('/about')
def about():
    """
    Route for render the about
    page
    """

    return render_template('about.html', active = 'About')
