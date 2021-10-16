#  Bar chart horisontal subplots + histograms
import plotly.graph_objects as go
from plotly.tools import make_subplots
import random
import pandas as pd

def draw_figure_demo():
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=[2, 1, 4, 3]))
    fig.add_trace(go.Bar(y=[1, 4, 3, 2]))
    fig.update_layout(title = 'Hello Figure')
    fig.show()

def draw_figure1(d1 = [1,2,3,6,3,4], 
                    p1 = [1,2,3,1,1,1,3,3,3,9,9], 
                    d2 = [1,2,3,3,7,5,12,3,6], 
                    p2 = [1,2,3,0,7,0,0,7], 
                    groups = {"group6":3.3, "group5":10, "group4":7, "group3":13, "group2":14, "group1":4.5}):

    colors = ['lightslategray',] * 6
    colors[1] = 'crimson'
    colors[0] = 'crimson'

    fig = make_subplots(
        rows=4, cols=2,
        specs=[[{"rowspan": 2, "colspan": 2 ,"type": "bar"}, None],
            [None, None],
            [{}, {}],
            [{}, {}]],
        subplot_titles=('',"days used Group3", "days used Group5","days used Group4","days used Group6"))

    group_names = []
    group_values = []
    group_texts = []
    for key in groups.keys():
        group_names.append(key)
        group_values.append(groups[key])
        group_texts.append(f"{groups[key]} days")

    fig.add_trace(go.Bar(y = group_names,
                        x = group_values,
                        orientation='h',
                        name="all",
                        text=group_texts,
                        textposition='auto',
                        marker_color=colors),row=1, col=1,
                        )
    fig.add_trace(go.Histogram(y=d1,marker_color='rgb(158,202,225)',opacity=0.5,marker_line_width=1.5,histnorm='probability',name="d1 name"), row=3, col=1)
    fig.add_trace(go.Histogram(y=p1,marker_color='crimson',opacity=0.5,marker_line_width=1.5,  name="p1 name",histnorm='probability'), row=3, col=2)
    fig.add_trace(go.Histogram(y=d2,marker_color='rgb(158,202,225)',opacity=0.5,marker_line_width=1.5,histnorm='probability',  name="d2 name"), row=4, col=1)
    fig.add_trace(go.Histogram(y=p2,marker_color='crimson',opacity=0.5,marker_line_width=1.5, histnorm='probability', name="p2 name"), row=4, col=2)

    fig.update_layout(height=800, width=900, title_text="How many days did it took? (avg)",xaxis_title="days", font=dict(size=14))
    fig.show()


#     --------

def draw_figure2(statistics = {'group6_name': 34,'group5_name':23,'group4_name':65,'group3_name':12,'group2_name':34,'group1_name':23},
                             title_name="First event duration (Median)",
                             measure_unit = 'min'):

    # first session duration

    colors = ['lightslategray', ] * 6
    colors[1] = 'crimson'
    colors[0] = 'crimson'
    colors[3] = '#61e357'
    colors[2] = '#61e357'

    fig = make_subplots(
        rows=1, cols=1,
        specs=[[{}]],
        subplot_titles=(''))

    statistics_names = []
    statistics_values = []
    statistics_labels = []
    for key in statistics.keys():
        statistics_names.append(key)
        statistics_values.append(statistics[key])
        statistics_labels.append(f" {statistics[key]} {measure_unit}")

    fig.add_trace(go.Bar(y = statistics_names,
                         x = statistics_values,
                        orientation='h',
                        name = "all",
                        text = statistics_labels,
                        textposition='auto',
                        marker_color=colors), row=1, col=1,
                )

    fig.update_layout(height=400, width=600, title_text = title_name,
                    xaxis_title= measure_unit, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
                    )
    fig.show()


# ------


