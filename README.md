# Broker Script Mapping Tool

This tool takes JSON input containing ISIN, symbol, and token details for a script and checks corresponding CSV files for five brokers (Kotak, Fyers, ICICI, Angel, and Zerodha). It attempts to map the script across these brokers by checking the ISIN, token, and exchange for each broker's data.

## Prerequisites

- Python 3.x
- CSV files for brokers (`kotak.csv`, `fyers.csv`, `icici.csv`, `angel.csv`, `zerodha.csv`) with the following columns:
  - `token`
  - `instrumentName`
  - `ISIN`
  - `exchange`
  - `segment`

## Setup

1. Clone this repository or download the code files.
2. Ensure you have the necessary CSV files for each broker in the same directory as the script, or update the paths in the code if the files are stored elsewhere.

## Install Requirements

This script does not require any external dependencies beyond Python's standard library. If you're using a virtual environment, activate it first:

```bash
# Create a virtual environment (optional)
python -m venv venv

# Activate the virtual environment (optional)
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

python code.py
```
## Sample Input
```json
{
    "ISIN": "INE155A01022",
    "symbol": "TATAMOTORS",
    "token": "3456",
    "exchange": "NSE"
}
```



