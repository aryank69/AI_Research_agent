from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(filename, query, content):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    story = []

    # Title
    story.append(Paragraph("<b>AI Research Report</b>", styles["Title"]))
    story.append(Spacer(1, 12))

    # Query
    story.append(Paragraph(f"<b>Query:</b> {query}", styles["Normal"]))
    story.append(Spacer(1, 12))

    # Content (handle line breaks)
    formatted_content = content.replace("\n", "<br/>")
    story.append(Paragraph(formatted_content, styles["Normal"]))

    doc.build(story)