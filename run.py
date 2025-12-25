from data.data_loader import fetch_data, load_data

symbol = "SUZLON.NS"
start_date = "2025-01-01"

# download and save data
fetch_data(symbol, start_date)

# load data from CSV
df = load_data(symbol)

# print verification
print("Rows, Columns:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
