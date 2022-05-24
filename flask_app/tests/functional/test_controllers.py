from flask_app.controllers import coaches, athletes, posts, events

def test_dashboard():

    flask_app = create_app('flask_test.cfg')