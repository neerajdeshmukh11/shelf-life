# scheduler.py
import schedule
import time
from alerts import send_alerts

def run_scheduled_tasks():
    schedule.every().day.at("09:00").do(send_alerts)  # Schedule to run every day at 9 AM
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduled_tasks()
