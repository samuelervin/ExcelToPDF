import pandas as pd
import glob
from fpdf import FPDF   # Import FPDF class from fpdf module
from pathlib import Path
import utils as utils




# Read all the excel files in the invoices folder
filepaths = glob.glob("invoices/*.xlsx")

# Read all the excel files in the invoices folder
for filepath in filepaths:
   
    
    filename = Path(filepath).stem
    invoice_number, invoice_date = filename.split("-")
    invoice_date = utils.make_date(invoice_date.replace(".", "-"))
    
    # Create instance of FPDF class
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()
    
    pdf.set_font(family="Times",style="B", size=16)  # Set font for the
    pdf.set_text_color(100, 100, 100)  # Set text color
    pdf.cell(200, 8, txt=f"Invoice #: {invoice_number}", ln=1, align="L")  
    pdf.cell(200, 8, txt=f"Invoice Date: {invoice_date}", ln=1, align="L")

    pdf.line(10, 30, 200, 30)
    pdf.cell(200, 8, txt="", ln=1, align="L")

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Add cells for the table headers
    columns = list(df.columns)
    pdf.set_font("Times", size=10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_fill_color(200, 200, 200)
    pdf.cell(w=30, h=10, txt=utils.format_columname(columns[0]), border=1, ln=0, align="C",fill=True)
    pdf.cell(w=70, h=10, txt=utils.format_columname(columns[1]), border=1, ln=0, align="C",fill=True)
    pdf.cell(w=30, h=10, txt=utils.format_columname(columns[2]), border=1, ln=0, align="C",fill=True)
    pdf.cell(w=30, h=10, txt=utils.format_columname(columns[3]), border=1, ln=0, align="C",fill=True)
    pdf.cell(w=30, h=10, txt=utils.format_columname(columns[4]), border=1, ln=1, align="C",fill=True)
    
    for index,row in df.iterrows():       
        # Set font for the rest of the text
        pdf.set_font("Times", size=10)
        pdf.set_text_color(80, 80, 80)

        # Add cells for the table headers
        pdf.cell(w=30, h=10, txt=str(row["product_id"]), border=1, align="C")
        pdf.cell(w=70, h=10, txt=row["product_name"], border=1, align="L")
        pdf.cell(w=30, h=10, txt=str(row["amount_purchased"]), border=1, align="C")
        pdf.cell(w=30, h=10, txt=utils.format_currency(row["price_per_unit"]), border=1, align="C")
        pdf.cell(w=30, h=10, txt=utils.format_currency(row["total_price"]), border=1, align="C",ln=1)
        

    # Add the total price
    pdf.set_font("Times", size=10, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=160, h=10, txt="Amount Due",  align="C")
    pdf.cell(w=30, h=10, txt=utils.format_currency(df["total_price"].sum()), align="C",ln=1)
    
    pdf.output(f"PDFS/{filename}.pdf")