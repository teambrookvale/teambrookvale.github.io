import os
import random
import re
from datetime import datetime, timedelta

SOURCE_PLATFORMS_LIST = 'automation/tb-system-integrations-open-ai-generator/zapier-premier-platforms.txt'
SOURCE_MD_ARTICLES_FOLDER = 'automation/tb-system-integrations-open-ai-generator/md'

TARGET_ROOT = 'collections'
TARGET_MD_ARTICLES_FOLDER = f'{TARGET_ROOT}/_landing_system_integrations_articles'
TARGET_MD_A_FOLDER = f'{TARGET_ROOT}/_landing_system_integrations_a'
TARGET_MD_B_FOLDER = f'{TARGET_ROOT}/_landing_system_integrations_b'

# read in source platforms from SOURCE_PLATFORMS_LIST
with open(SOURCE_PLATFORMS_LIST, 'r') as file:
    source_platforms = file.readlines()

# for file in os.listdir(SOURCE_MD_ARTICLES_FOLDER):
#     with open(f'{SOURCE_MD_ARTICLES_FOLDER}/{file}', 'r', encoding='utf-8') as source_file:
#         with open(f'{TARGET_MD_ARTICLES_FOLDER}/{file}', 'w', encoding='utf-8') as target_file:
#             target_file.write(source_file.read())

for platform in source_platforms:
    platform = platform.strip()
    platform_url_safe = re.sub(r'\W+', '-', platform).lower()

    with open(f'{TARGET_MD_A_FOLDER}/{platform_url_safe}.md', 'w', encoding='utf-8') as file:
        file.write(f'''---
title: {platform} System Integration Services
name: {platform}
permalink: /landings/system-integrations/{platform_url_safe}
leadtext: We develop software products and provide digital platform engineering services in across Australia, New Zeland and Asia
list_generator: landing_list_system_integrations_b.html
---
''' + '{% include {{ page.list_generator }} %}')

    with open(f'{TARGET_MD_B_FOLDER}/{platform_url_safe}.md', 'w', encoding='utf-8') as file:
        file.write(f'---\nname: {platform}\n---\n')
