import plotly.graph_objects as go
from plotly.tools import make_subplots
import random
import pandas as pd
import plotly.express as px


def draw_figure1():
    df = px.data.tips()
    fig_moves_left = px.line(df, x=df.index, y='total_bill', color='sex', title="Title", template='plotly_white',
                             width=1400, height=400, color_discrete_sequence=['lightseagreen', '#de465f'],
                             labels={
                                 'index': "order number",
                                 "total_bill": "Total bill",
                                 "sex": "gender"
                             })
    fig_moves_left.update_layout(font=dict(
        size=22), legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1))
    fig_moves_left.show()

# --------

def draw_figure2():
    x_values = ['unit' + str(i) for i in range(1, 9)]

    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{}, {}]],

        subplot_titles=('Group1 vs. Group2', 'Group3 vs. Group4 (Android)'))

    fig.add_trace(go.Scatter(x=x_values, y=[47, 36, 31, 25, 20, 19, 17, 16],
                             mode='lines+markers+text',
                             name='Group1 name',
                             text=[str(47) + '%', str(36) + '%', str(31) + '%', str(25) + '%', str(20) + '%',
                                   str(19) + '%', str(17) + '%', str(16) + '%'],
                             textposition="bottom center",
                             marker=dict(color='green')),
                  row=1, col=1)

    fig.add_trace(go.Scatter(x=x_values, y=[44, 37, 33, 28, 23, 21, 18, 17],
                             mode='lines+markers+text',
                             name='Group2 name',
                             text=[str(44) + '%', str(37) + '%', str(33) + '%', str(28) + '%', str(23) + '%',
                                   str(21) + '%', str(18) + '%', str(17) + '%'],
                             textposition="top center",
                             marker=dict(color='blue')),
                  row=1, col=1)

    fig.add_trace(go.Scatter(x=x_values, y=[46, 33, 30, 27, 25, 23, 18, 16],
                             mode='lines+markers+text',
                             name='Group3 name',
                             text=[str(46) + '%', str(33) + '%', str(30) + '%', str(27) + '%', str(25) + '%',
                                   str(23) + '%', str(18) + '%', str(16) + '%'],
                             textposition="bottom center"),
                  row=1, col=2)

    fig.add_trace(go.Scatter(x=x_values, y=[44, 34, 29, 26, 24, 24, 22, 21],
                             mode='lines+markers+text',
                             name='Group4 name',
                             text=[str(44) + '%', str(34) + '%', str(29) + '%', str(26) + '%', str(24) + '%',
                                   str(24) + '%', str(22) + '%', str(21) + '%'],
                             textposition="top center"),
                  row=1, col=2)

    fig.update_layout(
        height=500, width=1200,
        showlegend=True,
        yaxis_title='values',
        title_text="Title name",

    )

    fig.show()

# --------
