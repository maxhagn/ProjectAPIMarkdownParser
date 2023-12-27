import os

import requests

url_project = "https://api.projects.hagn.network/public/hagn/project"
url_project_stats = "https://api.projects.hagn.network/public/hagn/project/stats"
url_skill_stats = "https://api.projects.hagn.network/public/hagn/skill/stats"

projects = sorted(requests.get(url_project).json(), key=lambda x: x.get('relevanceScore', 0), reverse=True)
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
stats_text = f"""
# Statistics
## Projects
- Total Project Engagements: {project_stats['projectCount']}
- Websites Deployed on Kubernetes: {project_stats['totalWebsites']}
- Client Collaborations: {project_stats['clientCount']}
- Code Repositories Managed: {project_stats['totalRepositories']}
- Cumulative Workdays: {project_stats['totalWorkdays']}

## Skills
- Programming Languages: {skill_stats['languageCount']}
- Technologies: {skill_stats['technologyCount']}
- Soft Skills: {skill_stats['softSkillCount']}
- Total Skills: {skill_stats['skillCount']}
"""

os.makedirs('markdown', exist_ok=True)


def snake_case_to_normal(snake_str):
    words = snake_str.lower().split('_')
    return ' '.join(word.capitalize() for word in words)


with open('markdown/PROJECTS.md', 'w') as file:
    file.write(hero_text + "\n")
    file.write(catchy_text + "\n")
    file.write(intro_text + "\n")
    file.write(stats_text + "\n")
    file.write("# Projects\n")

    for project in projects:
        file.write(f"## {project['name']}\n")

        english_short_description = "Keine englische Kurzbeschreibung verfügbar"
        if project.get('shortDescription') and isinstance(project['shortDescription'], list):
            for description in project['shortDescription']:
                if description.get('language') == "ENGLISH":
                    english_short_description = description.get('content', "Keine englische Kurzbeschreibung verfügbar")
                    break
        file.write(f"{english_short_description}\n\n")

        if project.get('links') and isinstance(project['links'], list):
            for link in project['links']:
                if link['description'].startswith(("Website", "API", "GitHub", "Github")):
                    file.write(f"- [{link['description']}]({link['url']})\n")
        file.write("\n")

for project in projects:
    with open(f'markdown/{project["name"].replace("/", "_").replace(" ", "_")}.md', 'w') as file:
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
                for link in visite_links:
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
