from fpdf import FPDF

# fpdf library for pdf generation

class PDF(FPDF):
    def header(self):
        self.image('logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(81, 10, 'Vulnerable Passwords Report', 1, 0, 'C')
        self.ln(20)
        
    def percentage_to_round_chart(self,percentage, radius, color):
   
        # Set the font and size of the text.
        self.set_font("Arial", size=12)

        # Draw the chart.
        self.ellipse(radius, radius, radius, radius, color)

        # Write the percentage to the chart.
        self.text(radius + 20, radius + 25, str(percentage) + "%")

        # Return the fpdf object.
        return self