from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    post_date = job.find('span', class_='sim-posted').span.text
    if 'few' in post_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        job_skills = job.find('span', class_='srp-skills').text.strip().replace(" ", "")
        print(f'Company name: {company_name}')
        print(f'skill set: {job_skills}')
        print(' ')












# this was code for practicing with local file
# with open('index.html', 'r') as html_file:
    # content = html_file.read()
    
    # soup = BeautifulSoup(content, 'lxml')
    # buttons = soup.find_all('button')

    # for button in buttons:
    #     course_name = button.text.split()[0]
    #     course_price = button.text.split()[-1]
    #     print(f'The price for {course_name} is {course_price}')