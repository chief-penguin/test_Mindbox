import pandas as pd


def create_report(orders, order_lines):
    report = pd.DataFrame()
    orders['DateTime'] =  pd.to_datetime(orders['DateTime'], format='%Y-%m-%d %H:%M:%S') # у меня этот столбец считывается как string, так что я конвертнула
    help_df = orders.join(order_lines.set_index('OrderId'), on='OrderId', how='inner')
    help_df = help_df[(help_df.DateTime>='2019-06-01 00:00:00') &
                                    (help_df.DateTime<'2019-07-01 00:00:00')]
    report['most_popular'] = help_df.groupby(['ProductId']).DateTime.count()
    report['total_revenue'] = help_df.groupby(['ProductId']).Price.agg(['sum'])
    h_df = help_df.groupby(['OrderId'], as_index=False).Price.sum()
    h_df.columns = ['OrderId', 'Sum_price']
    help_df = pd.merge(help_df, h_df, on='OrderId')
    report['avg_sum'] = help_df.groupby(['ProductId']).Sum_price.mean()
    return report