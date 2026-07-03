import abc
from typing import List, Dict

class BaseScraper(abc.ABC):
    """
    Abstract base class for all job scrapers.
    """
    
    @abc.abstractmethod
    def fetch_jobs(self) -> List[Dict]:
        """
        Fetch jobs from the source and return a list of dictionaries.
        Each dictionary should roughly match the Job model schema.
        """
        pass

    def clean_title(self, title: str) -> str:
        return title.strip() if title else ""

    def generate_job_id(self, source_prefix: str, company: str, title: str) -> str:
        import hashlib
        unique_string = f"{source_prefix}_{company}_{title}".lower().strip()
        return f"{source_prefix}_{hashlib.md5(unique_string.encode()).hexdigest()[:10]}"
