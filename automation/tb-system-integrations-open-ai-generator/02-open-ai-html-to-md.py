import os
import random
from datetime import datetime, timedelta

for file in os.listdir('html'):
    # DEBUG ONLY
    #if 'amazon-s3-namely.html' not in file:
    #    continue

    title = ''
    body_lines = ['<div class="arttext">']
    is_capturing = False
    is_conclusion_active = False
    conclusion = ""
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 6, 6)
    with open(f'html/{file}', 'r') as file:
        for line in file.readlines():
            if '<title>' in line:
                title = line.replace('<title>', '').replace('</title>', '').replace('\n', '').strip()

            if '</body>' in line:
                is_capturing = False
            
            if is_capturing:
                body_lines.append(line)
            
            if is_conclusion_active and is_capturing:
                conclusion += line

            if '>Conclusion</h' in line:
                is_conclusion_active = True

            if '<body>' in line:
                is_capturing = True

            if '</p>' in line:
                is_conclusion_active = False

    body_lines.append('</div>')
    
    if len(title) == 0:
        print(f'ERROR: No title found for {file}')
        continue
    
    conclusion = conclusion.replace('<p>', '').replace('</p>', '').strip()

    # python find index of first instance of in string
    conclusion_sentence_end_index = conclusion.find('. ')
    
    if conclusion_sentence_end_index < 1:
        print(f'ERROR: No conclusion sentence end found for {file}')
        continue
    
    conclusion_first_sentence = conclusion[0:conclusion_sentence_end_index]
    conclusion_remaining = conclusion[conclusion_sentence_end_index + 2:]

    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)

    file_name = os.path.basename(file.name).replace('.html', '')

    md_header_lines = f'''---
aigenerated: true
permalink: /articles/aigenerated-{file_name}
boxclassname: black
author: "Edward Saunders"
topic: "System Integration"
title: "{title}"
leadhead: "{conclusion_first_sentence}"
leadtext: "{conclusion_remaining}"
image: /assets/images/articles/people-sitting-near-table.webp
date: '{random_date}'
---
'''

    with open(f'md/aigenerated-{file_name}.md', 'w', encoding='utf-8') as md_file:
        md_file.write(md_header_lines)
        md_file.writelines(body_lines)

    print(f'Wrote {file_name}')