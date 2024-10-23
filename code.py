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
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check for ISIN match first if provided
            if input_isin and row.get("ISIN") and row.get("ISIN").strip().lower() == input_isin.lower():
                return {
                    "broker": broker_name,
                    "instrumentToken": row.get("token"),
                    "instrumentName": row.get("instrumentName") or row.get("symbol"),
                    "ISIN": row.get("ISIN"),
                    "exchange": row.get("exchange"),
                    "segment": row.get("segment"),
                }
            
            # If no ISIN match, check for token match
            if input_token and row.get("token") and row.get("token").strip().lower() == input_token.lower():
                # Ensure that the exchange also matches
                if row.get("exchange") and input_exchange and row.get("exchange").strip().lower() == input_exchange.lower():
                    return {
                        "broker": broker_name,
                        "instrumentToken": row.get("token"),
                        "instrumentName": row.get("instrumentName") or row.get("symbol"),
                        "ISIN": row.get("ISIN"),
                        "exchange": row.get("exchange"),
                        "segment": row.get("segment"),
                    }
    
    # Return None if no match is found
    return None
# Function to query brokers for ISIN or symbol
def query_brokers(input_isin=None, input_symbol=None,input_token=None,input_exchange=None):
    results = {}
    
    # Iterate through each broker's data and check for the ISIN or symbol
    for broker, filepath in broker_data.items():
        result = check_broker_for_isin_or_symbol(broker, filepath, input_isin, input_symbol,input_token,input_exchange)
        if result:
            results[broker] = result
    
    return results

# Function to handle user input and broker-specific extraction
def query_script_mapping(json_data):
    # Extract ISIN and symbol from JSON data
    input_isin = json_data.get("ISIN")
    input_symbol = json_data.get("symbol")
    input_token = json_data.get("token")
    input_exchange = json_data.get("exchange")
    


    # Query brokers for the ISIN or symbol
    results = query_brokers(input_isin, input_symbol,input_token,input_exchange)

    if results:
        print(f"Results found for ISIN '{input_isin}' or symbol '{input_symbol}':")
        for broker, details in results.items():
            print(f"{broker.capitalize()}: {details}")
    else:
        print(f"No mapping found for ISIN '{input_isin}' or symbol '{input_symbol}'.")

def main():
    # Prompt user to input JSON data
    user_input = input("Please enter the JSON data: ")

    try:
        # Parse the JSON data from user input
        json_data = json.loads(user_input)

        # Call the function to query mappings using the provided JSON data
        query_script_mapping(json_data)
    except json.JSONDecodeError:
        print("Invalid JSON format. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()

