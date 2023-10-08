#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import pandas and numpy libraries
import pandas as pd
import numpy as np
warnings.filterwarnings("ignore")

# Read the csv file using pandas.read_csv function
# Specify the file name, the columns to use, and the header row
df = pd.read_csv("./biourja-efzrr-y7i38ed9-input .csv", usecols=["Plant_Name", "Forecast","Capacity"], header=0)


df


# In[2]:


df_E=df[df["Plant_Name"].str.startswith("E")]
df_E.reset_index(drop=True, inplace=True)
df_E


# In[3]:


df_N=df[df["Plant_Name"].str.startswith("N")]
df_N.reset_index(drop=True, inplace=True)
df_N


# In[4]:


df_W=df[df["Plant_Name"].str.startswith("W")]
df_W.reset_index(drop=True, inplace=True)
df_W


# In[5]:


df_S=df[df["Plant_Name"].str.startswith("S")]
df_S.reset_index(drop=True, inplace=True)
df_S


# In[6]:


Total_Capacity=12000
#This is the given contraint

East_constraint=2800

North_constraint=1500

West_constraint=2000

South_constraint=6500

#This constriants has to be rewised to satisfy the total constraint
Old_total=East_constraint+North_constraint+West_constraint+South_constraint



# In[7]:


New_E_con=(East_constraint/Old_total)*Total_Capacity

New_N_con=(North_constraint/Old_total)*Total_Capacity

New_W_con=(West_constraint/Old_total)*Total_Capacity

New_S_con=(South_constraint/Old_total)*Total_Capacity


# In[8]:


New_E_con


# In[9]:


New_N_con


# In[10]:


New_W_con


# In[11]:


New_S_con


# In[12]:


#For East Zone
total_forecast_east_old=df_E["Forecast"].sum()
total_forecast_east_old

#New_E_con


df_E["New_Forecast"]=(df_E["Forecast"]/total_forecast_east_old) * New_E_con


# In[13]:


#For North Zone
total_forecast_north_old=df_N["Forecast"].sum()
total_forecast_north_old

#New_N_con


df_N["New_Forecast"]=(df_N["Forecast"]/total_forecast_north_old) * New_N_con


# In[14]:


#For West Zone
total_forecast_west_old=df_W["Forecast"].sum()
total_forecast_west_old

#New_W_con


df_W["New_Forecast"]=(df_W["Forecast"]/total_forecast_west_old) * New_W_con


# In[15]:


#For South Zone
total_forecast_south_old=df_S["Forecast"].sum()
total_forecast_south_old

#New_W_con


df_S["New_Forecast"]=(df_S["Forecast"]/total_forecast_south_old) * New_S_con


# In[16]:


df_E


# In[17]:


df_N


# In[18]:


df_W


# In[19]:


df_S


# In[20]:


###Checking weather the total capicity is  sufficient to newforcast for North
nf_N=df_N["New_Forecast"].sum()

tc_N=df_N["Capacity"].sum()

print(nf_N)

print(tc_N)



# In[21]:


###Checking weather the total capicity is  sufficient to newforcast for East
nf_E=df_E["New_Forecast"].sum()

tc_E=df_E["Capacity"].sum()

print(nf_E)

print(tc_E)


# In[22]:


###Checking weather the total capicity is  sufficient to newforcast for West
nf_W=df_W["New_Forecast"].sum()

tc_W=df_W["Capacity"].sum()

print(nf_W)

print(tc_W)


# In[23]:


###Checking weather the total capicity is  sufficient to newforcast for South
nf_S=df_S["New_Forecast"].sum()

tc_S=df_S["Capacity"].sum()

print(nf_S)

print(tc_S)


# In[24]:


#Thus we just need to readjust the rows where the New_Capacity is greater than the Maxmum capacity and split the
# sum in the proportion of the row value to the whole region

#For df_E

df_E["Valid"]=np.where(df_E["New_Forecast"]<=df_E["Capacity"],1,0)

df_E




# In[25]:


df_E['Extra'] = np.where(df_E['Valid'] == 0, df_E['New_Forecast'] - df_E['Capacity'], 0)

# Calculate the total extra sum
extra_sum_E = df_E['Extra'].sum()

print("The total extra sum is:", extra_sum_E)


