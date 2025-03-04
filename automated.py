import pandas as pd
from fpdf import FPDF
from google.colab import files

# Function to upload file
def upload_file():
    uploaded = files.upload()
    file_path = list(uploaded.keys())[0]  # Get the uploaded file name
    return file_path

# Read data from a file
def read_data(file_path):
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        elif file_path.endswith(".json"):
            df = pd.read_json(file_path)
        elif file_path.endswith(".txt"):
            with open(file_path, "r") as file:
                lines = file.readlines()
            df = pd.DataFrame({"Content": [line.strip() for line in lines]})
        else:
            with open(file_path, "r", errors='ignore') as file:
                content = file.read()
            df = pd.DataFrame({"Content": content.splitlines()})
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Analyze data
def analyze_data(df):
    analysis = {
        "Total Rows": len(df),
        "Total Columns": len(df.columns),
        "Missing Values": df.isnull().sum().sum(),
        "Summary Statistics": df.describe(include='all').to_string()
    }
    return analysis

# Generate PDF report
def generate_pdf(report_data, output_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Data Analysis Report", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    for key, value in report_data.items():
        pdf.cell(0, 10, f"{key}:", ln=True, align="L")
        pdf.multi_cell(0, 10, str(value))
        pdf.ln(5)
    
    pdf.output(output_file)
    print(f"Report saved as {output_file}")

# Main function
def main():
    print("Please upload a data file...")
    file_path = upload_file()
    if file_path:
        output_file = "report.pdf"
        df = read_data(file_path)
        if df is not None:
            report_data = analyze_data(df)
            generate_pdf(report_data, output_file)

if name == "main":
    main()