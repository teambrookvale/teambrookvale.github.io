import os
import itertools
import re

ROOT_FOLDER = 'automation/tb-system-integrations-open-ai-generator'
HTML_FOLDER = f'{ROOT_FOLDER}/html'
MD_FOLDER = f'collections/_landing_system_integrations_articles'

def url_safe(s):
    return re.sub(r'\W+', '-', s).lower()

def url_safe_platform_combination(pc):
    return url_safe(pc[0] + '-' + pc[1])

md_files = os.listdir(MD_FOLDER)
md_file_names = [os.path.splitext(x)[0] for x in md_files]

html_files = os.listdir(HTML_FOLDER)
html_file_names = [os.path.splitext(x)[0] for x in html_files]

#count intesection of md_files and html_files
print(f'{len(set(md_file_names).intersection(html_file_names))} of {len(html_file_names)} md files already generated')

platforms = []
with open(f'{ROOT_FOLDER}/zapier-premier-platforms.txt', 'r') as file:
    platforms = [x.strip() for x in file.readlines()]
platform_combinations = list(itertools.product(platforms, platforms))

for html_file in html_files:
    # DEBUG ONLY
    #if 'amazon-s3-namely.html' not in file:
    #    continue

    html_file_name = os.path.splitext(html_file)[0]

    platform_combination = next(pc for pc in platform_combinations if url_safe_platform_combination(pc) == html_file_name)

    if platform_combination is None:
        raise Exception(f'No platform combination found for {html_file_name}')
    
    if platform_combination[0] == platform_combination[1]:
        continue

    #if html_file_name in md_file_names:
    #    continue

    title = ''
    body_lines = ['<div class="arttext">']
    is_capturing = False
    is_conclusion_active = False
    conclusion = ""

    # convert encoding from Windows 1252 to utf-8 if necessary
    try:
        with open(f'{HTML_FOLDER}/{html_file}', 'r', encoding='utf-8') as file:
            file.readlines()
    except UnicodeDecodeError:
        with open(f'{HTML_FOLDER}/{html_file}', 'r', encoding='cp1252') as file:
            lines = file.readlines()
        with open(f'{HTML_FOLDER}/{html_file}', 'w', encoding='utf-8') as file:
            file.writelines(lines)
    except:
        raise

    with open(f'{HTML_FOLDER}/{html_file}', 'r', encoding='utf-8') as file:
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

    file_name = os.path.basename(file.name).replace('.html', '')

    md_header_lines = f'''---
permalink: /landings/system-integrations/{url_safe(platform_combination[0])}/{url_safe(platform_combination[1])}
author: Edward Saunders
title: "{title}"
topic: System Integration
leadhead: "{conclusion_first_sentence}"
leadtext: "{conclusion_remaining}"
image: /assets/images/articles/people-sitting-near-table.webp
---
'''

    with open(f'{MD_FOLDER}/{file_name}.md', 'w', encoding='utf-8') as md_file:
        md_file.write(md_header_lines)
        md_file.writelines(body_lines)

    print(f'Wrote {file_name}')