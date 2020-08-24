import yagmail
from datetime import datetime

receiver = "xxxx@gmail.com"
oauth2_file="/file-location/yagmail.json"
yag = yagmail.SMTP(receiver, oauth2_file=oauth2_file)

def send_notification(process_name=None, status=None, subject="Mail Reminder", error_string=None):
    time_now = datetime.now()
    current_time_str = time_now.strftime("%Y-%m-%d %H:%M:%S")
    message = "{}:notification: Process {} was {}".format(current_time_str, process_name, status)
    if error_string is not None:
        message = "{} with error {}".format(message, error_string)
    yag.send(to = receiver,
             subject = subject,
             contents = message,
            )