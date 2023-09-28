import json
import pandas as pd
from io import StringIO

# Step 1: Read the existing JSON file
with open("Civil_Engineering_Formulas.json", "r") as read_file:
    data = json.load(read_file)

# Step 2: Edit the JSON data (Adding a new formula as an example)

# Initialize the JSON data structure
data = {
    "Formulas": [],
    "ReferenceBooks": [],
    "CalculationReports": [],
    "Papers": [],
    "FieldData": [],
    "Calc": [],
    "Calcs": [],
    "ExcelData": []
}

# Add a new formula as an example
new_formula = {
    "Name": "Chapter 1",
    "Symbol": "P",
    "Formula": "P = F / A",
    "Variables": [
        {
            "Symbol": "P",
            "Description": "Axial Load",
            "Units": "N"
        }
    ],
    "Context": "For columns and struts.",
    "References": ["Eurocode 4"],
    "Notes": "Assumes linear elastic behavior."
}
data['Formulas'].append(new_formula)

# Add a new reference book as an example
new_book = {
    "Title": "Eurocode Designers’ Guide Series",
    "Author": "R. S. Narayanan & A. Beeby",
    "Year": "2005",
    "Notes": "Focuses on reinforced concrete.",
    "Chapters": 
    [
        {
            "Name": "Chapter 1 Introduction",
            "Topics":     
            [
                {
                    "Topic Name":"1.1 Scope",
                    "content": """Eurocode 2, Design of Concrete Structures, will apply to the design of building and civil
                        engineering structures in plain, reinforced and prestressed concrete. The code has been
                        written in several parts, namely:
                        • EN 1992-1-1, General Rules and Rules for Buildings
                        * EN 1992-1-2, General Rules - Structural Fire Design
                        • EN 1992-2, Reinforced and Prestressed Concrete Bridges
                        • EN 1992-3, Liquid and Containment Structures.
                        EN 1992-1-1 has been written in such a way that the principles of the code will generally
                        apply to all the parts. The specific rules, which only apply to building structures, are
                        identified as such. Under the CEN (the European standards body) rules, other parts of
                        Eurocode 2 are allowed to identify those clauses in Part 1.1 which do not apply to that part
                        and provide other information that will complement Part 1.1.
                        This guide is concerned primarily with Part 1.1. Some limited information on Part 1.2 is
                        also provided in Chapter 12.
                        Part 1.1 covers in situ and precast structures using normal-weight or lightweight concrete.
                        It applies to plain, reinforced and prestressed concrete structures. Thus, many of the
                        separate parts of the ENV versions of the code covering the above topics have been brought
                        into one document. Part 1.1 has 12 main chapters and 10 annexes; Part 1-2 has six main
                        chapters and five annexes.
                        Compliance with the code will satisfy the requirements of the Construction Products
                        Directive in respect of mechanical resistance.""",
                    "Formula":
                    {
                        "D1":   [],
                        "D2":   []
                    },
                    
                    "Tables": 
                    {
                        "Table 1":[],
                        "Table 2":[]
                    }
                },
                {
                    "Topic Name": "1.2 Layout",
                    "content": """The code clauses are set out as Principles and Application Rules. Principles are identified by
                    the letter P following the paragraph number. Application Rulesare identified by a number in
                    parentheses.
                    Principles are general statements and definitions for which there are no alternatives. In
                    addition, they also include some requirements and analytical modelsfor which no alternative
                    is allowed unless specifically stated.
                    Application Rules are generally accepted methods, which follow the principles and satisfy
                    their requirements. It is permissible to use alternative design rules, provided that it can be
                    demonstrated that they comply with the relevant principles and are at least equivalent with
                    regard to structural safety, serviceability and durability to the rules in the code. This matter
                    should be approached with caution. A narrow interpretation of this requirement will provide no incentive to develop alternative rules. Equivalence could be defined more broadly as
                    meaning that the safety, serviceability' and durability that may be expected from using these
                    rules will be sufficient for the purpose. If this is accepted, procedures in the current national
                    codes are, by and large, likely to be acceptable, as the principles are likely to be similar.
                    Clearly, any alternative approach has to be acceptable to regulatory authorities. Provisions
                    of different codes should not be mixed without a thorough appraisal by responsible bodies. It
                    should also be noted that the design cannot be claimed to be wholly in accordance with the
                    Eurocode when an alternative rule is used.
                    Building regulations will not be harmonized across Europe, and safety in a country remains
                    the prerogative of individual nations. Therefore, in the Eurocode system, some parameters
                    and procedures are left open for national choice. These are referred to as Nationally
                    Determined Parameters (NDPs). These generally relate to safety factors, but not exclusively
                    so. Although at the outset of the conversion of ENVs into ENs, there was a desire by all
                    countries to keep the number of NDPs to a minimum, in practice it has proved difficult to
                    achieve this, and a number of parameters other than safety factors have also become NDPs.
                    The code provides recommended values for all NDPs. Each country is expected to state in
                    their National Annex to the code (which together with the code is likely to form the basis of
                    regulatory control in the country) whether the recommended value is to be changed. Where
                    the UK National Annexalters the recommended value of an NDP, it is identified in this guide.
                    Chapters are arranged generally by reference to phenomena rather than to the type of
                    element as in UK codes. For example, there are chapters on bending, shear, buckling, etc.,
                    but not on beams, slabs or columns. Such a layout is more efficient, as considerable
                    duplication is avoided. It also promotes a better understanding of structural behaviour.
                    However, some exceptions exist such as a chapter on detailing particular member types.""",
                    "Formula":
                    {
                        "D1":   [],
                        "D2":   []
                    },
                    
                    "Tables": 
                    {
                        "Table 1":[],
                        "Table 2":[]
                    }
                },
                {
                    "Topic Name": "1.3 Related Documents",
                    "content": """Eurocode 2 refers to a number of CEN standards and codes and some ISO standards where
                    relevant. The following are some of the more important:
                    • EN 1990, Basis of Structural Design
                    • EN 1991, Actions on Structures
                    • EN 206-1, Concrete Specification, Performance, Production and Conformity
                    • EN 10,080, Steel Reinforcement of Concrete
                    • EN 10,138, Prestressing Steels.
                    Eurocode 2 relies on EN 206-1 for the specification of concrete mixes to ensure durability
                    in various exposure conditions, which are also defined in the same document. In the UK, a
                    complementary standard, BS 8500, has been developed. Part 1 of this British standard
                    is written to assist anyone wishing to specify concrete to BS EN 206-1. Part 2 of this
                    complementary standard contains specification for materials and procedures that are outside
                    of European standardization but within national experience. This part supplements the
                    requirements of BS EN 206 -1.
                    ENV 13670, Execution of Concrete Structures,deals with workmanship aspects. It is due to
                    be converted into an EN.
                    In addition to the above, a number of product standards have been developed for
                    particular products - hollow core units, ribbed elements, etc. While the product standards
                    rely on Eurocode 2 for design matters, some supplementary design rules have been given in
                    some of them""",
                    "Formula":
                    {
                        "D1":   [],
                        "D2":   []
                    },
                    
                    "Tables": 
                    {
                        "Table 1":[],
                        "Table 2":[]
                    }
                },
                {
                    "Topic Name": "1.4 Terminology",
                    "content": """Generally, the language and terminology'employed will be familiar to most engineers. They
                    do not differ from the ENV. EN 1990 defines a number terms, which are applicable to all materials (actions, types of analysis, etc.). In addition, EN 1992-1-1 also defines particular
                    terms specifically applicable to Eurocode 2 A few commonly occurring features are noted
                    below:
                    • Loads are generally referred to as ‘actions’ to characterize the generalized format of the
                    code. Actions refer not only to the forces directly applied to the structure but also to
                    imposed deformations, such as temperature effect or settlement. These are referred to
                    as ‘indirect actions’, and the subscript ‘IND’ is used to identify this.
                    • Actions are further subdivided as permanent (G) (dead loads), variable (Q) (live loads
                    or wind loads) and accidental (A). Prestressing (P) is treated as a permanent action in
                    most situations.
                    • Action effects are the internal forces, stresses, bending moments, shear and deformations
                    caused by actions.
                    * Characteristic values of any parameter are distinguished by the subscript ‘k’. Design
                    values carry the subscript ‘d’, and take into account partial safety factors.
                    • The term ‘normative’ is used for the text of the standards that forms the requirements.
                    The term ‘informative’ is used only in relation to annexes, which seek to inform rather
                    than require.
                    • All the formulae and expressions in the code are in terms of the cylinder strength of
                    concrete. It is denoted byfck. The relationship between the cylinder and cube strengths is
                    set out within the code. The strength class refers to both cylinder and cube strengths, e.g.
                    C25/30 refers to a cylinder strength of 25 N/mm2 and a corresponding cube strength of
                    30 N/mm2. It is not anticipated that the quality control procedures for the production of
                    concrete will switch to cylinder strength where the cube strength is now used (e.g. as in
                    the UK).""",
                    "Formula":
                    {
                        "D1":   [],
                        "D2":   []
                    },
                    
                    "Tables": 
                    {
                        "Table 1":[],
                        "Table 2":[]
                    }
                }
            ]
        },
        {
            "Name": "Chapter 2: Basis of Design",
            "Topics":     
            [
                {
                    "Topic Name": "2.1 Notation",
                    "content": """In this manual symbols have been defined locally where they occur. However, the following
                    is a list of symbols, which occur throughout the document.
                    \\\\G_{j,k} is the characteristic value of the permanent action j
                    \\\\G_{j,inf} is the int lower characteristic value of a permanent action
                    \\\\G_{j,sup} is the upper characteristic value of a permanent action
                    \\\\Q_{k,i} is the characteristic value of the variable action i
                    \\\\A_{k} is the characteristic value of an accidental action
                    \\\\P_{k} is the characteristic value of prestressing force
                    \\\\gamma_{G,j} is the partial safety factor for permanent action j for persistent and transient design
                    situations
                    \\\\gamma_{GA,j} is the partial safety factor for permanent action j for accidental design situations
                    \\\\gamma_{Q,i} partial safety factor for variable action i
                    \\\\gamma_{p} partial safety factor for prestressing force
                    \\\\varphi_{0}, \\\\varphi_{1}, \\\\varphi_{2} are multipliers for the characteristic values of variable actions to produce
                    combination, frequent and quasi-permanent values, respectively, of variable
                    actions to be used in various verifications
                    \\\\aleph_{k} characteristic value of a material property
                    \\\\gamma_{M} partial safety factor for the material property, including model uncertainty""",
                    "Formula":
                    {
                        "D1":   [],
                        "D2":   []
                    },
                    
                    "Tables": 
                    {
                        "Table 1":[],
                        "Table 2":[]
                    }
                },
                {
                    "Topic Name": "1.1 Scope",
                    "content": """""",
                    "Formula":
                    {
                        "D1":   [],
                        "D2":   []
                    },
                    
                    "Tables": 
                    {
                        "Table 1":[],
                        "Table 2":[]
                    }
                },
                {
                    "Topic Name": "1.1 Scope",
                    "content": """""",
                    "Formula":
                    {
                        "D1":   [],
                        "D2":   []
                    },
                    
                    "Tables": 
                    {
                        "Table 1":[],
                        "Table 2":[]
                    }
                },
            ]
        },  
    ]
    
}
data['ReferenceBooks'].append(new_book)

