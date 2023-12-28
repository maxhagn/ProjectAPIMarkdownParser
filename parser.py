import os

import requests

dir_name = 'version_2'
url_project = "https://api.projects.hagn.network/public/hagn/project"
url_project_stats = "https://api.projects.hagn.network/public/hagn/project/stats"
url_skill_stats = "https://api.projects.hagn.network/public/hagn/skill/stats"
url_skill = "https://api.projects.hagn.network/public/hagn/skill"

projects = sorted(requests.get(url_project).json(), key=lambda x: x.get('relevanceScore', 0), reverse=True)
skills = requests.get(url_skill).json()
project_stats = requests.get(url_project_stats).json()
skill_stats = requests.get(url_skill_stats).json()

hero_text = "# Hi there, I'm Max!"
catchy_text = "## I'm where technology meets business, transforming complex ideas into innovative solutions."
intro_text = ("I am a computer science student at the Vienna University of Technology. As a software developer, "
              "I specialize in low level programming using C and C++. I have a passion for crafting efficient and "
              "reliable code, and I enjoy tackling challenging problems that require a deep understanding of how "
              "computers work. In my free time, I like to stay up to date on the latest developments in the tech "
              "industry and expand my skillset through self-study and experimentation. I am excited to share my "
              "projects and collaborate with others on GitHub while continuing to learn and grow as a developer.")
website_checkout_text = "<small>**🚀 Explore my digital universe: [maximilian.hagn.network](https://maximilian.hagn.network)!</small>**"
stats_text = f"""
# Statistics
## Projects
- Total Project Engagements: {project_stats['projectCount']}
- APIs and Websites: {project_stats['totalWebsites']}
- Client Collaborations: {project_stats['clientCount']}
- Code Repositories Managed: {project_stats['totalRepositories']}
- Cumulative Workdays: {project_stats['totalWorkdays']}

## Skills
- Programming Languages: {skill_stats['languageCount']}
- Technologies: {skill_stats['technologyCount']}
- Soft Skills: {skill_stats['softSkillCount']}
- Total Skills: {skill_stats['skillCount']}
"""

os.makedirs(dir_name, exist_ok=True)


def snake_case_to_normal(snake_str):
    words = snake_str.lower().split('_')
    return ' '.join(word.capitalize() for word in words)


with open(f'{dir_name}/maxhagn.md', 'w') as file:
    file.write(hero_text + "\n")
    file.write(catchy_text + "\n")
    file.write(intro_text + "\n")
    file.write(stats_text + "\n")
    file.write("# Projects\n")

    for project in projects:
        file.write(f"## {project['name']}\n")

        links = project.get('links')
        if links and isinstance(links, list):
            thumbnails = [link for link in links if link['description'].startswith("Thumbnail")]
            if thumbnails:
                for thumbnails in thumbnails:
                    file.write(f"![{thumbnails['description']}]({thumbnails['url']})\n")
                file.write("\n")

        english_short_description = "No english short description available."
        german_short_description = "Keine deutsche Kurzbeschreibung verfügbar."
        if project.get('shortDescription') and isinstance(project['shortDescription'], list):
            for description in project['shortDescription']:
                if description.get('language') == "ENGLISH":
                    english_short_description = description.get('content', "No english short description available.")
                if description.get('language') == "GERMAN":
                    german_short_description = description.get('content', "Keine deutsche Kurzbeschreibung verfügbar.")
        file.write(f"{english_short_description}\n")
        file.write(f"\n---\n")
        file.write(f"{german_short_description}\n\n<br>\n\n")

        if project.get('links') and isinstance(project['links'], list):
            for link in sorted(project['links'], key=lambda x: x['description'], reverse=False):
                if link['description'].startswith(("Website", "API", "GitHub", "Book", "Document")):
                    file.write(f"- [{link['description']}]({link['url']})\n")
        file.write("\n\n<br>\n\n")

    file.write("# Skills\n")
    sorted_skills = sorted(skills, key=lambda x: x['count'], reverse=True)
    markdown_table = "| Name | Category | Used |\n|------|----------|-------|\n"
    for skill in sorted_skills:
        markdown_table += f"| {skill['name']} | {snake_case_to_normal(skill['skillCategory'])} | {skill['count']} |\n"
    file.write(markdown_table)

