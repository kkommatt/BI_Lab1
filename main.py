from fpdf import FPDF

# Initialize the PDF object
class PDF(FPDF):
    def header(self):
        self.image("logo.png", 5, 5, 20)
        self.set_text_color(0, 51, 102)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Software Requirements Specification", border=0, ln=1, align="C")
        self.ln(10)
        self.set_draw_color(0, 51, 102)
        self.set_line_width(1)
        self.line(10, 28, 200, 28)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add the content
pdf.set_font("Arial", "B", 12)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 10, "1. Introduction", ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0)
pdf.multi_cell(0, 10, """
The purpose of this software product is to develop basic knowledge and skills for creating a mobile application. 
The application will use a database to store data, include an address book, process and visualize geospatial data, and provide a user-friendly interface adhering to UX design principles.
""")
pdf.ln(5)
pdf.set_font("Arial", "B", 12)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 10, "2. Functional Requirements", ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0)
pdf.multi_cell(0, 10, """
The mobile application must include the following functionalities:
1. Data Storage:
   - Support for writing/reading data from a file or local database.
   - Entity representation as a database table with fields.
   - Display book titles over 10 years old.
   - Calculate the percentage of selected books from the total.
2. Contact Management:
   - Show contacts whose last name ends in "ko".
   - Provide a sample of contacts.
3. Geospatial Data:
   - Calculate and display the route from the current location to a specified location on a map.
   - Display the address of the selected publisher.
4. Developer Information:
   - A dedicated section with information about the developer and their photo.
5. UX and Design:
   - Adhere to basic UX design and ergonomics principles suitable for mobile devices.
""")

pdf.set_font("Arial", "B", 12)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 10, "3. Database Design", ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0)
pdf.multi_cell(0, 10, """
Entity: Book
Fields:
- Book ID (Primary Key)
- Author (Text)
- Title (Text)
- Year of Publication (Integer)
- Publisher's Address (Text)
- Number of Pages (Integer)

Entity: Contact
Fields:
- Contact ID (Primary Key)
- First Name (Text)
- Last Name (Text)
- Phone Number (Text)
- Email Address (Text)
- Address (Text)
""")

pdf.set_font("Arial", "B", 12)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 10, "4. Calculations and Queries", ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0)
pdf.multi_cell(0, 10, """
- Display book titles older than 10 years.
- Calculate the percentage of selected books compared to the total number of books.
- Identify contacts whose last name ends with "ko".
- Provide the address of the selected publisher.
""")

pdf.set_font("Arial", "B", 12)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 10, "5. Geospatial Data Processing", ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0)
pdf.multi_cell(0, 10, """
The application will calculate and display the route from the current location to a user-specified location using geospatial APIs.
""")

pdf.set_font("Arial", "B", 12)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 10, "6. Developer Information", ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0)
pdf.multi_cell(0, 10, """
The application will include a dedicated section with information about the developer, including their name, biography, and photo.
""")

# Save the PDF to file
output_path = "Software_Requirements_Specification.pdf"
pdf.output(output_path)

