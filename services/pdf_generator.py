from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import A4


def create_resume_pdf(content):

    doc = SimpleDocTemplate(
        "generated_resume.pdf",
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    story = []

    for line in content.split("\n"):

        story.append(
            Paragraph(
                line,
                styles["BodyText"]
            )
        )

        story.append(
            Spacer(1, 10)
        )

    doc.build(story)