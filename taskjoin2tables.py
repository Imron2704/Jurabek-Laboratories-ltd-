import pandas as pds 

file2023 = "C:/Users/99890/Desktop/Jurabek laboratories(Ltd) 2025 documents/19.02.2025/Productbaseandsales/Januarysale2023.xlsx" 
file2024 = "C:/Users/99890/Desktop/Jurabek laboratories(Ltd) 2025 documents/19.02.2025/Productbaseandsales/Januarysale2024.xlsx" 

d2023 = pds.read_excel(file2023) 
d2024 = pds.read_excel(file2024) 

print(d2023) 
print(d2024) 

combined_df = pds.concat([d2023, d2024], ignore_index=True)
combined_df.to_excel("Januarysales2023and2024.xlsx", index=False) 
print(combined_df)






