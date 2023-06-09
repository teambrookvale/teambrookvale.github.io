import re
import os

current_directory = os.getcwd()
print("Current Directory:", current_directory)

location_technologies_directory = os.path.join(current_directory, 'collections/_landing_location_technologies')
technologies_directory = os.path.join(current_directory, 'collections/_landing_technologies')
locations_directory = os.path.join(current_directory, 'collections/_landing_locations')

def check_directory_exists(d):
    if not os.path.exists(d) or not os.path.isdir(d):
        print(f'ERROR: {d} directory does not exist')
        exit()

check_directory_exists(location_technologies_directory)
check_directory_exists(technologies_directory)
check_directory_exists(locations_directory)

technologies = [
    '.NET Core',
    '.NET',
    'Android',
    'Angular',
    'ASP.NET',
    'C#',
    'C',
    'C++',
    'Django',
    'F#',
    'Flutter',
    'Go',
    'iOS',
    'Java',
    'JavaScript',
    'Laravel',
    'Node.js',
    'PHP',
    'Python',
    'React',
    'Ruby on Rails',
    'Scala',
    'Svelte',
    'Vue.js',
]

locations = [
    'Sydney',
    'Adelaide',
    'Auckland',
    'Australia',
    'Brisbane',
    'Cairns',
    'Darwin',
    'Gold Coast',
    'Melbourne',
    'New Zealand',
    'Perth',
    'Singapore',
]

def tech_lower_url_safe(tech):
    return re.sub(r'[^a-zA-Z0-9\-]', '-', tech).lower()

def loc_lower_url_safe(loc):
     return re.sub(r'\W', '-', loc).strip('-').lower()

for tech in technologies:
    file_contents = f'''---
name: {tech}
---'''
    with open(os.path.join(technologies_directory, f'{tech_lower_url_safe(tech)}.md'), 'w') as f:
        f.write(file_contents)

for loc in locations:
    file_contents = f'''---
title: Software Development and System Integration services in {loc}
name: {loc}
permalink: /landings/locations/{loc_lower_url_safe(loc)}
leadtext: We develop software products and provide digital platform engineering services in across Australia, New Zeland and Asia
list_generator: landing_list_technologies.html
---
''' + '{% include {{ page.list_generator }} %}'

    with open(os.path.join(locations_directory, f'{loc_lower_url_safe(loc)}.md'), 'w') as f:
        f.write(file_contents)

# product of technologies and locations
for tech in technologies:
    for loc in locations:
        # DEBUG ONLY
        # if tech != '.NET Core' or loc != 'Adaleide':
        #      continue 

        file_contents = f'''---
title: {tech} Development Team in {loc}
permalink: {f'/landings/locations/{loc_lower_url_safe(loc)}/developer/{tech_lower_url_safe(tech)}'}
technology: {tech}
location: {loc}
---'''

        with open(os.path.join(location_technologies_directory, f'{loc_lower_url_safe(loc)}-{tech_lower_url_safe(tech)}.md'), 'w') as f:
            f.write(file_contents)