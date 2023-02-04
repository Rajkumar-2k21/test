import pyrebase

config = {
     'apiKey': "AIzaSyAWSn6bz7FnBiLI2rfDsC007YRWuF2lqEw",
    'authDomain': "auth-753a0.firebaseapp.com",
    'projectId': "auth-753a0",
    'storageBucket': "auth-753a0.appspot.com",
    'messagingSenderId': "586710427740",
    'appId': "1:586710427740:web:0a9ec2988eec3c8e071e99",
    'measurementId': "G-D4HHWJ9MLB",
    "databaseURL":"https://auth-753a0-default-rtdb.firebaseio.com/"
}
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()

def login():
    mail=input("enter the mail:")
    password=input("enter the pasd:")
    user = auth.sign_in_with_email_and_password(mail,password)
