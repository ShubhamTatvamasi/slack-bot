import slack
import os
from pathlib import Path
from dotenv import load_dotenv
# import csv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.getenv('SLACK_API_TOKEN'))

response=client.users_list()
users = response['members']

for user in users:
  if "email" in user["profile"]:
    print(user["profile"]["email"])


# slack_users_list = open('slack_users_list.csv', 'w') 
# csv_writer = csv.writer(slack_users_list)

# count = 0 
# for user in users:
#   if "email" in user["profile"]:
#     if count == 0:
#         header = user["profile"].keys()
#         csv_writer.writerow(header)
#         count += 1
#     csv_writer.writerow(user["profile"].values())
# slack_users_list.close()
