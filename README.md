# Sales Analytics

A Python project that explores the sample sales dataset and generates summaries and charts for product-line and country sales.

## Requirements

- Python 3.9+
- Packages listed in `requirements.txt`

## Run

1. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

2. Run the analysis from the project directory:

   ```bash
   python sales_analaysis.py
   ```

The script prints dataset and sales summaries, then saves `sales_by_product.png`, `sales_distribution.png`, and `top_countries.png` in the project directory. It also displays the charts.

## Project files

- `sales_analaysis.py` - analysis and chart generation
- `sales_data_sample.xlsx` - input dataset
- `sales_by_product.png` - sales by product line
- `sales_distribution.png` - product-line sales distribution
- `top_countries.png` - top countries by sales
