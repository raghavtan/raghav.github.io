# templates.py

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{{ name }}'s Resume</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1, h2, h3 { color: #333; }
        .contact { font-size: 0.9em; }
        .section { margin-bottom: 25px; }
        ul { list-style-type: disc; margin-left: 20px; }
    </style>
</head>
<body>
    <header>
        <h1>{{ name }}</h1>
        <h2>{{ title }}</h2>
        <div class="contact">
            <p>{{ contact.address }} | {{ contact.phone }} | {{ contact.email }}</p>
            <p>
                <a href="https://{{ contact.linkedin }}">{{ contact.linkedin }}</a> |
                <a href="https://{{ contact.github }}">{{ contact.github }}</a>
            </p>
        </div>
    </header>

    <div class="section">
        <h2>Executive Summary</h2>
        <p>{{ executive_summary }}</p>
    </div>

    <div class="section">
        <h2>Experience</h2>
        {% for job in experience %}
        <div class="job">
            <h3>{{ job.company }} - {{ job.role }} ({{ job.location }})</h3>
            <p><em>{{ job.duration }}</em></p>
            <ul>
                {% for item in job.details %}
                <li>{{ item }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </div>

    <div class="section">
        <h2>Core Competencies</h2>
        {% for category, skills in core_competencies.items() %}
        <p><strong>{{ category }}:</strong> {{ skills }}</p>
        {% endfor %}
    </div>

    <div class="section">
        <h2>Education</h2>
        {% for edu in education %}
        <div class="education">
            <h3>{{ edu.institution }}</h3>
            <p>{{ edu.degree }} ({{ edu.duration }}) - {{ edu.location }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

# Markdown Template
MARKDOWN_TEMPLATE = """
# {{ name }}
### {{ title }}

**Address:** {{ contact.address }}  
**Phone:** {{ contact.phone }}  
**Email:** {{ contact.email }}  
**LinkedIn:** [{{ contact.linkedin }}](https://{{ contact.linkedin }})  
**GitHub:** [{{ contact.github }}](https://{{ contact.github }})

---

## Executive Summary
{{ executive_summary }}

## Experience
{% for job in experience %}
### {{ job.company }} - {{ job.role }} ({{ job.location }})
**Duration:** {{ job.duration }}

{% for item in job.details %}
- {{ item }}
{% endfor %}

{% endfor %}

## Core Competencies
{% for category, skills in core_competencies.items() %}
**{{ category }}:** {{ skills }}  
{% endfor %}

## Education
{% for edu in education %}
### {{ edu.institution }}
- **{{ edu.degree }}** ({{ edu.duration }}) - {{ edu.location }}
{% endfor %}
"""

# PDF Template (HTML with inline CSS for styling)
PDF_TEMPLATE = """
<html>
<head>
    <meta charset="utf-8">
    <title>{{ name }}'s Resume (PDF)</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1, h2, h3 { color: #333; }
        .contact { font-size: 0.9em; }
        .section { margin-bottom: 30px; }
        ul { list-style-type: disc; margin-left: 20px; }
    </style>
</head>
<body>
    <header>
        <h1>{{ name }}</h1>
        <h2>{{ title }}</h2>
        <div class="contact">
            <p>{{ contact.address }} | {{ contact.phone }} | {{ contact.email }}</p>
            <p>
                <a href="https://{{ contact.linkedin }}">{{ contact.linkedin }}</a> |
                <a href="https://{{ contact.github }}">{{ contact.github }}</a>
            </p>
        </div>
    </header>

    <div class="section">
        <h2>Executive Summary</h2>
        <p>{{ executive_summary }}</p>
    </div>

    <div class="section">
        <h2>Experience</h2>
        {% for job in experience %}
        <div class="job">
            <h3>{{ job.company }} - {{ job.role }} ({{ job.location }})</h3>
            <p><em>{{ job.duration }}</em></p>
            <ul>
                {% for item in job.details %}
                <li>{{ item }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </div>

    <div class="section">
        <h2>Core Competencies</h2>
        {% for category, skills in core_competencies.items() %}
        <p><strong>{{ category }}:</strong> {{ skills }}</p>
        {% endfor %}
    </div>

    <div class="section">
        <h2>Education</h2>
        {% for edu in education %}
        <div class="education">
            <h3>{{ edu.institution }}</h3>
            <p>{{ edu.degree }} ({{ edu.duration }}) - {{ edu.location }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""
