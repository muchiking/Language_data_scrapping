import pandas as pd

# my_dict = {'book chapter': "Text"}
# Create a DataFrame
data = {
  "Book": "Genesis",
  "Text": "text"
}
# df = pd.DataFrame(my_dict)
# df
df = pd.DataFrame(data , index=[0])

print(df) 

# Write the DataFrame to an Excel file
df.to_excel('gen.xlsx', sheet_name='Sheet1')