def draw_figure3(x_group1 = [i for i in range(1,101)],
                 y_group1 = random.sample(range(11, 67), 34),
                 y_retention=pd.Series(
                     [1, 0.43, 0.25, 0.20, 0.18, 0.15, 0.15, 0.14, 0.13, 0.10, 0.09, 0.09, 0.07, 0.06, 0.05]),
                 x_group2=[i for i in range(1, 101)],
                 y_group2 = random.sample(range(4, 67), 23),
                 lineplot_name = 'Relative Retention' ,
                 barplot_name1 = 'group1',
                 barplot_name2 = 'group2',
                 title_name = "   <b> Churn by Level  </b> ",
                 xlabel_name = 'Levels',
                 yaxis1_name = 'Relative churn',
                 yaxis2_name = 'absolut churn'
                 ):
    # -------- bar chart vertical, two axis, relative retention + churn by level for two groups

    ## Create figure with secondary y-axis

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(

        go.Scatter(
            x= x_group1,
            y= y_retention,
            legendgroup=lineplot_name,
            name = lineplot_name,
            line_color='#0df50d',
            line=dict( width=4)
        ),
            secondary_y=False)

    fig.add_trace(
        go.Bar(
            x=x_group1,
            y=y_group1,
            legendgroup= barplot_name1,
            name= barplot_name1,
            text=y_group1 ,
            textposition = 'outside',
            marker_color='#de465f',
            offsetgroup=0
        ),secondary_y=True
    )

    fig.add_trace(
        go.Bar(
            x=x_group2[:100],
            y=y_group2,
            legendgroup=barplot_name2,
            name=barplot_name2,
            text=y_group2 ,

            textposition = 'outside',
            marker_color='#fe9548',
            offsetgroup=0

        ),secondary_y=True)


    fig.update_layout(
        title_text= title_name,
        width = 1000,height = 700,
        font=dict(
            size=22
        ),legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')

    fig.update_yaxes(title_text= yaxis1_name, secondary_y=False)
    fig.update_yaxes(title_text= yaxis2_name, secondary_y=True,range=[0,120])
    fig.update_xaxes(title_text= xlabel_name)
    fig.show()

#  ---------

def draw_figure4(x_group1 = [i for i in range(1,30)],
                 y_group1 = random.sample(range(11, 190), 100),
                 x_group2=[i for i in range(1, 30)],
                 y_group2 = random.sample(range(3, 120), 100),
                 group1_name = 'Group1',
                 group2_name = "Group2",
                 title_name = "   <b> Orders by day </b> "):

    # ------- Bar chart vertical level tries comparison

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=x_group1,
        y=y_group1,
        name= group1_name,
        marker_color='#de465f',
        text=y_group1,
        textposition='outside'
    ))

    fig.add_trace(go.Bar(
        x=x_group2,
        y=y_group2,
        name=group2_name,
        marker_color='lightseagreen',
        text=y_group2,
        textposition='outside'
    ))


    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(barmode='group',title_text= title_name,
        width = 1400,height = 400,yaxis_title="orders",xaxis_title="day",paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            size=22
        ),legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1))
    fig.show()


