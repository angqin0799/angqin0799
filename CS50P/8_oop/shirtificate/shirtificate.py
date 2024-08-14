from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")

# pdf.set_page_background("floral.png")
pdf.add_page()
pdf.set_font("times", "B", 35)
pdf.set_text_color(0)
pdf.cell(0, 30, text="CS50 Shirtificate", align="C")

pdf.image("shirtificate.png", x=5, y=50, w=200, h= 210)

pdf.set_font("times", "I", 30)
pdf.set_text_color(255,255,255)
pdf.set_xy(10, 50)
pdf.cell(0, 150, text=f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