# In[26]:


# Step 1: Calculate total sum of 'New_Forecast' where 'Valid' equals 1
total_new_forecast = df_E.loc[df_E['Valid'] == 1, 'New_Forecast'].sum()

# Step 2: Calculate proportion of each 'New_Forecast' value
df_E['Proportion'] = df_E.loc[df_E['Valid'] == 1, 'New_Forecast'] / total_new_forecast

# Step 3: Distribute the extra sum across the 'New_Forecast' values
df_E['Distributed_Extra'] = df_E['Proportion'] * extra_sum_E

# Step 4: Add these calculated values to original 'New_Forecast'
df_E.loc[df_E['Valid'] == 1, 'New_Forecast'] += df_E['Distributed_Extra']

# Drop the helper columns
df_E.drop(columns=['Proportion', 'Distributed_Extra'], inplace=True)

df_E


# In[27]:


df_E.loc[df_E['Valid'] == 0, 'New_Forecast'] = df_E.loc[df_E['Valid'] == 0, 'Capacity']


# In[28]:


df_E


# In[29]:


df_E.drop(columns=['Valid', 'Extra'], inplace=True)


# In[30]:


df_E


# In[31]:


print(df_E["New_Forecast"].sum())


# In[32]:


#For df_N

df_N["Valid"]=np.where(df_N["New_Forecast"]<=df_N["Capacity"],1,0)

df_N


# In[33]:


df_N.drop(columns=["Valid"], inplace=True)

df_N


# In[34]:


#For df_W

df_W["Valid"]=np.where(df_W["New_Forecast"]<=df_W["Capacity"],1,0)

df_W


# In[35]:


df_W['Extra'] = np.where(df_W['Valid'] == 0, df_W['New_Forecast'] - df_W['Capacity'], 0)

# Calculate the total extra sum
extra_sum_W = df_W['Extra'].sum()

print("The total extra sum is:", extra_sum_W)


# In[36]:


# Step 1: Calculate total sum of 'New_Forecast' where 'Valid' equals 1
total_new_forecast = df_W.loc[df_W['Valid'] == 1, 'New_Forecast'].sum()

# Step 2: Calculate proportion of each 'New_Forecast' value
df_W['Proportion'] = df_W.loc[df_W['Valid'] == 1, 'New_Forecast'] / total_new_forecast

# Step 3: Distribute the extra sum across the 'New_Forecast' values
df_W['Distributed_Extra'] = df_W['Proportion'] * extra_sum_W

# Step 4: Add these calculated values to original 'New_Forecast'
df_W.loc[df_W['Valid'] == 1, 'New_Forecast'] += df_W['Distributed_Extra']

# Drop the helper columns
df_W.drop(columns=['Proportion', 'Distributed_Extra'], inplace=True)

df_W


# In[37]:


df_W.loc[df_W['Valid'] == 0, 'New_Forecast'] = df_W.loc[df_W['Valid'] == 0, 'Capacity']



df_W


df_W.drop(columns=['Valid', 'Extra'], inplace=True)

df_W

print(df_W["New_Forecast"].sum())



# In[38]:


df_W


# In[39]:


#For df_W

df_W["Valid"]=np.where(df_W["New_Forecast"]<=df_W["Capacity"],1,0)

df_W

#Here we need to readjust the vales again


# In[40]:


df_W['Extra'] = np.where(df_W['Valid'] == 0, df_W['New_Forecast'] - df_W['Capacity'], 0)

# Calculate the total extra sum
extra_sum_W = df_W['Extra'].sum()

print("The total extra sum is:", extra_sum_W)


# In[41]:


# Step 1: Calculate total sum of 'New_Forecast' where 'Valid' equals 1
total_new_forecast = df_W.loc[df_W['Valid'] == 1, 'New_Forecast'].sum()

# Step 2: Calculate proportion of each 'New_Forecast' value
df_W['Proportion'] = df_W.loc[df_W['Valid'] == 1, 'New_Forecast'] / total_new_forecast

# Step 3: Distribute the extra sum across the 'New_Forecast' values
df_W['Distributed_Extra'] = df_W['Proportion'] * extra_sum_W

# Step 4: Add these calculated values to original 'New_Forecast'
df_W.loc[df_W['Valid'] == 1, 'New_Forecast'] += df_W['Distributed_Extra']

