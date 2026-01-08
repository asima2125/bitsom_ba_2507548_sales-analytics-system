# Sales Analytics System

A Python-based Sales Analytics System that reads messy sales transaction data, cleans and validates it, performs detailed sales analysis, integrates external product data using an API, and generates comprehensive business reports.

This project is developed as part of **Module 3: Python Programming Assignment** and demonstrates practical usage of Python fundamentals such as file handling, data structures, functions, API integration, and error handling.

---

## Project Features

- Handles non-UTF-8 encoded data files
- Cleans and validates messy sales transaction data
- Filters transactions based on user input
- Performs sales analytics and trend analysis
- Integrates external product data using DummyJSON API
- Enriches sales data with API information
- Generates a structured and formatted sales report
- Saves processed and enriched data to files

---

## Project Structure

sales-analytics-system \
├── main.py \
├── README.md \
├── requirements.txt \
├── utils \
│ ├── init.py \
│ ├── file_handler.py \
│ ├── data_processor.py \
│ └── api_handler.py \
├── data \
│ ├── sales_data.txt \
│ └── enriched_sales_data.txt \
└── output \
│ ├── sales_report.txt \
├──END

---

## Requirements

- Python 3.8 or higher
- Internet connection (for API integration)

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

- From the project root directory, run:

```bash
python main.py
```

---

## Program Workflow

- Displays a welcome message

- Reads the sales data file with encoding handling

- Parses and cleans raw transaction data

- Displays available regions and transaction amount range

- Asks user whether to apply filters

- Validates transactions based on defined rules

- Performs sales analytics:

  - Total revenue

  - Region-wise sales

  - Top-selling products

  - Customer analysis

  - Daily sales trends

  - Peak sales day

  - Low-performing products

- Fetches product data from DummyJSON API

- Enriches sales data with API information

- Saves enriched sales data to file

- Generates a comprehensive sales report

- Displays success messages on completion

---

## Data Cleaning & Validation Rules

### Invalid records are removed if:

- Quantity ≤ 0

- UnitPrice ≤ 0

- Missing CustomerID or Region

- TransactionID does not start with T

- ProductID does not start with P

- CustomerID does not start with C

### Valid records are cleaned by:

- Removing commas from product names

- Removing commas from numeric values

- Converting Quantity to int

- Converting UnitPrice to float

- Skipping empty or malformed rows

---

## API Integration

- Uses DummyJSON Products API

- Fetches up to 100 products

- Maps API product data to sales data using numeric ProductID

- Handles missing or unmatched products gracefully

- Adds the following enrichment fields:

  - API_Category

  - API_Brand

  - API_Rating

  - API_Match

---

## Output Files

### 1. Enriched Sales Data

#### Location: data/enriched_sales_data.txt

#### Contains original sales data along with API enrichment fields in pipe-delimited format.

---

### 2. Sales Analytics Report

#### Location: output/sales_report.txt

#### Includes:

- Report header and generation timestamp

- Overall sales summary

- Region-wise performance

- Top-selling products

- Peak sales day

- API enrichment summary

---

## Error Handling

- Handles file not found and encoding errors

- Handles malformed data rows

- Handles API connection failures gracefully

- Prevents program crashes using try-except blocks

- Validates user input for filtering options

---

## Submission Notes

- Repository name: `bitsom_ba_2507548_sales-analytics-system`

- Repository visibility: Public

- All required files and folders included

- No hardcoded file paths

- Project runs end-to-end without errors

- Output files generated successfully