# Add a new calculation report with tabulated data
new_calc_report = {
    "Title": "Load Analysis Report",
    "Author": "Jane Doe",
    "Year": "2022",
    "File": "load_analysis_report.pdf",
    "TabularData": [
        {
            "Parameter": "Load Type",
            "Value": "Dead Load",
            "Units": "N/m^2"
        },
        {
            "Parameter": "Load Magnitude",
            "Value": "5000",
            "Units": "N"
        }
    ],
    "Notes": "Based on Eurocode standards."
}
data['CalculationReports'].append(new_calc_report)

# Add a new field data with tabulated reports
new_field_data = {
    "Title": "Soil Test Data",
    "Location": "Site A",
    "Year": "2021",
    "TabularData": [
        {
            "Parameter": "Soil Type",
            "Value": "Clay",
            "Units": "N/A"
        },
        {
            "Parameter": "Shear Strength",
            "Value": "50",
            "Units": "kPa"
        }
    ],
    "Notes": "Conducted in accordance with geotechnical guidelines."
}
data['FieldData'].append(new_field_data)

Papers = {
    "Title": "Soil Test Data",
    "Location": "Site A",
    "Year": "2021",
    "TabularData": [
        {
            "Parameter": "Soil Type",
            "Value": "Clay",
            "Units": "N/A"
        },
        {
            "Parameter": "Shear Strength",
            "Value": "50",
            "Units": "kPa"
        }
    ],
    "Notes": "Conducted in accordance with geotechnical guidelines."
}
data['Papers'].append(Papers)

Calc = {
    "Title": "Soil Test Data",
    "Location": "Site A",
    "Year": "2021",
    "TabularData": [
        {
            "Parameter": "Soil Type",
            "Value": "Clay",
            "Units": "N/A"
        },
        {
            "Parameter": "Shear Strength",
            "Value": "50",
            "Units": "kPa"
        }
    ],
    "Notes": "Conducted in accordance with geotechnical guidelines."
}
data['Calc'].append(Calc)


Calcs = {
    "Title": "Soil Test Data",
}
data['Calcs'].append(Calcs)


#Activate the following line of code for CSV reading
''''# Read the CSV data into a DataFrame
csv_file_path = "Sample_CSV_Data.csv"

# Read the CSV data into a DataFrame
csv_df = pd.read_csv(csv_file_path)

# Convert the DataFrame to a list of dictionaries
csv_dict_list = csv_df.to_dict(orient='records')

# Add the CSV data to the JSON structure
data['ExcelData'].append({
    "Title": "Sample CSV Data",
    "Data": csv_dict_list
})'''



# Write the JSON data to a file
with open("Engineering_Data.json", "w") as write_file:
    json.dump(data, write_file, indent=4)
