import pandas

async def grouping(collection, group_type):
    grp_type = {'month': 'MS', 'day': 'D', 'hour': 'h'}
    df = pandas.DataFrame(collection)
    grouped = df.groupby([pandas.Grouper(key='dt', freq=grp_type[group_type])])['value'].sum()
    labels = list(grouped.index.strftime("%Y-%m-%dT%H:%M:%S"))
    dataset = list(grouped)
    result = {'dataset': dataset, 'labels': labels}
    return result