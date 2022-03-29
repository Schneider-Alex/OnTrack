from urllib import response
from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for, make_response, jsonify
from flask_app.models import coach, time, athlete, post, event
from flask_app.controllers import coaches, athletes, posts, events
import pdfkit  #########install at command line, similar to flask

#CREATE
@app.route('/coach/create/times')
def create_times_page():
    athletes_ = athlete.Athlete.get_athletes_by_coach_id(session['coach_id'])
    events_ = event.Event.get_all_events()
    return render_template('create_times.html', athletes = athletes_, events = events_)

@app.route('/create/new/time', methods=['POST'])
def create_new_times():
    if time.Time.validate_time(request.form):
        time.Time.create_times(request.form)
        return redirect('/dashboard')
    return redirect('/coach/create/times')

#READ
#render View time page

#UPDATE
@app.route('/time/update', methods=['POST'])
def update_time():
    if time.Time.validate_time(request.form):
        time.Time.update_time(request.form)
        print('$$$$$$', request.form)
    return redirect('/success_updated_time')

@app.route('/success_updated_time')
def success_update():
    return render_template('success_updated_time.html')

################Search  time###################
@app.route('/search/times')
def search_times():
    _events = event.Event.get_all_events()
    _athletes = athlete.Athlete.get_athletes_by_coach_id(session['coach_id'])
    # _date = time.Time.get_times_by_coach_date()
    return render_template('search_times.html', events= _events, athletes=_athletes)

@app.route('/pdf', methods=['POST'])
def pdf_():
    print(request.form['event_id'])
    if request.form['event_id'] !='':
        event_id = request.form['event_id']
        results = time.Time.get_times_by_event_id(request.form['event_id'])
        print(results)

    return redirect(f'/pdf/results/{event_id}')
    #     rendered = render_template('pdf_report.html', results = results)
    #     print(rendered)
    #     pdf = pdfkit.from_string(rendered, False, verbose=True)

    #     response = make_response(pdf)
    #     response.headers['Content-Type'] = 'application/pdf'
    #     response.headers['Content-Disposition'] = 'attachment; filename =output.pdf'

    # return response

@app.route('/pdf/results/int:id')
def make_pdf(id):
    results = time.Time.get_times_by_event_id(request.form['event_id'])
    print(results)
    return render_template('pdf_report.html', results= results)

# @app.route('/pdf/make')
#     rendered = render_template('pdf_report.html', results = results)
#     print(rendered)
#     pdf = pdfkit.from_string(rendered, False, verbose=True)

#     response = make_response(pdf)
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'attachment; filename =output.pdf'

#     return response

@app.route('/search/results', methods= ['POST'])
def search_results():

    results = time.Time.search_times_factors_coach_id(request.form)


    return jsonify(results)

    