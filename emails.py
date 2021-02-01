from flask import *
from flask_mail import *
app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME'] = 'tamsynsteed@gmail.com'
app.config['MAIL_PASSWORD'] = 'Marksteed01'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail= Mail(app)
@app.route('/')
def index():
    msg = Message('Hello', sender='tamsynsteed@gmail.com', recipients=['tamsynsteed@gmail.com'])
    msg.body = "Hi guys. whatsapp today"
    mail.send(msg)
    return "Mail has been send. Go check inbox"
if __name__=='__main__':
    app.run(debug=True)
