import threading
from notifications import email_notification_section


def user_contact_section(name, address, message):
    mail = name + ".\n\n" + address + ".\n\n" + message + ".\n"
    send_to = 'support@domain.com'
    thread_obj = threading.Thread(target=email_notification_section, args=[send_to, '', '', mail, 2])
    thread_obj.start()
