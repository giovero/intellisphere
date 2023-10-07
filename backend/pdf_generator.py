from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from PyPDF2 import PdfMerger
import os


class pdfGenerator(object):
    
    def __init__(self, pdf_name, pdf_content):
        self.pdf_name = pdf_name
        self.pdf_content = pdf_content
        self.pdf_folder = os.path.join(os.getcwd(), 'pdf_result')
        if not os.path.exists(self.pdf_folder):
            os.makedirs(self.pdf_folder, mode=0o777)
        self.pdf_path = os.path.join(self.pdf_folder, self.pdf_name)
    
    def generate_pdf(self, x_pos=20, y_pos=20):
        doc = SimpleDocTemplate(self.pdf_path, pagesize=letter)
        story = []
        
        styles = getSampleStyleSheet()
        self.pdf_content = self.pdf_content.replace(". ", ".\n")
        for token in self.pdf_content.split("\n"):
            paragraph = Paragraph(token, styles["Normal"])
            story.append(paragraph)
        
        doc.build(story)
        print("Pdf generated %s" % (self.pdf_path))
        return self.pdf_path

    def pdf_merge(self, pdf_to_merge):
        pdf_merger = PdfMerger()
        output_pdf = os.path.join(self.pdf_folder, 'merged.pdf')
        try:
            for pdf_file in pdf_to_merge:
                pdf_merger.append(pdf_file)
            with open(output_pdf, 'wb') as output_file:
                pdf_merger.write(output_file)
        except Exception as e:
            print(f'Error: {str(e)}')
        finally:
            pdf_merger.close()
        print("Pdf generated %s" % (output_pdf))
        return output_pdf

    