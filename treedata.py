import pandas as pd
from sodapy import Socrata
from nta_lists import boro_lists
from config import TOKEN

# Netlify / Heroku
import os
# TOKEN = os.environ['TOKEN']

def percentage(part, whole):
  return 100 * float(part)/float(whole)

def nta_table_maker(nta, row_length):
    client = Socrata("data.cityofnewyork.us", TOKEN)
    results = client.get("uvpi-gqnh", nta_name=nta, limit=800000)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    droplist = []
    keepers = ['tree_id', 'spc_common', 'spc_latin', 'health', 'status','boroname', 'nta_name']

    for label, content in results_df.items():
        if label not in keepers:
            droplist.append(label)

    df = results_df.drop(droplist, 1)
    neighborhood_df = df[(df.nta_name == nta)]
    treecount = {}
    captrees = []
    for index, row in neighborhood_df.iterrows():
        if row['spc_common'] not in treecount:
            treecount[row['spc_common']] = [1]
            captrees.append(str(row['spc_common']).title())
        else: 
            treecount[row['spc_common']][0] += 1

    cap_dict = dict(zip(captrees, list(treecount.values())))
    treecount_sorted = dict(sorted(cap_dict.items(), key=lambda x: x[1], reverse=True))
    if 'Nan' in treecount_sorted:
        treecount_sorted.pop('Nan')
    trees_df_raw = pd.DataFrame.from_dict(treecount_sorted)
    trees_df = trees_df_raw.T
    trees_df.rename(columns={0: 'Number of Trees'}, inplace=True)
    # trees_df.drop(['Nan'], 0, inplace=True)
    trees = trees_df.head(row_length)
    trees_html = trees.to_html()
    return(trees_html)

def nta_pie_data(nta):
    client = Socrata("data.cityofnewyork.us", TOKEN)
    results = client.get("uvpi-gqnh", nta_name=nta, limit=800000)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    droplist = []
    keepers = ['tree_id', 'spc_common', 'spc_latin', 'health', 'status','boroname', 'nta_name']

    for label, content in results_df.items():
        if label not in keepers:
            droplist.append(label)

    df = results_df.drop(droplist, 1)
    neighborhood_df = df[(df.nta_name == nta)]
    total_trees = neighborhood_df.tree_id.nunique()
    treecount = {}
    captrees = []
    for index, row in neighborhood_df.iterrows():
        if row['spc_common'] not in treecount:
            treecount[row['spc_common']] = [1]
            captrees.append(str(row['spc_common']).title())
        else: 
            treecount[row['spc_common']][0] += 1

    cap_dict = dict(zip(captrees, list(treecount.values())))
    treecount_sorted = dict(sorted(cap_dict.items(), key=lambda x: x[1], reverse=True))
    if 'Nan' in treecount_sorted:
        treecount_sorted.pop('Nan')
    trees_df_raw = pd.DataFrame.from_dict(treecount_sorted)
    trees_df = trees_df_raw.T
    trees_df.rename(columns={0: 'Number of Trees'}, inplace=True)
    # trees = trees_df.head(row_length)
    top_five_trees = []
    top_five_count = []
    for count in range(5):
        top_five_trees.append(trees_df.index[count])
        top_five_count.append(trees_df.iloc[count, 0])
    top_five_sum = sum(top_five_count)
    top_five_trees.append('Others')
    top_five_count.append(total_trees-top_five_sum)
    return([top_five_trees, top_five_count])

# nta_pie_data('Bedford')

# print(neighborhood_df.tree_id.nunique())

