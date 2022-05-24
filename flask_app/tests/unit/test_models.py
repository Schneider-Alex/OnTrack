from flask_app.models import event, post, time, coach


def test_new_coach():
    # GIVEN Coach class model
    #WHEN new Coach is created
    #Then check inputs are defined correctly
        
    coach_ = coach.Coach(1,'rob', 'simmons', 'rsim@highpoint.edu', 'password123'  )
    assert coach_.first_name == 'rob'
    assert coach_.last_name == 'simmons'
    assert coach_.email == 'rsim@highpoint.edu'
    assert coach_.password != 'password123'