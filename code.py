import csv
import json

# Sample broker data structure (paths to CSV files)
broker_data = {
    "kotak": "kotak.csv",
    "fyers": "fyers.csv",
    "icici": "icici.csv",
    "angel": "angel.csv",
    "zerodha": "zerodha.csv"
}

# Function to check ISIN or symbol in a single broker's data
def check_broker_for_isin_or_symbol(broker_name, filepath, input_isin=None, input_symbol=None, input_token=None, input_exchange=None):
    matches = []

    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check for ISIN match if provided
            if input_isin and row.get("ISIN") and row.get("ISIN").strip().lower() == input_isin.lower():
                matches.append(row)

            # Check for token match if no ISIN match or in addition
            elif input_token and row.get("token") and row.get("token").strip().lower() == input_token.strip().lower():
                matches.append(row)

    # Filter matches by exchange if there are multiple results and an exchange input is provided
    #if len(matches) > 1 and input_exchange:
        #matches = [row for row in matches if row.get("exchange") and row.get("exchange").strip().lower() == input_exchange.lower()]
    print(matches)

    if len(matches) > 1 and input_symbol:
        matches = [row for row in matches if row.get("name") and row.get("name").strip().lower().replace(" ","") == input_symbol.strip().lower().replace(" ","")]
    # Return the first match or None if no match found
    return matches[0] if matches else None

# Function to query brokers for ISIN or symbol
def query_brokers(input_isin=None, input_symbol=None, input_token=None, input_exchange=None):
    results = {}

    # Iterate through each broker's data and check for the ISIN or symbol
    for broker, filepath in broker_data.items():
        result = check_broker_for_isin_or_symbol(broker, filepath, input_isin, input_symbol, input_token, input_exchange)
        if result:
            results[broker] = result

    return results

# Function to handle user input and broker-specific extraction
def query_script_mapping(json_data):
    # Extract ISIN, symbol, token, and exchange from JSON data
    input_isin = json_data.get("ISIN")
    input_symbol = json_data.get("symbol")
    input_token = json_data.get("token")
    input_exchange = json_data.get("exchange")

    # Query brokers for the ISIN, symbol, or token
    results = query_brokers(input_isin, input_symbol, input_token, input_exchange)

    if results:
        print("Results found:")
        for broker, details in results.items():
            print(f"{broker.capitalize()}: {details}")
    else:
        print("No mapping found.")

def main():
    # Prompt user to input JSON data
    user_input = input("Please enter input: ")

    try:
        # Parse the JSON data from user input
        json_data = json.loads(user_input)

        query_script_mapping(json_data)
    except json.JSONDecodeError:
        print("Invalid JSON format. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
