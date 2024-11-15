# Constants
b = 2.897e-3  # Wien's constant in m*K
start_temp = 600
end_temp = 1100
temp_resolution = 0.1

# Generate lookup table
lookup_table = {}
for temp in range(start_temp, end_temp + 1, int(temp_resolution * 10)):
    temp_celsius = temp
    lambda_max = b / temp
    lookup_table[temp_celsius] = round(lambda_max * 1e6, 3)  # Convert to micrometers

# Print the lookup table
print("| Temperature (°C) | Peak Wavelength (μm) |")
print("|-------------------|-----------------------|")
for temp, wavelength in lookup_table.items():
    print(f"| {temp}               | {wavelength}                     |")



# Convert the lookup table to a DataFrame
df = pd.DataFrame(list(lookup_table.items()), columns=['Temperature (°C)', 'Peak Wavelength (μm)'])

# Save the DataFrame to an Excel file
excel_filename = 'peak_wavelength_lookup_table.xlsx'
df.to_excel(excel_filename, index=False)