MARKDOWN_TEMPLATE = """
<div align="center">
  <h1 style="font-size:2.5em; margin-bottom:0;">{{ name }}</h1>
  <h3 style="margin-top:0; font-weight:normal;">{{ title }}</h3>
  <p style="margin:5px 0; font-size:0.95em;">
    {{ contact.address }}<br>
    {{ contact.phone }} | {{ contact.email }}
  </p>
  <p style="margin:5px 0; font-size:0.95em;">
    <a href="https://{{ contact.linkedin }}">{{ contact.linkedin }}</a> |
    <a href="https://{{ contact.github }}">{{ contact.github }}</a>
  </p>
</div>

<hr style="border:0; border-top:1px solid #ccc; margin:20px 0;">

<h2 style="text-transform: uppercase; border-bottom:1px solid #ccc; padding-bottom:5px;">Executive Summary</h2>
<p style="line-height:1.5;">{{ executive_summary }}</p>

<h2 style="text-transform: uppercase; border-bottom:1px solid #ccc; padding-bottom:5px;">Core Competencies</h2>
{% for category, skills in core_competencies.items() %}
<p style="margin:5px 0;"><strong>{{ category }}:</strong> {{ skills }}</p>
{% endfor %}

<hr style="border:0; border-top:1px solid #ccc; margin:20px 0;">

<h2 style="text-transform: uppercase; border-bottom:1px solid #ccc; padding-bottom:5px;">Experience</h2>
{% for job in experience %}
<div style="margin-bottom:15px;">
  <p style="margin:0; font-weight:bold; font-size:1.1em;">{{ job.company }} - {{ job.location }} — {{ job.role }}</p>
  <p style="margin:0; font-style:italic; font-size:0.95em;">{{ job.duration }}</p>
  <ul style="margin:10px 0 10px 20px; line-height:1.4;">
    {% for item in job.details %}
    - {{ item }}
    {% endfor %}
  </ul>
</div>
{% endfor %}

<hr style="border:0; border-top:1px solid #ccc; margin:20px 0;">

<hr style="border:0; border-top:1px solid #ccc; margin:20px 0;">

<h2 style="text-transform: uppercase; border-bottom:1px solid #ccc; padding-bottom:5px;">Education</h2>
{% for edu in education %}
<div style="margin-bottom:15px;">
  <p style="margin:0; font-weight:bold; font-size:1.1em;">{{ edu.institution }}</p>
  <p style="margin:0; font-style:italic; font-size:0.95em;">{{ edu.degree }} ({{ edu.duration }}) - {{ edu.location }}</p>
</div>
{% endfor %}
"""