def draw_figure5(x_values = ['day'+str(i) for i in range(1,15)],
    df1 = pd.Series([13,17.6, 22.8,25,27.8,30,32.5,34]),
    df2 = pd.Series([15,21, 25.6,29,32.8,35,36,37]),
     group1_name = 'Group1',
     group2_name = "Group2",
     title_name = "Value Group1 vs. Group2 (Cumulative)",
     yaxis_name = 'value (cumulative)',
     barplot_name = 'value difference'):

    # ---- Line + bar shared axis

    y_difference = df2 - df1

    ## Values visualisation
    fig_rounds2 = go.Figure()

    fig_rounds2.add_trace(
        go.Scatter(
            x=x_values,
            y=df1,
            mode='lines+markers+text',
            line=dict(color='green', width=3),
            name=group1_name,
            text=df1[0:8],
            textposition="bottom center",
            marker=dict(color='green')

        )
    )

    fig_rounds2.add_trace(
        go.Scatter(
            x=x_values,
            y=df2,
            line=dict(color='purple', width=3),
            name=group2_name,
            mode='lines+markers+text',
            text=df2,
            textposition="bottom center",
            marker=dict(color='purple')

        )
    )

    fig_rounds2.add_trace(go.Bar(x=x_values, y=y_difference,
                                 name= barplot_name))

    fig_rounds2.update_layout(
        height=500, width=800,
        showlegend=True,
        font=dict(size=16),
        title_text= title_name,
        yaxis_title= yaxis_name, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

    fig_rounds2.show()


    # -----

def draw_figure6(x_data = ['avg', 'median', 'P60', 'P75', 'P90'],
                 y1 = [14, 1.5, 11, 1, 5],
                 y2 = [3.3, 7, 0, 2, 3],
                 y3 = [7, 4, 6, 3, 4],
                 title_name = 'Title name'):

    color = ["#947da5", "lightsalmon", "#e7d5f5"]
    fig = make_subplots(rows=3, cols=1)

    fig.append_trace(go.Bar(x=x_data, y=y1, text=y1, textposition='auto',
                              marker=dict(color="#947da5")), row=1, col=1)

    fig.append_trace(go.Bar(x=x_data, y=y2, text=y2, textposition='outside',
                              marker=dict(color="lightsalmon")), row=2, col=1)

    fig.append_trace(go.Bar(x=x_data, y=y3, text=y3, textposition='outside',
                              marker=dict(color="#e7d5f5")), row=3, col=1)

    fig.update_layout(font=dict(size=20), width=600, height=700, paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',title_text=title_name)

    fig.show()


    # --------

def draw_figure7(set1 = {'Group1 name':4.5,'roup2 name':5.6,'Group3 name':3,'Group4 name':5.4,'Group5 name':2.3,'Group6 name':5.5},
                set2 = {'Group1 name':7,'roup2 name':8,'Group3 name':2,'Group4 name':5.4,'Group5 name':9,'Group6 name':6.7},
                 subplot_titles=('Subtitle1 name', 'Subtitle2 name'),
                 xaxis_title = "Speed Rank (avg)"
                 ):
    colors = ['green'] * 6
    colors[1] = 'crimson'
    colors[0] = 'crimson'
    colors[3] = '#61e357'
    colors[2] = '#61e357'

    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{}, {}]],

        subplot_titles=subplot_titles)

    set1_names = []
    set1_values = []
    set1_labels = []
    for key in set1.keys():
        set1_names.append(key)
        set1_values.append(set1[key])
        set1_labels.append(f'{set1[key]}')

    set2_names = []
    set2_values = []
    set2_labels = []
    for key in set2.keys():
        set2_names.append(key)
        set2_values.append(set2[key])
        set2_labels.append(f'{set2[key]}')

    fig.add_trace(go.Bar(y=set1_names,
                         x=set1_values,
                         orientation='h',
                         name="all",
                         text=set1_labels,
                         textposition='auto',
                         marker_color=['orange', 'lightseagreen', '#de465f', 'lightseagreen', 'purple', 'green']),
                  row=1, col=1,
                  )

    fig.add_trace(go.Bar(y=set2_names,
                         x=set2_values,
                         orientation='h',
                         name="all",
                         text=set2_labels,
                         textposition='auto',
                         marker_color=['orange', 'lightseagreen', '#de465f', 'lightseagreen', 'purple', 'green']),
                  row=1, col=2,
                  )

    fig.update_layout(height=400, width=1300, title_text="Title name",
                      xaxis_title=xaxis_title, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
                      )
    fig.show()
# ----------------------- Simple two bar-charts comparison

