import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

job_data = {}
job_data["title"] = []
job_data["company"] = []
job_data["location"] = []

for i in range(1, 6):
  url = "https://www.work.ua/jobs-it-data+analyst/?page=" + str(i)
  raw_data = requests.get(url)
  parser = BeautifulSoup(raw_data.text, 'html.parser')
  jobs = parser.findAll(True, {"class" : ["card card-hover", "card-visited", "wordwrap", "job-link", "js-hot-block"]})

  for job in jobs:
    try:
      job_data["title"].append(job.select("h2")[0].get_text().strip())
      job_data["location"].append(job.select("span")[6].get_text().strip())
      job_data["company"].append(job.select("span")[0].get_text().strip())
    except:
      print("(")
print(job_data)
jobs_df = pd.DataFrame(job_data)
print(jobs_df.value_counts())
