
import plotly.graph_objects as go
from plotly.tools import make_subplots
import random
import pandas as pd
import plotly.express as px
from random import randrange

# box plot by type


def draw_figure1():
    import plotly.express as px
    df = px.data.tips()
    fig = px.box(df, x="day", y="total_bill", color="smoker", title='Title', width=600, height=400,
                 template='plotly_white', color_discrete_sequence=['#de465f', 'lightseagreen'],
                 labels={
                     "total_bill": "total bill",
                     "tip": "tip",
                     "sex": "gender"
                 })
    fig.update_layout(font=dict(size=22),
                      legend=dict(
                          orientation="h",
                          yanchor="bottom",
                          y=1.02,
                          xanchor="right",
                          x=1))
    fig.update_traces(quartilemethod="exclusive")  # or "inclusive", or "linear" by default
    fig.show()
# -------------------

# box plot ,comparison by type (exp.level tries)

def draw_figure2():
    # data :
    df1 = pd.DataFrame(columns=['number', 'value'])
    for user in range(1, 80):
        for level_number in range(1, 101):
            data = {'number': [level_number], 'value': [randrange(28)]}
            df_row = pd.DataFrame.from_dict(data)
            df1 = pd.concat([df1, df_row])

    df1['type'] = 'type1'

    df2 = pd.DataFrame(columns=['number', 'value', 'type'])
    for user in range(1, 80):
        for level_number in range(1, 101):
            data = {'number': [level_number], 'value': [randrange(28)]}
            df_row = pd.DataFrame.from_dict(data)
            df2 = pd.concat([df2, df_row])
    df2['type'] = 'type2'
    df = pd.concat([df1, df2])
    df = df.sort_values('number')
    # Figure:
    # box plot tries


    fig_tries=px.box(df, x='number', y='value', color='type',title='Values by level number',template='plotly_white',  width=1400, height=400,  color_discrete_sequence=['#de465f','lightseagreen'],
                    labels={
                     "number": "Level",
                     "value": "Average value",
                     "type": "type"
                 })

    fig_tries.update_layout(font=dict(
        size=22),
    legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1))
    fig_tries.update_traces(quartilemethod="exclusive")
    fig_tries.show()
# -------------------

