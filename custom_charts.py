import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=[2, 1, 4, 3]))
fig.add_trace(go.Bar(y=[1, 4, 3, 2]))
fig.update_layout(title = 'Hello Figure')
fig.show()



#  Bar chart horisontal subplots

colors = ['lightslategray',] * 6
colors[1] = 'crimson'
colors[0] = 'crimson'

fig = make_subplots(
    rows=4, cols=2,
    specs=[[{"rowspan": 2, "colspan": 2 ,"type": "bar"}, None],
           [None, None],
           [{}, {}],
           [{}, {}]],
    subplot_titles=('',"days played Phase1(retained)", "days played Phase1(churned)","days played Phase2(retained)","days played Phase2(churned)"))


fig.add_trace(go.Bar(y = ['phase2 (7d-churned)','phase1 (7d-churned)','phase2 (7d-retained)','phase1 (7d-retained)','phase2 ','phase1 '],
                     x = [phase2_7d_churned,phase1_7d_churned,phase2_7d_active,phase1_7d_active,phase2,phase1],
                     orientation='h',
                     name="all",
                     text=[str(phase2_7d_churned)+' days',str(phase1_7d_churned)+' days',str(phase2_7d_active)+' days',str(phase1_7d_active)+' days',str(phase2)+' days',str(phase1)+' days'],
                     textposition='auto',
                     marker_color=colors),row=1, col=1,
                      )
fig.add_trace(go.Histogram(y=ph1_d7_active_days_played['active_days'],marker_color='rgb(158,202,225)',opacity=0.5,marker_line_width=1.5,histnorm='probability',name="Phase1 retained"), row=3, col=1)
fig.add_trace(go.Histogram(y=ph1_d7_churned_days_played['active_days'],marker_color='crimson',opacity=0.5,marker_line_width=1.5,  name="Phase1 churned",histnorm='probability'), row=3, col=2)
fig.add_trace(go.Histogram(y=ph2_d7_active_days_played['active_days'],marker_color='rgb(158,202,225)',opacity=0.5,marker_line_width=1.5,histnorm='probability',  name="Phase2 retained"), row=4, col=1)
fig.add_trace(go.Histogram(y=ph2_d7_churned_days_played['active_days'],marker_color='crimson',opacity=0.5,marker_line_width=1.5, histnorm='probability', name="Phase2 churned"), row=4, col=2)

fig.update_layout(height=800, width=900, title_text="How many days they played during first week? (avg)",xaxis_title="days", font=dict(size=14))
fig.show()

# --------------

# first session duration for 7d retained and 7d churned

colors = ['lightslategray', ] * 6
colors[1] = 'crimson'
colors[0] = 'crimson'
colors[3] = '#61e357'
colors[2] = '#61e357'

fig = make_subplots(
    rows=1, cols=1,
    specs=[[{}]],

    subplot_titles=(''))

[ph1_7d_churned_first_session_duration_median, ph1_7d_active_first_session_duration_median,
 ph1_first_session_duration_median]
[ph2_7d_churned_first_session_duration_median, ph2_7d_active_first_session_duration_median,
 ph2_first_session_duration_median]

fig.add_trace(go.Bar(
    y=['phase2 (7d-churned)', 'phase1 (7d-churned)', 'phase2 (7d-retained)', 'phase1 (7d-retained)', 'phase2 (median)',
       'phase1 (median)'],
    x=[ph2_7d_churned_first_session_duration_median,
       ph1_7d_churned_first_session_duration_median,
       ph2_7d_active_first_session_duration_median,
       ph1_7d_active_first_session_duration_median,
       ph2_first_session_duration_median,
       ph1_first_session_duration_median],
    orientation='h',
    name="all",
    text=[str(ph2_7d_churned_first_session_duration_median) + ' min',
          str(ph1_7d_churned_first_session_duration_median) + ' min',
          str(ph2_7d_active_first_session_duration_median) + ' min',
          str(ph1_7d_active_first_session_duration_median) + ' min',
          str(ph2_first_session_duration_median) + ' min',
          str(ph1_first_session_duration_median) + ' min'],
    textposition='auto',
    marker_color=colors), row=1, col=1,
              )

fig.update_layout(height=400, width=600, title_text="First session duration (Median)",
                  xaxis_title="minutes", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
                  )
fig.show()


# -------- bar chart vertical, two axis


# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(

    go.Scatter(
        x=x_losers[:100],
        y=y_retention,
        legendgroup='Relative Retention',
        name='Relative Retention',
        line_color='#0df50d',
        line=dict(width=4)
    ),
    secondary_y=False)

fig.add_trace(
    go.Bar(
        x=x_losers[:100],
        y=y_losers,
        legendgroup='7d-churned/lost',
        name='7d-churned/lost',
        text=y_losers,
        textposition='outside',
        marker_color='#de465f',
        offsetgroup=0
    ), secondary_y=True
)

fig.add_trace(
    go.Bar(
        x=x_winners[:100],
        y=y_winners,
        legendgroup='7d-churned/won',
        name='7d-churned/won',
        text=y_winners,

        textposition='outside',
        marker_color='#fe9548',
        offsetgroup=0

    ), secondary_y=True)

fig.update_layout(
    title_text="   <b> Churn by Level  </b> ",
    width=1000, height=700, yaxis_title="Loading time in sec",

    font=dict(
        size=22
    ), legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

fig.update_yaxes(title_text="Relative Retention", secondary_y=False)
fig.update_yaxes(title_text="absolute churn ", secondary_y=True, range=[0, 120])
fig.update_xaxes(title_text="Levels")
fig.show()
Levels_churn_Phase12 = fig.write_html("Levels_churn_Phase1+Phase2.html")


# ------- Bar chart vertical


looser = ph1_loosers_tries[ph1_loosers_tries['type']=='Phase1 churned points']
y_looser = looser['avg_tries']
x_looser = looser['level_number']
retain = ph1_loosers_tries[ph1_loosers_tries['type']=='Phase1 7d-retained ']
y_retain = retain['avg_tries']
x_retain = retain['level_number']

fig = go.Figure()
fig.add_trace(go.Bar(
    x=x_looser,
    y=y_looser,
    name=' 7d-churned/lost',
    marker_color='#de465f',
    text=y_looser,
     textposition='outside'
))

fig.add_trace(go.Bar(
    x=x_retain,
   y=y_retain,
    name=' 7d-retained',
    marker_color='lightseagreen',
    text=y_retain,
     textposition='outside'
))

#fig.add_trace(go.Scatter(
 #   x=[0,103],
#        y= [0,0],
#        line_color='black',
 #       line=dict( width=1)
#))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group',title_text="   <b> Levels churn (Phase1) </b> ",
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
fig.write_html("ph1_loosers.html")


# ----


