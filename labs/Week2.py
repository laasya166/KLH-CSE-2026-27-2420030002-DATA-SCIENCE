#%%
import pandas as pd
import numpy as np
df=pd.DataFrame({'Age':[25,30,np.nan,40,35],
                 'Department':['HR','Finance','Finance',np.nan,'IT']})
print(df)
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Department']=df['Department'].fillna(df['Department'].mode()[0])
print(df)
# %%
import pandas as pd
import numpy as np
df=pd.DataFrame({
    'Age':[25,30,np.nan,40,35],
    'Department':['HR','Finance','Finance',np.nan,'IT']
})
print("Original DataSet:")
print(df)
df_ffill=df.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)
# %%
import pandas as pd
import numpy as np
df=pd.DataFrame({
    'Age':[25,30,np.nan,40,35],
    'Department':['HR','Finance','Finance',np.nan,'IT']
})
print("Original DataSet:")
print(df)
df_bfill=df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)
# %%
import pandas as pd
import numpy as np
df=pd.DataFrame({
    "Age":[25,30,np.nan,40,35],
    "Department":["HR","Finance","Finance",np.nan,"IT"]
})
print ("Original DataSet:")
print(df)
df_drop_rows=df.dropna()
print("After dropping rows:\n", df_drop_rows)
# %%
df_drop_cols=df.dropna(axis=1)
print("After dropping columns\n",df_drop_cols)
# %%
df_drop_rows=df.dropna(axis=0)
print("After dropping rows\n",df_drop_rows)
# %%
import pandas as pd
df=pd.DataFrame({
    'ID':[1,2,2,3,4,4],
    'Name':['Alice','Bob','Bob','Charlie','David','David'],
    'Age':[25,30,30,35,40,40]
})
print("Original DataSet:")
print(df)
df_exact=df.drop_duplicates()
print('\nAfter dropping duplicates:\n',df_exact)
# %%
import pandas as pd
df=pd.DataFrame({
    'ID':[1,2,2,3,4,4],
    'Name':['Alice','Bob','Bob','Charlie','David','David'],
    'Age':[25,30,30,35,40,40]
})
print("Original Dataset")
print(df)
df_subset_id=df.drop_duplicates(subset=['ID'])
print('\nAfter dropping duplicates based on ID:\n',df_subset_id)
# %%
import pandas as pd 
df=pd.DataFrame({
    'Date':['2025-1-5','5/1/2025','Jan 5 2025','2025.1.5']
})
print("Original DataSet:")
print(df)
df['Date']=pd.to_datetime(df['Date'],errors='coerce').dt.strftime('%Y-%m-%d')
print("After converting Date column:")
print(df)
# %%
df=pd.DataFrame({
    'Name':['Alice','Bob','CHARLIE','DAVID']
})
df['Name_lower']=df['Name'].str.lower()
print(df)
df['Name_lower']=df['Name'].str.upper()
print(df)
# %%
