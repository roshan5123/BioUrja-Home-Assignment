# -*- coding: utf-8 -*-


# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Read the csv file using pandas.read_csv function
# Specify the file name, the columns to use, and the header row
df = pd.read_csv("./biourja-efzrr-y7i38ed9-input .csv", usecols=["Plant_Name", "Forecast","Capacity"], header=0)


df

df_E=df[df["Plant_Name"].str.startswith("E")]
df_E.reset_index(drop=True, inplace=True)
df_E

df_N=df[df["Plant_Name"].str.startswith("N")]
df_N.reset_index(drop=True, inplace=True)
df_N

df_W=df[df["Plant_Name"].str.startswith("W")]
df_W.reset_index(drop=True, inplace=True)
df_W

df_S=df[df["Plant_Name"].str.startswith("S")]
df_S.reset_index(drop=True, inplace=True)
df_S

Total_Capacity=12000
#This is the given contraint

East_constraint=2800

North_constraint=1500

West_constraint=2000

South_constraint=6500

#This constriants has to be rewised to satisfy the total constraint
Old_total=East_constraint+North_constraint+West_constraint+South_constraint

New_E_con=(East_constraint/Old_total)*Total_Capacity

New_N_con=(North_constraint/Old_total)*Total_Capacity

New_W_con=(West_constraint/Old_total)*Total_Capacity

New_S_con=(South_constraint/Old_total)*Total_Capacity

New_E_con

New_N_con

New_W_con

New_S_con

#For East Zone
total_forecast_east_old=df_E["Forecast"].sum()
total_forecast_east_old

#New_E_con


df_E["New_Forecast"]=(df_E["Forecast"]/total_forecast_east_old) * New_E_con

#For North Zone
total_forecast_north_old=df_N["Forecast"].sum()
total_forecast_north_old

#New_N_con


df_N["New_Forecast"]=(df_N["Forecast"]/total_forecast_north_old) * New_N_con

#For West Zone
total_forecast_west_old=df_W["Forecast"].sum()
total_forecast_west_old

#New_W_con


df_W["New_Forecast"]=(df_W["Forecast"]/total_forecast_west_old) * New_W_con

#For South Zone
total_forecast_south_old=df_S["Forecast"].sum()
total_forecast_south_old

#New_W_con


df_S["New_Forecast"]=(df_S["Forecast"]/total_forecast_south_old) * New_S_con

df_E

df_N

df_W

df_S

###Checking weather the total capicity is  sufficient to newforcast for North
nf_N=df_N["New_Forecast"].sum()

tc_N=df_N["Capacity"].sum()

print(nf_N)

print(tc_N)

###Checking weather the total capicity is  sufficient to newforcast for East
nf_E=df_E["New_Forecast"].sum()

tc_E=df_E["Capacity"].sum()

print(nf_E)

print(tc_E)

###Checking weather the total capicity is  sufficient to newforcast for West
nf_W=df_W["New_Forecast"].sum()

tc_W=df_W["Capacity"].sum()

print(nf_W)

print(tc_W)

###Checking weather the total capicity is  sufficient to newforcast for South
nf_S=df_S["New_Forecast"].sum()

tc_S=df_S["Capacity"].sum()

print(nf_S)

print(tc_S)

#Thus we just need to readjust the rows where the New_Capacity is greater than the Maxmum capacity and split the
# sum in the proportion of the row value to the whole region

#For df_E

df_E["Valid"]=np.where(df_E["New_Forecast"]<=df_E["Capacity"],1,0)

df_E

df_E['Extra'] = np.where(df_E['Valid'] == 0, df_E['New_Forecast'] - df_E['Capacity'], 0)

# Calculate the total extra sum
extra_sum_E = df_E['Extra'].sum()

print("The total extra sum is:", extra_sum_E)

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

df_E.loc[df_E['Valid'] == 0, 'New_Forecast'] = df_E.loc[df_E['Valid'] == 0, 'Capacity']

df_E

df_E.drop(columns=['Valid', 'Extra'], inplace=True)

df_E

print(df_E["New_Forecast"].sum())

#For df_N

df_N["Valid"]=np.where(df_N["New_Forecast"]<=df_N["Capacity"],1,0)

df_N

df_N.drop(columns=["Valid"], inplace=True)

df_N

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

#For df_W

df_W["Valid"]=np.where(df_W["New_Forecast"]<=df_W["Capacity"],1,0)

df_W

#Here we need to readjust the vales again

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

df_W["New_Forecast"] = df_W["New_Forecast"].round(3)
df_W["Valid"]=np.where(df_W["New_Forecast"]<=df_W["Capacity"],1,0)


df_W
#Now all are valid

df_W.drop(columns=['Valid'], inplace=True)

df_W

#For df_S

df_S["Valid"]=np.where(df_S["New_Forecast"]<=df_S["Capacity"],1,0)

df_S

df_S['Extra'] = np.where(df_S['Valid'] == 0, df_S['New_Forecast'] - df_S['Capacity'], 0)

# Calculate the total extra sum
extra_sum_S = df_S['Extra'].sum()

print("The total extra sum is:", extra_sum_S)

# Step 1: Calculate total sum of 'New_Forecast' where 'Valid' equals 1
total_new_forecast = df_S.loc[df_S['Valid'] == 1, 'New_Forecast'].sum()

# Step 2: Calculate proportion of each 'New_Forecast' value
df_S['Proportion'] = df_S.loc[df_S['Valid'] == 1, 'New_Forecast'] / total_new_forecast

# Step 3: Distribute the extra sum across the 'New_Forecast' values
df_S['Distributed_Extra'] = df_S['Proportion'] * extra_sum_S

# Step 4: Add these calculated values to original 'New_Forecast'
df_S.loc[df_S['Valid'] == 1, 'New_Forecast'] += df_S['Distributed_Extra']

# Drop the helper columns
df_S.drop(columns=['Proportion', 'Distributed_Extra'], inplace=True)

df_S

df_S.loc[df_S['Valid'] == 0, 'New_Forecast'] = df_S.loc[df_S['Valid'] == 0, 'Capacity']



df_S

df_S.drop(columns=['Valid', 'Extra'], inplace=True)

df_S

print(df_S["New_Forecast"].sum())




df_S

df_S["Valid"]=np.where(df_S["New_Forecast"]<=df_S["Capacity"],1,0)

df_S

df_S.drop(columns=["Valid"],inplace=True)

df_S

df_E["New_Forecast"].sum()

df_N["New_Forecast"].sum()

df_W["New_Forecast"].sum()

df_S["New_Forecast"].sum()

df_output = pd.concat([df_E, df_N, df_W, df_S])
df_output.reset_index(drop=True, inplace=True)

df_output

df_ans = df_output[['Plant_Name', 'New_Forecast']].copy()
df_ans = df_ans.rename(columns={'New_Forecast': 'Predicted_Forecast'})

df_ans

# Assuming df_ans is your DataFrame
df_ans[['Plant_Name', 'Predicted_Forecast']].to_csv('output.txt', index=False, header=False, sep=',')
df_ans

df.to_csv("output.csv")