for project in projects:

    links = project.get('links')
    if links and isinstance(links, list):
        github_links = [link for link in links if link['description'].startswith("GitHub Repository")]
    else:
        continue

    if not github_links:
        continue

    for github_link in github_links:
        repo_name = github_link['url'].rstrip('/').split('/')[-1]
        file_name = f'{dir_name}/{repo_name}.md'

        with open(file_name, 'w') as file:
            file.write(f"{website_checkout_text}\n\n")
            file.write(f"# {project['name']}\n\n")

            links = project.get('links')
            if links and isinstance(links, list):
                thumbnails = [link for link in links if link['description'].startswith("Thumbnail")]
                if thumbnails:
                    for thumbnails in thumbnails:
                        file.write(f"![{thumbnails['description']}]({thumbnails['url']})\n")
                    file.write("\n")

            english_short_description = "No englisch short description available."
            german_short_description = "Keine englische Kurzbeschreibung verfügbar."
            if project.get('shortDescription') and isinstance(project['shortDescription'], list):
                for description in project['shortDescription']:
                    if description.get('language') == "ENGLISH":
                        english_short_description = description.get('content')
                    if description.get('language') == "GERMAN":
                        german_short_description = description.get('content')
            file.write(f"{english_short_description}\n\n")
            file.write(f"\n---\n")
            file.write(f"{german_short_description}\n\n")

            file.write(f"## Key Facts\n\n")
            file.write(f"- {snake_case_to_normal(project['type'])} {snake_case_to_normal(project['category'])} Project\n")
            file.write(f"- {project['workDays']} Workdays\n")
            if project.get('client'):
                file.write(f"- Client: {project['client']}\n")
            file.write(f"- Language: {snake_case_to_normal(project['language'])}\n")
            if project.get('volume'):
                file.write(f"- Volume: {project['volume']}\n")
            file.write(f"- Team Size: {project['teamSize']}\n\n")

            roles = project.get('roles')
            if roles and isinstance(roles, list):
                file.write(f"### Roles\n\n")
                for role in roles:
                    file.write(f"- {snake_case_to_normal(role)}\n")
                file.write("\n")

            file.write(f"## Project Goals\n\n")
            english_goal = "No englisch goal description available."
            german_goal = "Keine deutsche Zielbeschreibung verfügbar."
            if project.get('shortDescription') and isinstance(project['shortDescription'], list):
                for goal in project['goal']:
                    if goal.get('language') == "ENGLISH":
                        english_goal = goal.get('content')
                    if goal.get('language') == "GERMAN":
                        german_goal = goal.get('content')
            file.write(f"{english_goal}\n\n")
            file.write(f"\n---\n")
            file.write(f"{german_goal}\n\n")

            file.write(f"## Experience\n\n")
            english_description = "No englisch description available."
            german_description = "Keine deutsche Beschreibung verfügbar."
            if project.get('description') and isinstance(project['description'], list):
                for description in project['description']:
                    if description.get('language') == "ENGLISH":
                        english_description = description.get('content')
                    if description.get('language') == "GERMAN":
                        german_description = description.get('content')
            file.write(f"{english_description}\n\n")
            file.write(f"\n---\n")
            file.write(f"{german_description}\n\n")

            skills = project.get('skills')
            if skills and isinstance(skills, list):
                softSkills = [skill for skill in skills if skill['skillCategory'].startswith("SOFT_SKILL")]
                technologySkill = [skill for skill in skills if skill['skillCategory'].startswith("TECHNOLOGY")]
                programmingLanguageSkills = [skill for skill in skills if skill['skillCategory'].startswith("PROGRAMMING_LANGUAGE")]

                file.write(f"## Skills\n\n")
                if programmingLanguageSkills:
                    file.write(f"### Programming Languages\n\n")
                    for skill in programmingLanguageSkills:
                        file.write(f" - {skill['name']}\n")
                if technologySkill:
                    file.write(f"### Technologies\n\n")
                    for skill in technologySkill:
                        file.write(f" - {skill['name']}\n")
                if softSkills:
                    file.write(f"### Soft Skill\n\n")
                    for skill in softSkills:
                        file.write(f" - {skill['name']}\n")
                file.write("\n")

            links = project.get('links')
            if links and isinstance(links, list):
                visite_links = [link for link in links if
                                link['description'].startswith(("Website", "API", "GitHub", "Book", "Document"))]
                if visite_links:
                    file.write(f"## Visite\n\n")
                    for link in sorted(visite_links, key=lambda link: link['description']):
                        file.write(f"- [{link['description']}]({link['url']})\n")
                    file.write("\n")

            links = project.get('links')
            if links and isinstance(links, list):
                image_links = [link for link in links if link['description'].startswith("Image")]
                sorted_image_links = sorted(image_links, key=lambda link: link['description'])
                if sorted_image_links:
                    file.write(f"## Gallery\n\n")
                    for link in sorted_image_links:
                        file.write(f"![{link['description']}]({link['url']})\n")
                    file.write("\n")
