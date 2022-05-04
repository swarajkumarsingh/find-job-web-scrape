import random
import time

import requests
from bs4 import BeautifulSoup

job_title = input(">")
job_title_reformatted = job_title.replace(' ', '+')

print('Put some skill that you are not familiar with.')
unfamiliar_skill = input(">")
unfamiliar_skill.lower()
print("Fetching results...")
e = ''


def find_jobs():
    try:
        html_text = requests.get(
            f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job_title_reformatted}&txtLocation=").text
    except Exception as e:
        return print("Network not connected")

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").span.text
        if "few" in published_date:
            skills = job.find('span', class_="srp-skills").text.replace(' ', '')
            skills = skills.lower()
            company_name = job.find('h3', class_="joblist-comp-name").text
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                n = random.randint(1, 200)
                with open(f"posts/{n}.txt", 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More info: {more_info} \n")
                print(f"File Saved: {n}")


if __name__ == "__main__":
    while True:
        find_jobs()
        print(f"Waiting for 10 minutes")
        time.sleep(10 * 60)
