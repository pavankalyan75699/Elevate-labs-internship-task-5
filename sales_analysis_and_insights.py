import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('sales_data.csv')
df.head()
df.shape
df.info()
df.describe()
df.isnull()
category_sales = df.groupby('Category')['Sales'].sum()
df[df['Region'] == 'South']
df.groupby('Category')['Sales'].sum().plot(kind='bar')
plt.figure(figsize=(10, 6))  # Width x Height in inches
category_sales.plot(kind='bar', color='skyblue')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()


