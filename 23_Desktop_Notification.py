import time
from plyer import notification
import threading

def send_notification(title, message, timeout):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )

def notification_loop():
    while not exit_notification_thread:
        send_notification("ALERT!!!", "Take a break! It has been an hour!", 10)
        time.sleep(3600)

if __name__ == "__main__":
    exit_notification_thread = False

    notification_thread = threading.Thread(target=notification_loop)
    notification_thread.start()

    while True:
        user_input = input("Press 'q' to quit: ")
        if user_input.lower() == 'q':
            exit_notification_thread = True
            notification_thread.join()  # Wait for the notification thread to finish
            break