PDF_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{{ name }}'s Resume</title>
  <style>
    @page { size: A4; margin: 20mm; }
    body {
      font-family: Arial, sans-serif;
      font-size: 10pt;
      line-height: 1.5;
      color: #000;
    }
    .header {
      text-align: center;
      margin-bottom: 10mm;
    }
    .header h1 { font-size: 24pt; margin: 0; }
    .header h3 { font-size: 14pt; margin: 5pt 0; font-weight: normal; }
    .header p { font-size: 10pt; margin: 3pt 0; }
    .container {
      width: 100%;
      display: table;
    }
    .left-column, .right-column {
      display: table-cell;
      vertical-align: top;
    }
    .left-column { width: 65%; padding-right: 10mm; }
    .right-column { width: 35%; padding-left: 10mm; border-left: 1pt solid #ccc; }
    h2 {
      text-transform: uppercase;
      border-bottom: 1pt solid #000;
      margin: 10pt 0 5pt 0;
      font-size: 12pt;
    }
    .section { margin-bottom: 10mm; }
    .job, .edu { margin-bottom: 5mm; }
    .job-title, .edu-title { font-weight: bold; font-size: 12pt; margin: 0; }
    .job-duration, .edu-duration { font-style: italic; font-size: 9pt; margin: 0; }
    ul { margin-left: 10mm; }
  </style>
</head>
<body>
  <div class="header">
    <h1>{{ name }}</h1>
    <h3>{{ title }}</h3>
    <p>{{ contact.address }}</p>
    <p>{{ contact.phone }} | {{ contact.email }}</p>
    <p>
      <a href="https://{{ contact.linkedin }}">{{ contact.linkedin }}</a> |
      <a href="https://{{ contact.github }}">{{ contact.github }}</a>
    </p>
  </div>
  <div class="container">
    <!-- Left Column -->
    <div class="left-column">
      <div class="section">
        <h2>Executive Summary</h2>
        <p>{{ executive_summary }}</p>
      </div>
      <div class="section">
        <h2>Experience</h2>
        {% for job in experience %}
        <div class="job">
          <p class="job-title">{{ job.company }} - {{ job.location }} — {{ job.role }}</p>
          <p class="job-duration">{{ job.duration }}</p>
          <ul>
            {% for item in job.details %}
            <li>{{ item }}</li>
            {% endfor %}
          </ul>
        </div>
        {% endfor %}
      </div>
      <div class="section">
        <h2>Education</h2>
        {% for edu in education %}
        <div class="edu">
          <p class="edu-title">{{ edu.institution }}</p>
          <p class="edu-duration">{{ edu.degree }} ({{ edu.duration }}) - {{ edu.location }}</p>
        </div>
        {% endfor %}
      </div>
    </div>
    <!-- Right Column -->
    <div class="right-column">
      <div class="section">
        <h2>Core Competencies</h2>
        {% for category, skills in core_competencies.items() %}
        <p><strong>{{ category }}:</strong><br>{{ skills }}</p>
        {% endfor %}
      </div>
    </div>
  </div>
</body>
</html>
"""
