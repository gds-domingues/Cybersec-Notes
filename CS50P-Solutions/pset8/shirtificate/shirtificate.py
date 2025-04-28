# Import the CS50Shirtificate class from the 'fpdf' module for creating PDF documents
from fpdf import FPDF

class CS50Shirtificate(FPDF):
    def header(self):
        # Add a header to every page
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, 'C')

    def create_shirtificate(self, name):
        # Method to create a CS50 shirtificate with the given name

        # Set page settings
        self.add_page("P", "A4")
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font("Arial", size=12)

        # Add shirt image
        self.image("shirtificate.png", x=50, y=50, w=110)

        # Add user's name on top of the shirt in white text
        self.set_text_color(255, 255, 255)
        self.set_font("Arial", size=20)
        self.cell(0, 10, name, 0, 1, 'C')

        # Reset text color
        self.set_text_color(0, 0, 0)

    def save_pdf(self, filename):
        # Method to save the PDF to the specified filename
        self.output(filename)

def main():
    # Main function to execute the program

    # Get user's name
    user_name = input("Enter your name: ")

    # Create CS50Shirtificate instance
    pdf = CS50Shirtificate()

    # Create the shirtificate with the user's name
    pdf.create_shirtificate(user_name)

    # Save the PDF to shirtificate.pdf
    pdf.save_pdf("shirtificate.pdf")

if __name__ == "__main__":
    main()  # Execute the main function if the script is run as the main program

"""
The code imports the CS50Shirtificate class from the 'fpdf' module, which extends the FPDF class for creating PDF documents.
The CS50Shirtificate class contains three methods:
header(self): Adds a header to every page of the PDF with the title "CS50 Shirtificate."
create_shirtificate(self, name): Creates a shirtificate page with the user's name, adding an image of a shirt and placing the name on top of it.
save_pdf(self, filename): Saves the generated PDF to the specified filename.
The main() function prompts the user to enter their name, creates an instance of the CS50Shirtificate class, generates a shirtificate with the entered name, and saves the PDF as "shirtificate.pdf" using the save_pdf method.
The __name__ == "__main__" block ensures that the main() function is executed when the script is run as the main program.
"""