import sqlite3

def create_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # SQL statements for table creation with Hyperlink fields
    tables_to_create = [
        """CREATE TABLE IF NOT EXISTS Chapters (ChapterID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                ChapterTitle TEXT, 
                                                ChapterDescription TEXT,
                                                Clause TEXT, 
                                                Formula TEXT, 
                                                Tables TEXT, 
                                                Hyperlink TEXT);""",
        """CREATE TABLE IF NOT EXISTS Formulas (FormulaID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                ChapterID INTEGER, 
                                                ClauseID INTEGER, 
                                                FormulaContent TEXT, 
                                                FormulaDescription TEXT, 
                                                Hyperlink TEXT, 
                                                FOREIGN KEY (ChapterID) REFERENCES Chapters(ChapterID), 
                                                FOREIGN KEY (ClauseID) REFERENCES Clauses(ClauseID));""",
        """CREATE TABLE IF NOT EXISTS CalculationSheets (CalculationSheetID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                CalculationSheetTitle TEXT, 
                                                CalculationSheetContent TEXT,
                                                Tables TEXT, 
                                                Hyperlink TEXT);""",
        """CREATE TABLE IF NOT EXISTS Reports (ReportID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                ReportTitle TEXT, 
                                                ReportDescription TEXT, 
                                                Clause TEXT, 
                                                Formula TEXT, 
                                                Tables TEXT, 
                                                Hyperlink TEXT);""",
        """CREATE TABLE IF NOT EXISTS FieldData (FieldDataID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                FieldDataTitle TEXT, 
                                                FieldDataContent TEXT, .
                                                Hyperlink TEXT);""",
        """CREATE TABLE IF NOT EXISTS Specifications (SpecificationID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                SpecificationTitle TEXT, 
                                                SpecificationContent TEXT, 
                                                Hyperlink TEXT);""",
        """CREATE TABLE IF NOT EXISTS Tables (TableID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                TableTitle TEXT, 
                                                TableContent TEXT, 
                                                Hyperlink TEXT);"""
    ]
    
    # Execute each table creation statement
    for table_creation_sql in tables_to_create:
        cursor.execute(table_creation_sql)
    
    conn.commit()
    conn.close()

def add_item(db_path, table_name, item_data):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        columns = ', '.join(item_data.keys())
        placeholders = ', '.join('?' * len(item_data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        cursor.execute(query, tuple(item_data.values()))
        
        conn.commit()
        print(f"Item successfully added to the {table_name}.")
        
    except sqlite3.Error as e:
        print("SQLite error:", e)
    
    finally:
        if conn:
            conn.close()

# Example usage
db_path = 'CE_Data.db'

# Create database and tables
create_database(db_path)

# Define sample data for each table with Hyperlink fields
chapter_data = {'ChapterTitle': 'CHAPTER 4. INTRODUCTION',
                'ChapterDescription': 'a description of the chapter',
                'Clause': 'Clause 4.1. Rvalues',
                'Formula': 'c+cc',
                'Tables': 'Table 2.4. Rvalues',
                'Hyperlink': 'https://example.com/chapter4'}

formula_data = {'ChapterID': 1,
                'ClauseID': 1, 
                'FormulaContent': 'F = m * a',
                'FormulaDescription': "Newton's Second Law of Motion",
                'Hyperlink': 'https://example.com/formula1'}

calculation_sheet_data = {'CalculationSheetTitle': 'Sheet 1',
                          'CalculationSheetContent': 'Calculations for beam strength',
                          'Tables': 'Table 2.4. Rvalues',
                          'Hyperlink': 'https://example.com/sheet1'}

report_data = {'ReportTitle': 'CHAPTER 4. INTRODUCTION',
               'ReportDescription': 'a description of the chapter',
               'Clause': 'Clause 4.1. Rvalues',
               'Formula': 'c+cc', 
               'Tables': 'Table 2.4. Rvalues',
               'Hyperlink': 'https://example.com/chapter4'}

field_data = {'FieldDataTitle': 'Field Data 1',
              'FieldDataContent': 'Soil analysis data',
              'Hyperlink': 'https://example.com/field1'}

specification_data = {'SpecificationTitle': 'Specification 1', 
                      'SpecificationContent': 'Material specifications', 
                      'Hyperlink': 'https://example.com/spec1'}

table_data = {'TableTitle': 'Table 1', 
              'TableContent': 'Load distribution', 
              'Hyperlink': 'https://example.com/table1'}

# Add sample data to each table
table_data_list = [
    ('Chapters', chapter_data),
    #('Formulas', formula_data),
    #('CalculationSheets', calculation_sheet_data),
    #('Reports', report_data),
    #('FieldData', field_data),
    #('Specifications', specification_data),
    #('Tables', table_data)
]

# Loop through the list and add each item to its respective table
for table_name, item_data in table_data_list:
    add_item(db_path, table_name, item_data)
