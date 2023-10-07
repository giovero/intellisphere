from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os


class pdfGenerator(object):
    
    def __init__(self, pdf_name, pdf_content):
        self.pdf_name = pdf_name
        self.pdf_content = pdf_content
        pdf_folder = os.path.join(os.getcwd(), 'pdf_result')
        if not os.path.exists(pdf_folder):
            os.makedirs(pdf_folder, mode=0o777)
        self.pdf_path = os.path.join(pdf_folder, self.pdf_name)
    
    def generate_pdf(self, x_pos=20, y_pos=20):
        doc = SimpleDocTemplate(self.pdf_path, pagesize=letter)
        story = []
        
        styles = getSampleStyleSheet()
        self.pdf_content = self.pdf_content.replace(". ", ".\n")
        for token in self.pdf_content.split("\n"):
            paragraph = Paragraph(token, styles["Normal"])
            story.append(paragraph)
        
        doc.build(story)

        return self.pdf_path

