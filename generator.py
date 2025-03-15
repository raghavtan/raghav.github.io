# generator.py

import sys

from jinja2 import Template

try:
    import pdfkit
except ImportError:
    print("pdfkit is not installed. Please install it with 'pip install pdfkit'.")
    sys.exit(1)

from templates import HTML_TEMPLATE, MARKDOWN_TEMPLATE, PDF_TEMPLATE


def render_template(template_str, context):
    """Render a Jinja2 template with the provided context."""
    template = Template(template_str)
    return template.render(**context)


def generate_html_resume(data, output_file="resume.html"):
    """Generate an HTML resume."""
    rendered_html = render_template(HTML_TEMPLATE, data)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rendered_html)
    print(f"HTML resume generated and saved as '{output_file}'.")


def generate_markdown_resume(data, output_file="resume.md"):
    """Generate a Markdown resume."""
    rendered_md = render_template(MARKDOWN_TEMPLATE, data)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rendered_md)
    print(f"Markdown resume generated and saved as '{output_file}'.")


def generate_pdf_resume(data, output_file="resume.pdf"):
    """Generate a PDF resume using pdfkit."""
    rendered_pdf_html = render_template(PDF_TEMPLATE, data)
    try:
        # If wkhtmltopdf is not in your PATH, specify its location:
        # config = pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')
        # pdfkit.from_string(rendered_pdf_html, output_file, configuration=config)
        pdfkit.from_string(rendered_pdf_html, output_file)
        print(f"PDF resume generated and saved as '{output_file}'.")
    except Exception as e:
        print("An error occurred while generating the PDF resume:")
        print(e)
