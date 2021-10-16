
import plotly.graph_objects as go
from plotly.tools import make_subplots
import random
import pandas as pd
import plotly.express as px


def draw_figure1():
    fig_funnel = go.Figure()

    fig_funnel.add_trace(go.Funnel(
        name='Group1',
        y=["1st day", "2d day", "3d day", "4th day", '5th day', '6th day'],
        x=[100 * 7,
           58 * 7,
           37 * 7,
           29 * 7,
           24 * 7,
           15 * 7],
        textinfo="value+percent initial",
        text=['a', 'b', 'c', 'd'],
        marker={"color": "#e7d5f5"})
    )

    fig_funnel.add_trace(go.Funnel(
        name='Group2',
        orientation="h",
        y=["1st day", "2d day", "3d day", "4th day", '5th day', '6th day'],
        x=[100 * 7,
           55 * 7,
           40 * 7,
           30 * 7,
           25 * 7,
           20 * 7],
        textposition="inside",
        textinfo="value+percent initial",
        marker={"color": "teal"})
    )

    fig_funnel.update_layout(
        title="Order's funnel",
        xaxis_title="",
        yaxis_title="",
        legend_title="",
        width=1000,
        height=500,
        font=dict(size=20), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
        , legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1))

    fig_funnel.show()
# --------  funnels subplots:

def draw_figure2():
    fig = go.Figure()

    fig = make_subplots(
        rows=2, cols=3,
        specs=[[{}, {}, {}],
               [{}, {}, {}]],
        subplot_titles=(
        'Low-end iOS', "Regular iOS", "High-end iOS", "Low-end Android", 'Regular Android', 'High-end Android'))

    fig.add_trace(go.Funnel(
        text=["1st day", "2nd day", "7th day"],
        y=["1st day", "2nd day", "7th day"],
        x=[1716, 991, 503],
        textposition="inside",
        textinfo="percent initial",
        opacity=0.85, marker={"color": ["#8977d5", "#e7d5f5", "lightseagreen", "teal", "silver"],
                              "line": {"width": [2, 2, 3, 3, 1, 1],
                                       "color": ["lightseagreen", "lightseagreen", "red", "lightseagreen",
                                                 "lightseagreen"]}},
        connector={"line": {"color": "#e7d5f5", "width": 1}}
    ), row=1, col=1)

    fig.add_trace(go.Funnel(
        text=["1st day", "2nd day", "7th day"],
        y=["1st day", "2nd day", "7th day"],
        x=[2345, 1267, 392],
        textposition="inside",
        textinfo="percent initial",
        opacity=0.85, marker={"color": ["#8977d5", "#e7d5f5", "lightseagreen", "teal", "silver"],
                              "line": {"width": [2, 2, 3, 3, 1, 1],
                                       "color": ["lightseagreen", "lightseagreen", "lightseagreen", "lightseagreen",
                                                 "lightseagreen"]}},
        connector={"line": {"color": "#e7d5f5", "width": 1}}
    ), row=1, col=2)

    fig.add_trace(go.Funnel(
        text=["1st day", "2nd day", "7th day"],
        y=["1st day", "2nd day", "7th day"],
        x=[5203, 3390, 1555],
        textposition="inside",
        textinfo="percent initial",
        opacity=0.85, marker={"color": ["#8977d5", "#e7d5f5", "lightseagreen", "teal", "silver"],
                              "line": {"width": [2, 2, 3, 3, 1, 1],
                                       "color": ["lightseagreen", "lightseagreen", "lightseagreen", "lightseagreen",
                                                 "lightseagreen"]}},
        connector={"line": {"color": "#e7d5f5", "width": 1}}
    ), row=1, col=3)

    fig.add_trace(go.Funnel(
        text=["1st day", "2nd day", "7th day"],
        y=["1st day", "2nd day", "7th day"],
        x=[3607, 1593, 997],
        textposition="inside",
        textinfo="percent initial",
        opacity=0.85, marker={"color": ["#8977d5", "#e7d5f5", "lightseagreen", "teal", "#e7d5f5"],
                              "line": {"width": [2, 2, 3, 3, 1, 1],
                                       "color": ["lightseagreen", "lightseagreen", "red", "lightseagreen",
                                                 "lightseagreen"]}},
        connector={"line": {"color": "#e7d5f5", "width": 1}}
    ), row=2, col=1)

    fig.add_trace(go.Funnel(
        text=["1st day", "2nd day", "7th day"],
        y=["1st day", "2nd day", "7th day"],
        x=[4694, 3394, 1006],
        textposition="inside",
        textinfo="percent initial",
        opacity=0.85, marker={"color": ["#8977d5", "#e7d5f5", "lightseagreen", "teal", "silver"],
                              "line": {"width": [2, 2, 3, 3, 1, 1],
                                       "color": ["lightseagreen", "lightseagreen", "lightseagreen", "lightseagreen",
                                                 "lightseagreen"]}},
        connector={"line": {"color": "#e7d5f5", "width": 1}}
    ), row=2, col=2)

    fig.add_trace(go.Funnel(
        text=["1st day", "2nd day", "7th day"],
        y=["1st day", "2nd day", "7th day"],
        x=[3492, 2334, 889],
        textposition="inside",
        textinfo="percent initial",
        opacity=0.85, marker={"color": ["#8977d5", "#e7d5f5", "lightseagreen", "teal", "silver"],
                              "line": {"width": [2, 2, 3, 3, 1, 1],
                                       "color": ["lightseagreen", "lightseagreen", "lightseagreen", "lightseagreen",
                                                 "lightseagreen"]}},
        connector={"line": {"color": "#e7d5f5", "width": 1}}
    ), row=2, col=3)

    fig.update_layout(height=600, width=1000, font=dict(size=14), title_text="Group1+Group2 Churn by Device Category ",
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.show()

# -------