from typing import List, Dict
import pandas as pd

class DataCleaner:
    @staticmethod
    def clean_jobs(jobs: List[Dict]) -> List[Dict]:
        """
        Cleans a list of job dictionaries:
        - Removes tracking parameters from URLs.
        - Normalizes company names.
        - Converts missing values to None.
        - Removes explicit duplicates based on company and title.
        """
        if not jobs:
            return []
            
        df = pd.DataFrame(jobs)
        
        # Remove duplicates
        df = df.drop_duplicates(subset=['company', 'title'], keep='first')
        
        # Normalize company names (uppercase, strip)
        if 'company' in df.columns:
            df['company'] = df['company'].astype(str).str.strip().str.title()
            
        # Clean URLs (remove tracking parameters)
        if 'apply_link' in df.columns:
            df['apply_link'] = df['apply_link'].apply(lambda x: x.split('?')[0] if isinstance(x, str) else x)
            
        # Convert NaN to None for database compatibility
        df = df.where(pd.notnull(df), None)
        
        return df.to_dict('records')
