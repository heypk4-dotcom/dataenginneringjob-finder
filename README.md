# Data Engineering Job Hunter

An automated system to scrape, evaluate, and deliver Data Engineering jobs daily.

## Features
- **Scraping**: Supports extensible scrapers. Test version includes a Dummy scraper and a YCombinator HackerNews Playwright scraper.
- **LLM Processing**: Uses OpenAI to summarize job descriptions and score them against your resume.
- **Database**: Stores jobs locally in SQLite and exports to CSV and JSON.
- **Reporting**: Sends a daily HTML email report with top matches and the attached CSV.
- **Dashboard**: A Streamlit dashboard to explore jobs visually.
- **Automation**: Deployable via Docker or GitHub Actions.

## Installation

1. **Clone the repository**
2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
3. **Configure Environment**:
   Copy `.env.example` to `.env` and fill in your details:
   ```
   EMAIL=your_email@gmail.com
   APP_PASSWORD=your_app_password
   OPENAI_API_KEY=your_openai_api_key
   ```

## Running Locally

**Run the scraper pipeline immediately:**
```bash
python -m job_hunter.scheduler.main_job
```

**Run the daily scheduler (runs in foreground):**
```bash
python main.py
```

**Run the Dashboard:**
```bash
streamlit run job_hunter/dashboard/app.py
```

## Running with Docker

```bash
docker-compose up -d
```
This starts both the background scheduler (`job_hunter` service) and the Streamlit dashboard (`dashboard` service) on port 8501.

## GitHub Actions Deployment

1. Go to your GitHub repository Settings -> Secrets and Variables -> Actions.
2. Add the following repository secrets:
   - `EMAIL`
   - `APP_PASSWORD`
   - `OPENAI_API_KEY`
3. The action runs daily at 7:00 PM IST (13:30 UTC) and commits the updated data (`jobs.csv`, `jobs.json`) back to the repo.

## Architecture & Roadmap
The system uses `BaseScraper` which can be extended to support any platform using Requests, BeautifulSoup, or Playwright.
Future implementations will include full Playwright scrapers for LinkedIn, Wellfound, Internshala, and Naukri as the system scales.
