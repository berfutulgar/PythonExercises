import seaborn as sns # type: ignore
df = sns.load_dataset("car_crashes")
print(df.columns)

print([col for col in df.columns if "ins" in col ])

print([ "flag_" + col for col in df.columns if "ins" in col])

print([ "flag_" + col if "ins" in col else "no_flag_" + col for col in df.columns ])