def draw_figure8(data = {'Group1 name':0.39,'Group2 name':0.18},
                 title_name = "Comparison, Group1 vs Goup2 "):
    colors = ['green', 'purple']

    data_names = []
    data_values = []
    data_labels = []
    for key in data.keys():
        data_names.append(key)
        data_values.append(data[key])
        data_labels.append(f'{data[key]}%')
    fig = go.Figure(go.Bar(x=data_names,
                           y=data_values,
                           orientation='v',
                           name="all",
                           text=data_labels,
                           textposition='auto',
                           marker_color=colors))
    fig.update_layout(height=600, width=1000, title_text=title_name, font=dict(size=35),
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    fig.show()

#     ---- Comparison between 4 groups and on different stages

def draw_figure9(
data = {

        "Group1 name": [2.48, 2.37, 2.28, 2.22, 2.07, 2.04],
        "Group2 name": [2.49, 2.39, 2.31, 2.22, 2.06, 2.03],
        "Group3 name": [2.45, 2.34, 2.25, 2.19, 2.06, 2.02],
        "Group4 name": [2.5, 2.39, 2.30, 2.19, 2.07, 2.03],
        "labels": ["goal 1", "goal 2", "goal 40", "goal 50", "goal 75", "goal 100"]
    }
                ):


    fig1 = go.Figure(
        data=[
            go.Bar(
                name="Group1 name",
                x=data["labels"],
                y=data["Group1 name"],
                text=data["Group1 name"],
                textposition='auto',
                offsetgroup=0,
                marker_color='#74d6f2'
            ),
            go.Bar(
                name="Group2 name",
                x=data["labels"],
                y=data["Group2 name"],
                text=data["Group2 name"],
                textposition='auto',
                offsetgroup=1,
                marker_color='#74d6f2', marker_line_width=1.5, opacity=0.6, marker_line_color='#1b5f73'
            ),
            go.Bar(
                name="Group3 name",
                x=data["labels"],
                y=data["Group3 name"],
                text=data["Group3 name"],
                textposition='auto',
                offsetgroup=2,
                marker_color='#31ac28'
            ),
            go.Bar(
                name="Group4 name",
                x=data["labels"],
                y=data["Group4 name"],
                text=data["Group4 name"],
                textposition='auto',
                offsetgroup=3,
                marker_color='#31ac28', marker_line_width=1.5, opacity=0.6, marker_line_color='#1b6216'
            ),

        ],
        layout=go.Layout(
            title="Comparison Group1 vs Group2 vs Group3 vs Group4",

            width=1300, height=500,
            yaxis_title='Statistic'
        )
    )
    fig1.show()

# --------- number of feature occurence + statistic

# ---data:
df_blockers = pd.DataFrame(columns=['feature1 + feature2', 'avg_count', 'occurance (times)'])
df_blockers['feature1 + feature2'] = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6']
df_blockers['avg_count'] = pd.Series([1, 0.5, 2.2, 3, 1.2, 1.1])
df_blockers['occurance (times)'] = pd.Series([3, 2, 8, 5, 6, 7])

def draw_figure10():
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=("avg_count", "occurence (times)"),
                        shared_yaxes=True)

    fig.add_trace(go.Bar(y=df_blockers['feature1 + feature2'].apply(str)[::-1],
                         x=df_blockers['avg_count'][::-1],
                         orientation='h',
                         name="all",
                         text=df_blockers['avg_count'][::-1],
                         textposition='auto',
                         marker_color='#62a9d1'
                         ), row=1, col=1
                  )

    fig.add_trace(go.Bar(y=df_blockers['feature1 + feature2'].apply(str)[::-1],
                         x=df_blockers['occurance (times)'][::-1],
                         orientation='h',
                         name="all",
                         text=df_blockers['occurance (times)'][::-1],
                         textposition='auto',
                         marker_color='#f6c244'
                         ), row=1, col=2
                  )

    fig.update_layout(height=600, width=1200, title_text="feature1 + feature2")
    fig.show()

# ------

def draw_figure11():
    colors = ['#c4294d', 'grey', 'grey', 'grey', '#e86141', '#e48f34', 'grey', 'grey']

    fig = make_subplots(
        rows=1, cols=1,
        specs=[[{}]], subplot_titles=(''))

    fig.add_trace(go.Bar(y=['after 2hr', 'after 4hr', 'after 6hr', 'after 8hr'],
                         x=[19, 27, 36, 46],
                         orientation='h',
                         name="all",
                         text=['29%', '37%', '46%', '56%'],
                         textposition='auto',
                         marker_color=colors), row=1, col=1,
                  )

    fig.update_layout(height=400, width=600, title_text="Title name",
                      xaxis_title="customer share affected(%)", paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)'
                      )
    fig.show()


# --------

def draw_figure12():
#  subplots bar charts comparison by type

    fig1 = make_subplots(
        rows=1, cols=3, shared_xaxes=False, subplot_titles=("Clients 1-30", "Clients 30-60", "Clients 60-100")
    )
    colors = ['lightseagreen', '#de465f']
    fig1.append_trace(go.Bar(x=['female', 'male'],
                             y=[4.44, 3.89],
                             orientation='v',
                             name="all",
                             text=[4.44, 3.89],
                             textposition='auto',
                             marker_color=colors), row=1, col=1)

    fig1.append_trace(go.Bar(x=['female', 'male'],
                             y=[7.58, 1.47],
                             orientation='v',
                             name='all',
                             text=[7.58, 1.47],
                             textposition='auto',
                             marker_color=colors), row=1, col=2)

    fig1.append_trace(go.Bar(x=['female', 'male'],
                             y=[2.77, 2.34],
                             orientation='v',
                             name="all",
                             text=[2.77, 2.34],
                             textposition='auto',
                             marker_color=colors), row=1, col=3)

    fig1.update_layout(height=300, width=1000, title_text="Average purchases", paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)')
    fig1.show()
# -----------