# Drop the helper columns
df_W.drop(columns=['Proportion', 'Distributed_Extra'], inplace=True)

df_W


# In[42]:


df_W.loc[df_W['Valid'] == 0, 'New_Forecast'] = df_W.loc[df_W['Valid'] == 0, 'Capacity']



df_W


df_W.drop(columns=['Valid', 'Extra'], inplace=True)

df_W

print(df_W["New_Forecast"].sum())


# In[43]:


df_W


# In[44]:


#For df_W

df_W["Valid"]=np.where(df_W["New_Forecast"]<=df_W["Capacity"],1,0)

df_W


# In[45]:


df_W['Extra'] = np.where(df_W['Valid'] == 0, df_W['New_Forecast'] - df_W['Capacity'], 0)

# Calculate the total extra sum
extra_sum_W = df_W['Extra'].sum()

print("The total extra sum is:", extra_sum_W)


# In[46]:


# Step 1: Calculate total sum of 'New_Forecast' where 'Valid' equals 1
total_new_forecast = df_W.loc[df_W['Valid'] == 1, 'New_Forecast'].sum()

# Step 2: Calculate proportion of each 'New_Forecast' value
df_W['Proportion'] = df_W.loc[df_W['Valid'] == 1, 'New_Forecast'] / total_new_forecast

# Step 3: Distribute the extra sum across the 'New_Forecast' values
df_W['Distributed_Extra'] = df_W['Proportion'] * extra_sum_W

# Step 4: Add these calculated values to original 'New_Forecast'
df_W.loc[df_W['Valid'] == 1, 'New_Forecast'] += df_W['Distributed_Extra']

# Drop the helper columns
df_W.drop(columns=['Proportion', 'Distributed_Extra'], inplace=True)

df_W



# In[47]:


df_W.loc[df_W['Valid'] == 0, 'New_Forecast'] = df_W.loc[df_W['Valid'] == 0, 'Capacity']



df_W


df_W.drop(columns=['Valid', 'Extra'], inplace=True)

df_W

print(df_W["New_Forecast"].sum())




# In[48]:


df_W


# In[49]:


#For df_W

df_W["Valid"]=np.where(df_W["New_Forecast"]<=df_W["Capacity"],1,0)

df_W






df_W['Extra'] = np.where(df_W['Valid'] == 0, df_W['New_Forecast'] - df_W['Capacity'], 0)

# Calculate the total extra sum
extra_sum_W = df_W['Extra'].sum()

print("The total extra sum is:", extra_sum_W)



# Step 1: Calculate total sum of 'New_Forecast' where 'Valid' equals 1
total_new_forecast = df_W.loc[df_W['Valid'] == 1, 'New_Forecast'].sum()

# Step 2: Calculate proportion of each 'New_Forecast' value
df_W['Proportion'] = df_W.loc[df_W['Valid'] == 1, 'New_Forecast'] / total_new_forecast

# Step 3: Distribute the extra sum across the 'New_Forecast' values
df_W['Distributed_Extra'] = df_W['Proportion'] * extra_sum_W

# Step 4: Add these calculated values to original 'New_Forecast'
df_W.loc[df_W['Valid'] == 1, 'New_Forecast'] += df_W['Distributed_Extra']

# Drop the helper columns
df_W.drop(columns=['Proportion', 'Distributed_Extra'], inplace=True)

df_W








df_W.loc[df_W['Valid'] == 0, 'New_Forecast'] = df_W.loc[df_W['Valid'] == 0, 'Capacity']



df_W


df_W.drop(columns=['Valid', 'Extra'], inplace=True)

df_W

print(df_W["New_Forecast"].sum())




df_W


# In[50]:


for i in range(10):
  #For df_W

  df_W["Valid"]=np.where(df_W["New_Forecast"]<=df_W["Capacity"],1,0)


  df_W['Extra'] = np.where(df_W['Valid'] == 0, df_W['New_Forecast'] - df_W['Capacity'], 0)

  # Calculate the total extra sum
  extra_sum_W = df_W['Extra'].sum()


  # Step 1: Calculate total sum of 'New_Forecast' where 'Valid' equals 1
  total_new_forecast = df_W.loc[df_W['Valid'] == 1, 'New_Forecast'].sum()

  # Step 2: Calculate proportion of each 'New_Forecast' value
  df_W['Proportion'] = df_W.loc[df_W['Valid'] == 1, 'New_Forecast'] / total_new_forecast

  # Step 3: Distribute the extra sum across the 'New_Forecast' values
  df_W['Distributed_Extra'] = df_W['Proportion'] * extra_sum_W

  # Step 4: Add these calculated values to original 'New_Forecast'
  df_W.loc[df_W['Valid'] == 1, 'New_Forecast'] += df_W['Distributed_Extra']

  # Drop the helper columns
  df_W.drop(columns=['Proportion', 'Distributed_Extra'], inplace=True)





  df_W.loc[df_W['Valid'] == 0, 'New_Forecast'] = df_W.loc[df_W['Valid'] == 0, 'Capacity']






  df_W.drop(columns=['Valid', 'Extra'], inplace=True)








df_W


# In[51]:


df_W["New_Forecast"] = df_W["New_Forecast"].round(3)
df_W["Valid"]=np.where(df_W["New_Forecast"]<=df_W["Capacity"],1,0)


df_W
#Now all are valid


# In[52]:


df_W.drop(columns=['Valid'], inplace=True)


# In[53]:


df_W


# In[54]:


#For df_S

df_S["Valid"]=np.where(df_S["New_Forecast"]<=df_S["Capacity"],1,0)

df_S




# In[55]:


df_S['Extra'] = np.where(df_S['Valid'] == 0, df_S['New_Forecast'] - df_S['Capacity'], 0)

# Calculate the total extra sum
extra_sum_S = df_S['Extra'].sum()

print("The total extra sum is:", extra_sum_S)


# In[56]:


# Step 1: Calculate total sum of 'New_Forecast' where 'Valid' equals 1
total_new_forecast = df_S.loc[df_S['Valid'] == 1, 'New_Forecast'].sum()

# Step 2: Calculate proportion of each 'New_Forecast' value
df_S['Proportion'] = df_S.loc[df_S['Valid'] == 1, 'New_Forecast'] / total_new_forecast

# Step 3: Distribute the extra sum across the 'New_Forecast' values
df_S['Distributed_Extra'] = df_S['Proportion'] * extra_sum_S

# Step 4: Add these calculated values to original 'New_Forecast'
df_S.loc[df_S['Valid'] == 1, 'New_Forecast'] += df_S['Distributed_Extra']


# In[57]:


# Drop the helper columns
df_S.drop(columns=['Proportion', 'Distributed_Extra'], inplace=True)

df_S


# In[58]:


df_S.loc[df_S['Valid'] == 0, 'New_Forecast'] = df_S.loc[df_S['Valid'] == 0, 'Capacity']



df_S


# In[59]:


df_S.drop(columns=['Valid', 'Extra'], inplace=True)

df_S

print(df_S["New_Forecast"].sum())




df_S


# In[60]:


df_S["Valid"]=np.where(df_S["New_Forecast"]<=df_S["Capacity"],1,0)

df_S


# In[61]:


df_S.drop(columns=["Valid"],inplace=True)


# In[62]:


df_S


# In[63]:


df_E["New_Forecast"].sum()


# In[64]:


df_N["New_Forecast"].sum()


# In[65]:


df_W["New_Forecast"].sum()


# In[66]:


df_S["New_Forecast"].sum()


# In[67]:


df_output = pd.concat([df_E, df_N, df_W, df_S])
df_output.reset_index(drop=True, inplace=True)



# In[68]:


df_output


# In[69]:


df_output["New_Forecast"].sum()


# In[70]:


df_ans = df_output[['Plant_Name', 'New_Forecast']].copy()
df_ans = df_ans.rename(columns={'New_Forecast': 'Forecast'})


# In[71]:


df_ans


# In[72]:


df_ans["Forecast"].sum()


# In[73]:


# Assuming df_ans is your DataFrame
df_ans[['Plant_Name', 'Forecast']].to_csv('output.txt', index=False, header=False, sep=',')


# In[74]:


df_ans


# In[75]:


df_ans["Forecast"].sum()


# In[76]:


df_ans.to_csv("output.csv")

