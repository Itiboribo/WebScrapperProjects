from bs4 import BeautifulSoup
import requests 
import time 
import datetime

print('Desired Location: Berlin')
desired_location = input('>') # Berlin 
print(f'City of interest {desired_location}')

def find_jobs_berlin():
    URL = 'https://www.stepstone.de/jobs/python/in-berlin?radius=30'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    source = requests.get(URL, headers=headers).text
    soup = BeautifulSoup(source,'html.parser')
    jobs = soup.find_all('article', class_='resultlist-19kpq27')
    for index, job in enumerate(jobs):
        posted_date = job.find('span', class_ = 'resultlist-w7zbt7').text
        if 'Tagen' in posted_date:
            company_name = job.find('span', class_ = 'resultlist-1va1dj8').text
            job_location = job.find('span', class_ = 'resultlist-suri3e').text
            title = job.find('div', class_ = 'resultlist-noiqwp')
            job_title = job.find('div', class_ = 'resultlist-noiqwp').text
            more_info_link = title.a['href'].replace('/','https://www.stepstone.de/')
            today = datetime.date.today()

            if desired_location in job_location:
                
                with open(f'JobPosts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name} \n")
                    f.write(f"Job Location: {job_location} \n")
                    f.write(f"Job Title: {job_title} \n")
                    f.write(f"More Description: {more_info_link} \n")
                    print(f'File Saved: {index}')
                print(f'{today} run successfully')

if __name__ == '__main__':
    while True:
        find_jobs_berlin()
        time_wait = 24
        print(f'waiting {time_wait} hours ....')
        time.sleep(time_wait * 3600)
