import sqlite3
import itertools
import openai
import json
import re
import time

HTML_FOLDER_NAME = 'html'
JSON_FOLDER_NAME = 'json'

conn = sqlite3.connect('open-ai-generator-sqlite.db')
conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, platform_1 TEXT, platform_2 TEXT, file_name TEXT, html TEXT, response TEXT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)')

openai.api_key = "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"

def generate_open_ai_messages(platfrom_1, platform_2):
    prompt = f'''
    Write blog post in HTML and cover the following:
    - {platfrom_1}
    - {platform_2}   
    - Integration of the two through API or SDK
    - Problems their integration solves
    - Conclusion
    '''
    messages=[{"role": "user", "content":prompt}]

    return messages

def is_generated(platform_1, platform_2):
    s12 = conn.execute(f"SELECT COUNT(*) FROM posts WHERE platform_1 = '{platform_1}' AND platform_2 = '{platform_2}'").fetchall()[0][0] > 0
    s21 = conn.execute(f"SELECT COUNT(*) FROM posts WHERE platform_1 = '{platform_2}' AND platform_2 = '{platform_1}'").fetchall()[0][0] > 0
    return s12 or s21

def insert_blog_post(platform_1, platform_2, file_name, html, response):
    conn.execute("INSERT INTO posts (platform_1, platform_2, file_name, html, response) values (?, ?, ?, ?, ?)", (platform_1, platform_2, file_name, html, response))
    conn.commit()

platforms = []

with open("zapier-premier-platforms.txt", "r") as file:
    platforms = [x.strip() for x in file.readlines()]

platform_permutations = list(itertools.product(platforms, platforms))

for p in platform_permutations:
   
    if p[0] == p[1] or is_generated(p[0], p[1]):
        continue

    print(f'INFO: Generating {p[0]} vs {p[1]}')

    messages = generate_open_ai_messages(p[0], p[1])

    while True:
        try:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

            file_name = re.sub(r'\W+', '-', p[0] + '-' + p[1]).lower()

            with open(f"{JSON_FOLDER_NAME}/{file_name}.json", "w") as file:
                file.write(json.dumps(response))

            with open(f"{HTML_FOLDER_NAME}/{file_name}.html", "w") as file:
                file.write(response.choices[0].message.content)

            insert_blog_post(p[0], p[1], file_name, response.choices[0].message.content, json.dumps(response))

            break
        
        except Exception as e:
            if hasattr(e, 'message'):
                print(f"ERROR: {e.message}")
            else:
                print(f"ERROR: {e}")

            time.sleep(120)

