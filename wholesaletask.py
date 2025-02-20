import pandas as pd 

file_path2704 = "C:/Users/99890/Desktop/Jurabek laboratories(Ltd) 2025 documents/17.02.2025/Productbaseandsales/Productbase.xlsx" 
file_path2003 = "C:/Users/99890/Desktop/Jurabek laboratories(Ltd) 2025 documents/17.02.2025/Productbaseandsales/Januarysale.xlsx" 

dl = pd.read_excel(file_path2704) 
dr = pd.read_excel(file_path2003) 

print(dr) 
print(dl) 

df_merged577 = dr.merge(dl[['Product_id', 'Promo','Group','Форма Вида']], on='Product_id', how='left') 
df_merged577.to_excel("wholesale.xlsx", index=False) 
print(df_merged577) 












