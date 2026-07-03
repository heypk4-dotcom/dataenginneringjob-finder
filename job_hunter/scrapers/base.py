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
