<small>**🚀 Explore my digital universe: [maximilian.hagn.network](https://maximilian.hagn.network)!</small>**

# Homeserver Docker CI Architecture

![Thumbnail](https://files.hagn.network/images/docker/thumbnail.webp)

A project to modernize my homeserver architecture by transitioning to Docker containers and implementing a GitHub Actions-based CI pipeline.


---
Modernisierung meiner Homeserver-Architektur durch den Einsatz von Docker-Containern und die Implementierung einer GitHub Actions-basierten CI-Pipeline.

## Key Facts

- Private Server Architecture Project
- 15 Workdays
- Language: German
- Team Size: 1

### Roles

- Software Architect

## Project Goals

The primary objectives were to modernize the existing homeserver architecture by containerizing all hosted web applications and APIs using Docker. A key goal was to transition from a continuous integration pipeline based on shell scripts and CLI commands to GitHub Actions. This involved adding a GitHub workflow to each project for automated building and pushing to a private Docker registry upon a push to the main branch, facilitating faster deployment to production. Another goal was to replace the existing Apache reverse proxy setup with a more modular nginx reverse proxy configuration. Each container now has a mini nginx web server making data available, managed globally by a reverse proxy dynamically assembled through a shell script and planned to be replaced by Kubernetes ingress in a follow-up project. Additionally, the project aimed to automate SSL encryption with Let's Encrypt, using a shell script that dynamically handles tasks like starting, updating, or deleting containers.


---
Die Hauptziele bestanden darin, die bestehende Homeserver-Architektur zu modernisieren, indem alle gehosteten Webapplikationen und APIs mit Docker containerisiert wurden. Ein wesentliches Ziel war der Übergang von einer Continuous Integration Pipeline, basierend auf Shell-Skripten und CLI-Befehlen, zu GitHub Actions. Dies beinhaltete das Hinzufügen eines GitHub-Workflows zu jedem Projekt, der bei einem Push in den Hauptzweig automatisch buildet und auf meine private Docker-Registry pusht, um eine schnellere Bereitstellung in der Produktion zu ermöglichen. Ein weiteres Ziel war es, das bestehende Apache Reverse Proxy-Setup durch eine modularere nginx Reverse Proxy-Konfiguration zu ersetzen. Jeder Container verfügt nun über einen Mini-Nginx-Webserver, die Datenverwaltung erfolgt global durch einen dynamisch durch ein Shell-Skript aufgebauten Reverse Proxy, der in einem Folgeprojekt durch Kubernetes Ingress ersetzt werden soll. Zusätzlich zielte das Projekt darauf ab, die SSL-Verschlüsselung mit Let's Encrypt zu automatisieren, wobei ein Shell-Skript dynamisch Aufgaben wie das Starten, Aktualisieren oder Löschen von Containern übernimmt.

## Experience

In this project, I extensively worked with Docker, Linux, and server architectures. I containerized seven websites (PHP, Angular, React), two APIs (Kotlin, Java), four databases (MySQL, Redis, MongoDB), and additional services like a Nginx reverse proxy container, Keycloak, a private Docker registry, and a document server. Integrating Keycloak as an open-source identity and access management solution centralized authorization for all APIs and websites. This project served as a significant learning experience in server architecture development, improving my skills in continuous integration, server management, and automated SSL encryption.


---
In diesem Projekt arbeitete ich intensiv mit Docker, Linux und Serverarchitekturen. Ich containerisierte sieben Websites (PHP, Angular, React), zwei APIs (Kotlin, Java), vier Datenbanken (MySQL, Redis, MongoDB) und zusätzliche Dienste wie einen Nginx Reverse Proxy Container, Keycloak, eine private Docker-Registry und einen Dokumentenserver. Die Integration von Keycloak als Open-Source-Identitäts- und Zugriffsmanagementlösung zentralisierte die Autorisierung für alle APIs und Websites. Dieses Projekt war eine bedeutende Lernerfahrung in der Entwicklung von Server Architekturen und verbesserte meine Fähigkeiten in kontinuierlicher Integration, Serververwaltung und automatisierter SSL-Verschlüsselung.

## Skills

### Technologies

 - Docker
 - Nginx
 - UNIX
 - IntelliJ
 - Git

## Visite

- [GitHub Repository Docker Scripts](https://github.com/maxhagn/DockerHomeserver)
- [GitHub Repository Static File Server](https://github.com/maxhagn/StaticFileServer)

## Gallery

![Image 01 Architecture](https://files.hagn.network/images/docker/architecture.webp)

