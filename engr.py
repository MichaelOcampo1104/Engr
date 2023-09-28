import sqlite3

def create_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    tables_to_create = [
        """CREATE TABLE IF NOT EXISTS TechRef (TechRefID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                Code TEXT,
                                                Topic TEXT, 
                                                Info TEXT,
                                                Hyperlink TEXT);""",
        """CREATE TABLE IF NOT EXISTS DesignReports (DesignReportID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                ReportTitle TEXT, 
                                                ReportDescription TEXT, 
                                                Clause TEXT, 
                                                Formula TEXT, 
                                                Tables TEXT, 
                                                Hyperlink TEXT);""",
        """CREATE TABLE IF NOT EXISTS Specifications (SpecificationID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                SpecificationTitle TEXT, 
                                                SpecificationContent TEXT, 
                                                Hyperlink TEXT);""",
        """CREATE TABLE IF NOT EXISTS Ref_Formula (FormulaID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                FormulaRef TEXT, 
                                                Formula TEXT, 
                                                FormulaDesc TEXT,
                                                FOREIGN KEY (TechRefID) REFERENCES TechRef(TechRefID));""",
        """CREATE TABLE IF NOT EXISTS Ref_Clause (ClauseID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                RefClause TEXT, 
                                                Clause TEXT,
                                                FOREIGN KEY (TechRefID) REFERENCES TechRef(TechRefID));""",
        """CREATE TABLE IF NOT EXISTS Ref_Table (TableID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                Ref_Table TEXT, 
                                                Table_Contents TEXT,
                                                FOREIGN KEY (TechRefID) REFERENCES TechRef(TechRefID));"""
    ]
    
    for table_creation_sql in tables_to_create:
        cursor.execute(table_creation_sql)
    
    conn.commit()
    conn.close()

def add_item(db_path, table_name, item_data):
    last_row_id = None
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        columns = ', '.join(item_data.keys())
        placeholders = ', '.join('?' * len(item_data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        cursor.execute(query, tuple(item_data.values()))
        
        conn.commit()
        last_row_id = cursor.lastrowid
        
    except sqlite3.IntegrityError:
        print("Integrity Error: Likely a duplicate or null primary key.")
    except sqlite3.OperationalError as e:
        print("SQLite error:", e)
    finally:
        if conn:
            conn.close()
    
    return last_row_id

def populate_formula_table(db_path, last_techref_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    formula_data = [
(last_techref_id, 
r"""\\chi^a+y^a = \\varkappa""",
r"""(D5.14)"""),

 
    ]
    
    try:
        cursor.executemany("INSERT INTO Ref_Formula (FormulaRef, Formula, FormulaDesc) VALUES (?, ?, ?)", formula_data)
        conn.commit()
        print("Formula data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def populate_clause_table(db_path, last_techref_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    clause_data = [
        (last_techref_id, r"""Clause 5.8.9(4) """),

    ]
    
    try:
        cursor.executemany("INSERT INTO Ref_Clause (RefClause, Clause) VALUES (?, ?)", clause_data)
        conn.commit()
        print("Clause data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def populate_table_contents(db_path, last_techref_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    table_data = [
(last_techref_id,
r"""Table 5.4. Values of the exponent a in equation (D5. 15)"""),

]
    
    try:
        cursor.executemany("INSERT INTO Ref_Table (Ref_Table, Table_Contents) VALUES (?, ?)", table_data)
        conn.commit()
        print("Table data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Function to prompt user for which tables to update
def get_user_choices():
    print("Select the tables to update (separate multiple choices with commas):")
    print("1 - TechRef")
    print("2 - Ref_Formula")
    print("3 - Ref_Clause")
    print("4 - Ref_Table")
    print("5 - Exit")
    
    return input("Enter your choices: ").split(',')

# Main code execution starts here
db_path = 'CE_Data.db'

create_database(db_path)

def set_autoincrement_start(db_path, table_name, start_value):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE sqlite_sequence SET seq = {start_value} WHERE name = '{table_name}';")
    conn.commit()
    conn.close()

# Set the starting value of AUTOINCREMENT for TechRef table to following the CURRENT sequence
set_autoincrement_start(db_path, 'TechRef', 100)

TechRef_data = {"Code": 'EC_2',"Topic": 'Table 5.4',"Info": 
r"""
Table 5.4. Values of the exponent a in equation (D5. 15)
Ned/Nrd|a
<0.1 |1.00
0.7| 1.5
1.0 |2.0
""",
}


table_data_list = [
    ('TechRef', TechRef_data),
]

last_techref_id = None

while True:
    user_choices = get_user_choices()
    
    for choice in user_choices:
        choice = choice.strip()
        
        if choice == '1':
            last_techref_id = add_item(db_path, 'TechRef', TechRef_data)
            print("TechRef data inserted successfully.")
            
        elif choice == '2':
            if last_techref_id is not None:
                populate_formula_table(db_path, last_techref_id)
            else:
                print("Please add TechRef data first.")
                
        elif choice == '3':
            if last_techref_id is not None:
                populate_clause_table(db_path, last_techref_id)
            else:
                print("Please add TechRef data first.")
                
        elif choice == '4':
            if last_techref_id is not None:
                populate_table_contents(db_path, last_techref_id)
            else:
                print("Please add TechRef data first.")
                
        elif choice == '5':
            print("Exiting.")
            exit(0)
        
        else:
            print(f"Invalid choice {choice}. Skipping.")

    another_round = input("Do you want to continue? (yes/no): ").strip().lower()
    if another_round != 'yes':
        print("Exiting.")
        break
