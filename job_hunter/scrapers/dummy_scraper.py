from typing import List, Dict
from datetime import datetime, timedelta
import uuid
from .base import BaseScraper
from ..config.settings import settings

class DummyScraper(BaseScraper):
    """
    A dummy scraper used for testing the end-to-end pipeline 
    without relying on actual web scraping which might fail or block.
    """
    
    def fetch_jobs(self) -> List[Dict]:
        jobs = []
        now = datetime.utcnow()
        
        # Dummy Job 1: Perfect match (Remote Data Engineer Fresher)
        jobs.append({
            "job_id": f"dummy_{uuid.uuid4().hex[:8]}",
            "company": "TechNova Data Systems",
            "title": "Junior Data Engineer",
            "location": "Remote, India",
            "remote": True,
            "internship": False,
            "experience_required": "0-1 years",
            "salary": "₹8,00,000 - ₹12,00,000 PA",
            "skills": "Python, SQL, Apache Spark, Airflow, AWS",
            "posting_date": now - timedelta(days=1),
            "apply_link": "https://example.com/apply/1",
            "full_job_description": "We are looking for a Junior Data Engineer to join our fully remote team. You will build ETL pipelines using Python and SQL. Ideal for freshers with strong SQL skills and understanding of Big Data concepts.",
            "source": "DummyScraper",
            "timestamp": now
        })
        
        # Dummy Job 2: Internship Match
        jobs.append({
            "job_id": f"dummy_{uuid.uuid4().hex[:8]}",
            "company": "AI Startup Inc",
            "title": "Data Engineering Intern",
            "location": "Remote",
            "remote": True,
            "internship": True,
            "experience_required": "Fresher",
            "salary": "₹30,000/month stipend",
            "skills": "Python, Pandas, PostgreSQL",
            "posting_date": now,
            "apply_link": "https://example.com/apply/2",
            "full_job_description": "Exciting internship opportunity for students. Work with data scientists to prepare data for ML models.",
            "source": "DummyScraper",
            "timestamp": now
        })
        
        # Dummy Job 3: Senior Role (Should be filtered out or scored low)
        jobs.append({
            "job_id": f"dummy_{uuid.uuid4().hex[:8]}",
            "company": "BigBank Corp",
            "title": "Senior Data Platform Engineer",
            "location": "Mumbai, India",
            "remote": False,
            "internship": False,
            "experience_required": "5+ years",
            "salary": "₹35,00,000 PA",
            "skills": "Scala, Spark, Kubernetes, Kafka",
            "posting_date": now - timedelta(days=2),
            "apply_link": "https://example.com/apply/3",
            "full_job_description": "Requires 5+ years of experience leading data platform teams. On-site only in Mumbai.",
            "source": "DummyScraper",
            "timestamp": now
        })
        
        return jobs[:settings.max_jobs_per_source]
