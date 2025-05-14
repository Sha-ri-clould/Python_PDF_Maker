from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(False,margin=0)
df=pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', size=26, style='B')
    pdf.set_text_color(0,0,0)
    pdf.cell(w=0,h=12,txt=row['Topic'],align="L",ln=1,border=0)
    pdf.line(10,21,200,21)

    #Set Footer
    pdf.ln(257)
    pdf.set_font(family='Times', size=14, style='I')
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row['Topic'],align="R",ln=1,border=0)
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set Footer
        pdf.ln(270)
        pdf.set_font(family='Times', size=14, style='I')
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row['Topic'], align="R", ln=1, border=0)



pdf.output("output.pdf")