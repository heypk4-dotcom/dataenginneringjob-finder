from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from job_hunter.config.settings import settings
from job_hunter.scheduler.main_job import run_job_hunter

if __name__ == "__main__":
    print("Starting Job Hunter Scheduler...")

    # Run once immediately on startup for testing
    print("Running initial job...")
    run_job_hunter()

    # Setup scheduler
    scheduler = BlockingScheduler(timezone=pytz.timezone(settings.timezone))

    # Parse HH:MM
    hour, minute = map(int, settings.schedule_time.split(":"))

    trigger = CronTrigger(hour=hour, minute=minute)
    scheduler.add_job(run_job_hunter, trigger)

    print(
        f"Scheduler is running. Next job at {settings.schedule_time} {settings.timezone} daily."
    )
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
