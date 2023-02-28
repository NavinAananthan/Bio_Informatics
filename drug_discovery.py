import pandas as pd
from chembl_webresource_client.new_client import new_client


# Target search for corono virus
target=new_client.target
target_query=target.search('coronavirus')
targets=pd.DataFrame.from_dict(target_query)


# We are choosing th single protien as the the selected target
selected_target=targets.target_chembl_id[4]
print(selected_target)


# We are retriving the CHEMBL3927 proteins that are reported as IC50
activity=new_client.activity
res=activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")
df=pd.DataFrame.from_dict(res)

#to verify there are only IC50 standard type
print(df.standard_type.unique())

df.to_csv('bioactivity_data.csv',index=False)