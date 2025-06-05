from requests import get
import json

companies_name = []
job_titles = []
url = 'https://www.arbeitnow.com/api/job-board-api'
res = get(url)
if res.status_code == 200:
    content = json.loads(res.text)
    job_details = content.get('data')
    for job in job_details:
        company_name = job.get('company_name')
        companies_name.append(company_name)
        job_title = job.get('title')
        job_titles.append(job_title)


print(companies_name)
print(job_titles)
