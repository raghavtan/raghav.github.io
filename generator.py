from jinja2 import Template

from html_template import HTML_TEMPLATE
from markdown_template import MARKDOWN_TEMPLATE
from pdf_template import PDF_TEMPLATE


# Remove pdfkit import since we're not using it anymore

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
    """Generate a PDF resume using xhtml2pdf."""
    from xhtml2pdf import pisa  # Import xhtml2pdf library
    rendered_pdf_html = render_template(PDF_TEMPLATE, data)

    # Open output file for writing (binary mode)
    with open(output_file, "w+b") as result_file:
        # Convert HTML to PDF
        pisa_status = pisa.CreatePDF(rendered_pdf_html, dest=result_file)

    if pisa_status.err:
        print("An error occurred while generating the PDF resume using xhtml2pdf.")
    else:
        print(f"PDF resume generated and saved as '{output_file}'.")
