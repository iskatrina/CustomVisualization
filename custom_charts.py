import random

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=[2, 1, 4, 3]))
fig.add_trace(go.Bar(y=[1, 4, 3, 2]))
fig.update_layout(title = 'Hello Figure')
fig.show()



#  Bar chart horisontal subplots + histograms
d1 = [1,2,3,6,3,4]
p1 = [1,2,3,1,1,1,3,3,3,9,9]
d2 = [1,2,3,3,7,5,12,3,6]
p2 = [1,2,3,0,7,0,0,7]

group2 = 3.3
group1 = 10
group3 = 7
group4 = 13
group5 = 14
group6 = 4.5

# ------------

colors = ['lightslategray',] * 6
colors[1] = 'crimson'
colors[0] = 'crimson'

fig = make_subplots(
    rows=4, cols=2,
    specs=[[{"rowspan": 2, "colspan": 2 ,"type": "bar"}, None],
           [None, None],
           [{}, {}],
           [{}, {}]],
    subplot_titles=('',"days played d1", "days played p1","days played d2","days played p2"))


fig.add_trace(go.Bar(y = ['group1','group2','group3','group4','group5 ','group6'],
                     x = [group1,group2,group3,group4,group5,group6],
                     orientation='h',
                     name="all",
                     text=[str(group1)+' days',str(group2)+' days',str(group3)+' days',str(group4)+' days',str(group5)+' days',str(group6)+' days'],
                     textposition='auto',
                     marker_color=colors),row=1, col=1,
                      )
fig.add_trace(go.Histogram(y=d1,marker_color='rgb(158,202,225)',opacity=0.5,marker_line_width=1.5,histnorm='probability',name="d1 name"), row=3, col=1)
fig.add_trace(go.Histogram(y=p1,marker_color='crimson',opacity=0.5,marker_line_width=1.5,  name="p1 name",histnorm='probability'), row=3, col=2)
fig.add_trace(go.Histogram(y=d2,marker_color='rgb(158,202,225)',opacity=0.5,marker_line_width=1.5,histnorm='probability',  name="d2 name"), row=4, col=1)
fig.add_trace(go.Histogram(y=p2,marker_color='crimson',opacity=0.5,marker_line_width=1.5, histnorm='probability', name="p2 name"), row=4, col=2)

fig.update_layout(height=800, width=900, title_text="How many days did it took? (avg)",xaxis_title="days", font=dict(size=14))
fig.show()

# --------------
group1 =34
group2 = 23
group3 = 65
group4 = 12
group5 = 34
group6 = 23

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

[group1, group2, group3]
[group4, group5, group6]

fig.add_trace(go.Bar(y=['group4', 'group1', 'group5', 'group2', 'group6', 'group3'],
                     x=[group4,
                        group1,
                        group5,
                        group2,
                        group6,
                        group3],
                     orientation='h',
                     name="all",
                     text=[str(group4) + ' min',
                           str(group1) + ' min',
                           str(group5) + ' min',
                           str(group2) + ' min',
                           str(group6) + ' min',
                           str(group3) + ' min'],
                     textposition='auto',
                     marker_color=colors), row=1, col=1,
              )

fig.update_layout(height=400, width=600, title_text="First event duration (Median)",
                  xaxis_title="minutes", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
                  )
fig.show()

# -------- bar chart vertical, two axis, relative retention+ churn by level
x_group1 = [i for i in range(1,101)]
y_group1 = random.sample(range(11, 67), 34)
y_retention = pd.Series([1,0.43,0.25,0.20,0.18,0.15,0.15,0.14,0.13,0.10,0.09,0.09,0.07,0.06,0.05])
x_group2 = [i for i in range(1,101)]
y_group2 = random.sample(range(4, 67), 23)

## Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(

    go.Scatter(
        x= x_group1[:100],
        y= y_retention,
        legendgroup='Relative Retention',
         name='Relative Retention',
        line_color='#0df50d',
        line=dict( width=4)
    ),
        secondary_y=False)

fig.add_trace(
    go.Bar(
        x=x_group1[:100],
        y=y_group1,
        legendgroup='group1',
         name='group1',
        text=y_losers ,
        textposition = 'outside',
        marker_color='#de465f',
        offsetgroup=0
    ),secondary_y=True
)

fig.add_trace(
    go.Bar(
        x=x_group2[:100],
        y=y_group2,
        legendgroup='group2',
         name='group2',
        text=y_winners ,

        textposition = 'outside',
        marker_color='#fe9548',
        offsetgroup=0

    ),secondary_y=True)




fig.update_layout(
    title_text="   <b> Churn by Level  </b> ",
    width = 1000,height = 700,yaxis_title="Loading time in sec",

      font=dict(
        size=22
    ),legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')

fig.update_yaxes(title_text="Relative Retention", secondary_y=False)
fig.update_yaxes(title_text="absolute churn ", secondary_y=True,range=[0,120])
fig.update_xaxes(title_text="Levels")
fig.show()


# ------- Bar chart vertical level tries comparison

x_group1 = [i for i in range(1,30)]
y_group1 = random.sample(range(11, 190), 100)
x_group2 = [i for i in range(1,30)]
y_group2 = random.sample(range(3, 120), 100)



fig = go.Figure()
fig.add_trace(go.Bar(
    x=x_group1,
    y=y_group1,
    name=' group1',
    marker_color='#de465f',
    text=y_group1,
     textposition='outside'
))

fig.add_trace(go.Bar(
    x=x_group2,
   y=y_group2,
    name=' group2',
    marker_color='lightseagreen',
    text=y_group2,
     textposition='outside'
))


# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group',title_text="   <b> Levels churn  </b> ",
    width = 1400,height = 400,yaxis_title="Average tries",xaxis_title="Level",paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
      font=dict(
        size=22
    ),legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1))
fig.show()


# ---- Line + bar shared axis

x_values = ['day'+str(i) for i in range(1,15)]
df1 = pd.Series([13,17.6, 22.8,25,27.8,30,32.5,34])
df2 = pd.Series([15,21, 25.6,29,32.8,35,36,37])
y_difference = df2 - df1

## Values visualisation
fig_rounds2 = go.Figure()

fig_rounds2.add_trace(
    go.Scatter(
        x=x_values,
        y=df1[0:8],
        mode='lines+markers+text',
        line=dict(color='green', width=3),
        name='Group 1 ',
        text=ph1_rounds_played_all[0:8],
        textposition="bottom center",
        marker=dict(color='green')

    )
)

fig_rounds2.add_trace(
    go.Scatter(
        x=x_values,
        y=df2[0:8],
        line=dict(color='purple', width=3),
        name='Group 2',
        mode='lines+markers+text',
        text=ph2_rounds_played_all[0:8],
        textposition="bottom center",
        marker=dict(color='purple')

    )
)

fig_rounds2.add_trace(go.Bar(x=x_values, y=y_difference[0:8],
                             name='value difference'))

fig_rounds2.update_layout(
    height=500, width=800,
    showlegend=True,
    font=dict(size=16),
    title_text="Value Group1 vs. Group2 (Cumulative)",
    yaxis_title='value (cumulative)', legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))

fig_rounds2.show()


# -----


