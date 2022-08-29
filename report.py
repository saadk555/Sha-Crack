from fpdf import FPDF

# fpdf library for pdf generation

class PDF(FPDF):
    def header(self):
        self.image('logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(81, 10, 'Vulnerable Passwords Report', 1, 0, 'C')
        self.ln(20)
