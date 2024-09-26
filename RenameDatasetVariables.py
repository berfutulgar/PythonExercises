# before: ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

#after: ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns # type: ignore
df = sns.load_dataset("car_crashes")
print(df.columns)

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())
print(A)

df.columns=A

#list comprehension

df.columns=[col.upper() for col in df.columns]
print(df.columns)