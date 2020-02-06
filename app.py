from flask import Flask, g, render_template, request, redirect, send_from_directory
import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask_mail import Mail,Message
import math
import os


app = Flask(__name__, static_folder='static')
app.config.update(
    MAIL_SERVER='smtp.zoho.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'info@technieks.in',
    MAIL_PASSWORD = os.environ['ZOHO']
)
mail = Mail(app)


@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/OneSignalSDKWorker.js')
def onesignalfirst():
    return send_from_directory(app.static_folder,request.path[1:])

@app.route('/OneSignalSDKUpdaterWorker.js')
def onesignalsecond():
    return send_from_directory(app.static_folder,request.path[1:])

@app.route('/manifest.json')
def onesignalthird():
    return send_from_directory(app.static_folder,request.path[1:])

@app.route('/')
@app.route('/index.html')
def index():
#    scope = ['https://spreadsheets.google.com/feeds']
#    credentials = ServiceAccountCredentials.from_json_keyfile_name('technieks19.json', scope)
#    gc = gspread.authorize(credentials)
#    wks = gc.open_by_key('10pB43SvGbIWX0LEGaRfkYe1XYa_bw-OvlvdUgj-66gQ').sheet1
#    sdata = wks.get_all_values()
    return render_template('index.html')
#FIX THIS
#    return render_template('index.html',data=sdata[1:])

# FIX THIS
@app.route('/technieks-run')
def technieks_run():
    return redirect("https://yepdesk.com/technieks-run-2020", code=302)

#FIX THIS

# @app.route('/events')
# def events_all():
#     try:
#         to generate past and present files manually, follow this :
#         url = 'https://graph.facebook.com/v2.8/' + 'techNIEks/events' \
#         + '?fields=id%2Cname%2Ccover%2Cstart_time%2Cdescription%2Cplace%2Cticket_uri' \
#         + '&access_token=EAAWnWNp4iZBIBAKvoZA1kmIEivqNTyjsjuq1ZAYZBfXwYdEcLJbm2NzhMLNo4OjpXUewsxphNn6297ZA8OsMnhp8PGzN1pXqdF5kJOz79xhTLZAJfnAXAADZAzUZCEwyAXiF2NhD31ZBfZCHkCZAtppPeGtbOVgeEtTyPc3yDwllzTXsh0mCab8YZA76mOnY0Dgeik5nAFw9S9rPogZDZD'
#         json1_str = requests.get(url)
#         json1_data = json.loads(json1_str.text)["data"]
#         e1 = json1_data[0:n] , where n is the no of new events
#         e2 = json1_data[:-7] , past 7 events
#         with open('present.json', 'w') as pastfile:
#             json.dump(json1_data, pastfile)
#         with open('past.json', 'r') as pastfile:
#             past = json.load(pastfile)
#         with open('present.json', 'r') as presentfile:
#             present = json.load(presentfile)
#         return render_template('events1.html', events1 = present , past = past, title="New Events")
#     except:
#         return render_template('events1.html',events1=[], title="New Events")

#FIX THIS
"""
@app.route('/events1')
def test_events():
    try:
        url = 'https://graph.facebook.com/v2.8/' + 'techNIEks/events' \
        + '?fields=id%2Cname%2Ccover%2Cstart_time%2Cdescription%2Cplace%2Cticket_uri' \
        + '&1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
        json1_str = requests.get(url)
        json1_data = json.loads(json1_str.text)["data"]
        e1 = json1_data[:-20]
        e2 = json1_data[-20:]
        return render_template('events3.html',events1=e1, events2=e2, title="All Events")
    except:
        e1 = {}
        e2 = {}
        return render_template('events3.html',events1=e1, events2=e2, title="All Events")
"""

#FIX THIS 

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')    

    
    #DONT UNCOMMENT FROM HERE --------------
"""url = 'https://graph.facebook.com/v2.12/720663717966776?fields=photos.fields(source).limit(100)&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
json1_str = requests.get(url)
jdata = json.loads(json1_str.text)["photos"]
data = jdata["data"]
while "next" in jdata["paging"].keys():
    json1_str = requests.get(jdata["paging"]["next"])
    jdata = json.loads(json1_str.text)
    data.extend(jdata["data"])
with open('images.json') as f:
    data = json.load(f)

if(year==2019):
    startFromImage = 0
    noOfImagesToBeRemoved  = 823
elif(year==2018):
    startFromImage = len(data)-823
    noOfImagesToBeRemoved  = 473
else:
    return render_template('404.html')
data = data[startFromImage:-noOfImagesToBeRemoved]
noOfImages = len(data)
imagesPerPage = 20
noOfPages = int(math.ceil(noOfImages/imagesPerPage))
if(request.args.get('page')==None):
    currentPage = 1
else:
    currentPage = int(request.args.get('page'))    
lowerLimitAtCurrentPage = (currentPage-1)*20
if(currentPage*20>noOfImages):
    upperLimitAtCurrentPage = noOfImages
else:
    upperLimitAtCurrentPage = currentPage*20
""" 


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/hackathon/')
# def hackathon():
#     return redirect('https://docs.google.com/forms/d/e/1FAIpQLSdy0PTBTJmAklzPThYgb78GlT9QzYI8oPsZ4DF8HjfyKnnTzg/viewform?usp=sf_link')

# @app.route('/marathon/')
# def marathon():
#     return redirect('https://www.payumoney.com/events/#/buyTickets/technieksmarathon18')

@app.route('/youtube/')
def youtube():
    return redirect('https://www.youtube.com/channel/UC0Ky30GAIfdtGccczVNUIqA')


# @app.route('/cyclothon/')
# def cyclathon():
#     return redirect('https://www.payumoney.com/events/#/buyTickets/cyclothon2018')

@app.route('/contactform/',  methods=['GET', 'POST'])
def contactform():
    try:
        contactName=request.form['contactName']
        contactEmail=request.form['contactEmail']
        contactSubject=request.form['contactSubject']
        contactMessage=request.form['contactMessage']
        body="Name: "+contactName+"\nEmail: "+contactEmail+"\nSubject: "+contactSubject+"\nMessage: "+contactMessage
        msg = Message(subject="Contact Form Entry",body=body, sender=(contactName,"info@technieks.in"), recipients=["techNIEks2020@gmail.com"])
        mail.send(msg)
        body1="Dear "+contactName+",\n\nThankyou you for reaching out to us, we have received the following data:\n\n"+"Name: "+contactName+"\nEmail: "+contactEmail+"\nSubject: "+contactSubject+"\nMessage: "+contactMessage+"\n\nWe will get back to you soon.\n\nRegards,\nTeam techNIEks"
        msg1 = Message(subject="Contact techNIEks",body=body1, sender=("techNIEks","info@technieks.in"), recipients=[contactEmail])
        mail.send(msg1)
        return "OK"
    except:
        return "Error"

@app.route('/live')
def live():
    try:
        return render_template("live.html")
    except:
        return "Error"


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)
