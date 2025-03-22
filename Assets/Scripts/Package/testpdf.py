from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import datetime


class PDF(FPDF):
    def header(self):
        self.set_y(5)
        self.set_font("helvetica", "", 10)
        w = self.w
        l_margin = self.l_margin
        r_margin = self.r_margin
        width = (w - l_margin - r_margin)
        self.cell(width / 3, 10, "Prüfbericht", border=False, align="L")
        self.cell(width / 3, 10, "KST-Schweißprüfung", border=False, align="C")
        self.cell(width / 3, 10, "<Nachname> <Vorname>", border=False, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        w = self.w
        l_margin = self.l_margin
        r_margin = self.r_margin
        width = (w - l_margin - r_margin)
        exam_date = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"
        self.set_font("helvetica", "", 10)
        self.cell(width / 2, 10, f"Seite {self.page_no()} von {self.pages_count}", border=False, align="L")
        self.cell(width / 2, 10, f"{exam_date}", border=False, align="R")


pdf = PDF("P", "mm", "A4")
pdf.set_title("Prüfbericht - <Nachname> <Vorname>")
pdf.set_auto_page_break(auto=True, margin=25)
pdf.set_margin(margin=25)
pdf.add_page()
pdf.set_font("helvetica", "B", 16)

# Title ----------------------------------------------------------------------------------------------------------------
pdf.cell(0, 10, "Prüfbericht nach ÖNORM M 7861-6:2009", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(5)

# examinee data --------------------------------------------------------------------------------------------------------
pdf.set_font("helvetica", "U", 12)
pdf.cell(0, 10, "Prüflingsdaten:", align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("helvetica", "", 12)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Vorname:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Vorname>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Nachname:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Nachname>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Geburtsdatum:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Geburtsdatum>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(5)

# piece data -----------------------------------------------------------------------------------------------------------
pdf.set_font("helvetica", "U", 12)
pdf.cell(0, 10, "Erzeugnisdaten:", align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("helvetica", "", 12)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Art:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Art>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Lieferform:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Lieferform>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Bezeichnung:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Bezeichnung>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Herstellungsdatum:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Herstellungsdatum>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Herstellungsverfahren:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Herstellungsverfahren>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Grundwerkstoff:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Grundwerkstoff>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Zusatzwerkstoffe:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Zusatzwerkstoffe>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Abmessungen:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Abmessungen>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(5)

# exam data ------------------------------------------------------------------------------------------------------------
pdf.set_font("helvetica", "U", 12)
pdf.cell(0, 10, "Prüfdaten:", align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("helvetica", "", 12)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Durchschnittstemperatur:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Durchschnittstemperatur>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Dauerprüfdruck:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Dauerprüfdruck>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Berstdruck:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Berstdruck>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(40, 10, "Prüfdauer:", border=False, align="L")
pdf.cell(10, 10, "", border=False, align="L")
pdf.cell(60, 10, "<Prüfdauer>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.add_page()

# visual grade ---------------------------------------------------------------------------------------------------------
pdf.set_font("helvetica", "U", 12)
pdf.cell(0, 10, "Visuelle Beurteilung des Prüfstücks und der Schweißverbindungen:", align="L",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("helvetica", "", 12)

pdf.cell(10, 10, "", border=False, align="L")
pdf.multi_cell(0, 10, "<Visuelle Beurteilung des Prüfstücks und der Schweißverbindungen>", border=False, align="L")
pdf.ln(5)

# pressure diagram -----------------------------------------------------------------------------------------------------
image_height = 100
text_height = 10
remaining_space = pdf.h - pdf.b_margin - pdf.get_y()

if remaining_space < (image_height + text_height):
    pdf.add_page()
pdf.set_font("helvetica", "U", 12)
pdf.cell(0, 10, "Abbildung des Druckverlaufes während der Prüfung:", align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("helvetica", "", 12)
pdf.image("../../Testdiagramm.png", x=15, y=pdf.get_y() + 5, w=180)
pdf.set_y(pdf.get_y() + image_height + 5)

# grade of exam --------------------------------------------------------------------------------------------------------
pdf.set_font("helvetica", "U", 12)
pdf.cell(0, 10, "Beurteilung der Prüfung:", align="L",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("helvetica", "", 12)

pdf.cell(10, 10, "", border=False, align="L")
pdf.multi_cell(0, 10, "<Beutreilung der Prüfung>")
pdf.ln(5)

# result of exam -------------------------------------------------------------------------------------------------------
pdf.set_font("helvetica", "U", 12)
pdf.cell(0, 10, "Ergebnis der Prüfung:", align="L",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("helvetica", "", 12)

pdf.cell(10, 10, "", border=False, align="L")
pdf.multi_cell(0, 10, "<Ergebnis der Prüfung>")

# save -----------------------------------------------------------------------------------------------------------------
pdf.output("Pruefbericht_Nachname_Vorname.pdf")
