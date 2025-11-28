# Campus Energy Dashboard

## Project Overview
This Python project processes electricity meter readings for multiple campus buildings, aggregates the data, and generates:

- Cleaned combined dataset  
- Daily and weekly energy summaries  
- Per-building statistical summary  
- A graphical dashboard (`dashboard.png`)  
- A text summary report  
- OOP-based building consumption reports

The program automatically reads **all CSV files** inside the `data/` directory. Each file name (without `.csv`) is treated as a building name.
