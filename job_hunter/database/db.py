import pandas as pd
import json
import os
from datetime import datetime
from .models import Job, SessionLocal, data_dir

class DatabaseManager:
    def __init__(self):
        self.csv_path = os.path.join(data_dir, 'jobs.csv')
        self.json_path = os.path.join(data_dir, 'jobs.json')
    
    def save_jobs(self, jobs_data: list[dict]):
        """
        Saves a list of job dictionaries to the database, CSV, and JSON.
        Avoids duplicates based on job_id.
        """
        if not jobs_data:
            return 0
            
        new_jobs_added = 0
        db = SessionLocal()
        try:
            for job_dict in jobs_data:
                # Check if job already exists
                existing_job = db.query(Job).filter(Job.job_id == job_dict['job_id']).first()
                if not existing_job:
                    # Insert new job
                    db_job = Job(**job_dict)
                    db.add(db_job)
                    new_jobs_added += 1
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
            
        if new_jobs_added > 0:
            self._update_csv_and_json()
            
        return new_jobs_added
        
    def _update_csv_and_json(self):
        """Dump the entire database to CSV and JSON."""
        db = SessionLocal()
        try:
            jobs = db.query(Job).all()
            
            # Convert to list of dicts
            jobs_list = []
            for j in jobs:
                j_dict = j.__dict__.copy()
                j_dict.pop('_sa_instance_state', None)
                # Convert datetime to string for JSON serialization
                for k, v in j_dict.items():
                    if isinstance(v, datetime):
                        j_dict[k] = v.isoformat()
                jobs_list.append(j_dict)
                
            # Write JSON
            with open(self.json_path, 'w', encoding='utf-8') as f:
                json.dump(jobs_list, f, indent=4, ensure_ascii=False)
                
            # Write CSV
            if jobs_list:
                df = pd.DataFrame(jobs_list)
                df.to_csv(self.csv_path, index=False)
                
        finally:
            db.close()

db_manager = DatabaseManager()
