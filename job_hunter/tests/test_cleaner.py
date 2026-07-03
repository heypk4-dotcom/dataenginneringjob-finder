from job_hunter.processors.data_cleaner import DataCleaner

def test_data_cleaner():
    raw_jobs = [
        {"title": "Data Engineer", "company": "  google  ", "apply_link": "http://x.com/a?utm_source=123"},
        {"title": "Data Engineer", "company": "Google", "apply_link": "http://x.com/a?utm_source=123"},
        {"title": "SWE", "company": "Meta", "apply_link": None}
    ]
    
    cleaned = DataCleaner.clean_jobs(raw_jobs)
    
    # Should remove duplicate (Google Data Engineer)
    assert len(cleaned) == 2
    
    # Check normalization
    assert cleaned[0]['company'] == "Google"
    
    # Check URL cleaning
    assert cleaned[0]['apply_link'] == "http://x.com/a"
