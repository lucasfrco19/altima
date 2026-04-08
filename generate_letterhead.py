from fpdf import FPDF, XPos, YPos
import os

class AltimaLetterhead(FPDF):
    def header(self):
        # Logo
        if os.path.exists("logo sem fundo.png"):
            self.image("logo sem fundo.png", 10, 8, 45)
        
        # Line break to ensure the line is below the logo
        self.ln(50)
        # Decorative line
        self.set_draw_color(212, 175, 55)
        self.set_line_width(0.5)
        self.line(10, 58, 200, 58)
        
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-25)
        self.set_line_width(0.2)
        self.set_draw_color(212, 175, 55)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)
        # Helvetica 8
        self.set_font("helvetica", "I", 8)
        self.set_text_color(60, 63, 65) # Graphite
        self.cell(0, 4, "ALTIMA Clínica Integrada | Excelência em Saúde e Bem-estar", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.cell(0, 4, "Rua do Cuidado, 123 - Centro Médico - São Paulo/SP", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.cell(0, 4, "Contato: (11) 99999-8888 | www.altimaclinica.com.br", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

def create_pdf():
    pdf = AltimaLetterhead()
    pdf.add_page()
    pdf.set_font("times", "", 12)
    # Background watermark (optional, but keep it quiet luxury)
    # pdf.image("logo sem fundo.png", 60, 100, 90, opacity=0.05) 
    # fpdf2 supports image opacity but let's keep it simple first
    
    output_filename = "papel_timbrado_altima.pdf"
    pdf.output(output_filename)
    print(f"PDF generated: {output_filename}")

if __name__ == "__main__":
    create_pdf()
