import sqlite3
import pandas as pd

DB_PATH = "data/animal_shelter.db"
INTAKES_CSV = "data/Austin_Animal_Center_Intakes.csv"
OUTCOMES_CSV = "data/Austin_Animal_Center_Outcomes.csv"

def create_tables():
    """Create the tables for intakes and outcomes."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create Animal Intakes Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Animal_Intakes (
            animal_id TEXT PRIMARY KEY, 
            name TEXT, 
            datetime TEXT, 
            month_year TEXT,
            found_location TEXT,
            intake_type TEXT, 
            intake_condition TEXT, 
            animal_type TEXT,
            sex_upon_intake TEXT,
            age_upon_intake TEXT,
            breed TEXT,
            color TEXT
        )
    """)

    # Create Animal Outcomes Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Animal_Outcomes (
            animal_id TEXT PRIMARY KEY, 
            name TEXT, 
            datetime TEXT, 
            month_year TEXT,
            date_of_birth TEXT,
            outcome_type TEXT, 
            outcome_subtype TEXT,
            animal_type TEXT,
            sex_upon_outcome TEXT,
            age_upon_outcome TEXT,
            breed TEXT,
            color TEXT,
            FOREIGN KEY (animal_id) REFERENCES Animal_Intakes(animal_id)
        )
    """)

    conn.commit()
    conn.close()

def load_csv_to_db():
    """Load data from CSV files into SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Load Intake Data
    intakes_df = pd.read_csv(INTAKES_CSV, encoding="ISO-8859-1")
    intakes_df = intakes_df.fillna("Unknown")  # Handle missing values

    for _, row in intakes_df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO Animal_Intakes 
            (animal_id, name, datetime, month_year, found_location, intake_type, intake_condition, animal_type, sex_upon_intake, age_upon_intake, breed, color) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["Animal ID"], row["Name"], row["DateTime"], row["MonthYear"],
            row["Found Location"], row["Intake Type"], row["Intake Condition"],
            row["Animal Type"], row["Sex upon Intake"], row["Age upon Intake"],
            row["Breed"], row["Color"]
        ))

    # Load Outcome Data
    outcomes_df = pd.read_csv(OUTCOMES_CSV, encoding="ISO-8859-1")
    outcomes_df = outcomes_df.fillna("Unknown")  # Handle missing values

    for _, row in outcomes_df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO Animal_Outcomes 
            (animal_id, name, datetime, month_year, date_of_birth, outcome_type, outcome_subtype, animal_type, sex_upon_outcome, age_upon_outcome, breed, color) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["Animal ID"], row["Name"], row["DateTime"], row["MonthYear"],
            row["Date of Birth"], row["Outcome Type"], row["Outcome Subtype"],
            row["Animal Type"], row["Sex upon Outcome"], row["Age upon Outcome"],
            row["Breed"], row["Color"]
        ))
def fetch_all_animals():
    """Retrieve all intake records from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("✅ Querying Animal_Intakes table...")  # Debugging Log
    
    cursor.execute("SELECT * FROM Animal_Intakes")
    records = cursor.fetchall()
    conn.close()
          
    return records

def insert_animal(animal_id, name, datetime, month_year, found_location, intake_type, intake_condition, animal_type, sex_upon_intake, age_upon_intake, breed, color):
    """Insert an animal record into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT OR IGNORE INTO Animal_Intakes 
        (animal_id, name, datetime, month_year, found_location, intake_type, intake_condition, animal_type, sex_upon_intake, age_upon_intake, breed, color) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (animal_id, name, datetime, month_year, found_location, intake_type, intake_condition, animal_type, sex_upon_intake, age_upon_intake, breed, color))
    
    conn.commit()
    conn.close()
    
    print("✅ Data successfully loaded into the database!")
