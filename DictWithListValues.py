# Output:
# { 'total' : ['mean', 'min', 'max', 'var'],
#    'speeding' :['mean', 'min', 'max', 'var'],
#    'alcohol' :['mean', 'min', 'max', 'var'],
#    'not_distracted' :['mean', 'min', 'max', 'var'],
#    'no_previous' :['mean', 'min', 'max', 'var'],
#    'ins_premium' :['mean', 'min', 'max', 'var'],
#    'ins_losses' :['mean', 'min', 'max', 'var'],
#}


import seaborn as sns # type: ignore
df = sns.load_dataset("car_crashes")
print(df.columns)

num_cols=[col for col in df.columns if df[col].dtype != "O"] #Selecting numerical values in the dataframe
print(num_cols)

dic = {}

agg_list = [ "mean", "min", "max", "sum"]

for col in num_cols:
    dic[col] = agg_list
    print(f"{col}: {dic[col]}")

#   or

new_dic ={col: agg_list for col in num_cols}
print(new_dic)

print(df[num_cols].head())


print(df[num_cols].agg(new_dic)) #key value seperation
