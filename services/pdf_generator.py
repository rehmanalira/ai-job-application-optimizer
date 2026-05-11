from reportlab.platypus import *
from reportlab.lib.styles import *
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


def create_resume_pdf(content, filename):

    doc = SimpleDocTemplate(

        filename,

        pagesize=A4,

        rightMargin=40,
        leftMargin=40,
        topMargin=30,
        bottomMargin=20
    )

    styles = getSampleStyleSheet()

    story = []

    lines = content.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # HEADINGS
        if (
            line.isupper()
            and len(line) < 40
        ):

            heading = Paragraph(

                f"""
                <font size="14" color="#1D4ED8">
                <b>{line}</b>
                </font>
                """,

                styles["Heading2"]
            )

            story.append(heading)

            story.append(
                Spacer(1, 6)
            )

            story.append(
                HRFlowable(
                    color=colors.HexColor("#1D4ED8")
                )
            )

            story.append(
                Spacer(1, 10)
            )

        else:

            paragraph = Paragraph(

                f"""
                <font size="10.5">
                {line}
                </font>
                """,

                styles["BodyText"]
            )

            story.append(paragraph)

            story.append(
                Spacer(1, 5)
            )

    doc.build(story)