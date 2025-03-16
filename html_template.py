HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{{ name }}'s Resume</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background-color: #ffffff;
      color: #000;
      line-height: 1.5;
    }
    .header {
      text-align: center;
      margin-bottom: 30px;
    }
    .header h1 {
      font-size: 2.5em;
      margin: 0;
    }
    .header h3 {
      margin: 5px 0;
      font-weight: normal;
    }
    .header p {
      margin: 5px 0;
      font-size: 0.95em;
    }
    hr {
      border: none;
      border-top: 1px solid #ccc;
      margin: 20px 0;
    }
    .full-width {
      width: 100%;
    }
    h2 {
      text-transform: uppercase;
      border-bottom: 1px solid #ccc;
      padding-bottom: 5px;
      margin-bottom: 15px;
      font-size: 1.2em;
    }
    .section {
      margin-bottom: 30px;
    }
    .job, .edu {
      margin-bottom: 20px;
    }
    .job-title, .edu-title {
      font-weight: bold;
      font-size: 1.1em;
      margin: 0;
    }
    .job-duration, .edu-duration {
      font-style: italic;
      font-size: 0.95em;
      margin: 0;
    }
    ul {
      margin-left: 20px;
    }
    /* Two-column layout for the lower section */
    .two-column-container {
      display: flex;
      gap: 20px;
    }
    .left-column {
      width: 65%;
      /* Contains Experience */
    }
    .divider {
      width: 1px;
      background-color: #ccc;
    }
    .right-column {
      width: 34%;
      padding-left: 20px;
      /* Contains Core Competencies and Education stacked */
    }
    .right-section {
      margin-bottom: 30px;
    }
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

  <!-- Full Width Executive Summary -->
  <div class="section full-width">
    <h2>Executive Summary</h2>
    <p>{{ executive_summary }}</p>
  </div>

  <!-- Two-Column Layout with Divider -->
  <div class="two-column-container">
    <!-- Left Column: Experience -->
    <div class="left-column">
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
    </div>

    <!-- Divider -->
    <div class="divider"></div>

    <!-- Right Column: Core Competencies and Education -->
    <div class="right-column">
      <div class="right-section">
        <h2>Core Competencies</h2>
        {% for category, skills in core_competencies.items() %}
        <p><strong>{{ category }}:</strong><br>{{ skills }}</p>
        {% endfor %}
      </div>
      <div class="right-section">
        <h2>Education</h2>
        {% for edu in education %}
        <div class="edu">
          <p class="edu-title">{{ edu.institution }}</p>
          <p class="edu-duration">{{ edu.degree }} ({{ edu.duration }}) - {{ edu.location }}</p>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
</body>
</html>
"""
