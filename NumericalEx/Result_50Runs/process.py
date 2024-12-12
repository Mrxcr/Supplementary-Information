import pandas as pd
import plotly.graph_objects as go


# Load data from 50 simulation runs
df_res_DPR2MRM = pd.read_csv("data/Result_DPR2MRM.csv")
df_res_DPMRM = pd.read_csv("data/Result_DPMRM.csv")
df_res_DPIRMRM = pd.read_csv("data/Result_DPIRMRM.csv")
df_res_DPORMRM = pd.read_csv("data/Result_DPORMRM.csv")
df_res_GMR = pd.read_csv("data/Result_GMR.csv")


dict_color = {"DPR2MRM":"blue", "DPMRM":"green", "DPIRMRM":"brown"
              , "DPORMRM":"red", "GMR":"magenta"}


# Generate Figure 2 in the manuscript --------------------------------------
fig = go.Figure()
fig.add_trace(go.Histogram(
    x=df_res_GMR["NumberClu"],
    # histnorm='percent',
    name='GMR',
    xbins=dict(
        start=2.5,
        end=8,
        size=1
    ),
    marker_color=dict_color["GMR"],
    opacity=1.
))
fig.add_trace(go.Histogram(
    x=df_res_DPMRM["NumberClu"],
    # histnorm='percent',
    name='DPMRM',
    xbins=dict(
        start=2.5,
        end=8,
        size=1
    ),
    marker_color=dict_color["DPMRM"],
    opacity=1.
))
fig.add_trace(go.Histogram(
    x=df_res_DPIRMRM["NumberClu"],
    # histnorm='percent',
    name='DPIRMRM',
    xbins=dict(
        start=2.5,
        end=8,
        size=1
    ),
    marker_color=dict_color["DPIRMRM"],
    opacity=1.
))
fig.add_trace(go.Histogram(
    x=df_res_DPORMRM["NumberClu"],
    # histnorm='percent',
    name='DPORMRM',
    xbins=dict(
        start=2.5,
        end=8,
        size=1
    ),
    marker_color=dict_color["DPORMRM"],
    opacity=1.
))
fig.add_trace(go.Histogram(
    x=df_res_DPR2MRM["NumberClu"],
    # histnorm='percent',
    name='DPR2MRM', # name used in legend and hover labels
    xbins=dict( # bins used for histogram
        start=2.5,
        end=8,
        size=1
    ),
    marker_color=dict_color["DPR2MRM"],
    opacity=1.
))

fig.update_layout(
    xaxis_title_text='Estimated Number', # xaxis label
    yaxis_title_text='Times', # yaxis label
    bargap=0.4, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)
fig.update_layout(width=800, height=500
                , paper_bgcolor='white', plot_bgcolor="white"
                , font=dict(family="Times New Roman", size=15))
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')    
fig.show()
print("Save Figure 2 at Figures/Figure 2.png.")
fig.write_html("Figures/Figure2.html")
fig.write_image("Figures/Figure2.png")


# Generate Figure 6 in manuscript --------------------------------------
fig = go.Figure()
fig.add_trace(go.Box(y=df_res_GMR["MSE"], quartilemethod="linear"
                     , marker_color=dict_color["GMR"], name="GMR"))
fig.add_trace(go.Box(y=df_res_DPMRM["MSE"], quartilemethod="linear"
                     , marker_color=dict_color["DPMRM"], name="DPMRM"))
fig.add_trace(go.Box(y=df_res_DPIRMRM["MSE"], quartilemethod="linear"
                     , marker_color=dict_color["DPIRMRM"], name="DPIRMRM"))
fig.add_trace(go.Box(y=df_res_DPORMRM["MSE"], quartilemethod="linear"
                     , marker_color=dict_color["DPORMRM"], name="DPORMRM"))
fig.add_trace(go.Box(y=df_res_DPR2MRM["MSE"], quartilemethod="linear"
                     , marker_color=dict_color["DPR2MRM"], name="DPR2MRM"))

fig.update_traces(boxpoints='all', jitter=0.1)

fig.update_layout(width=800, height=500
                , paper_bgcolor='white', plot_bgcolor="white"
                , font=dict(family="Times New Roman", size=15))
fig.update_layout(boxmode = "overlay")
fig.update_layout(yaxis_range=[0,14])
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')
fig.show()
print("Save Figure 6 at Figures/Figure 6.png.")
fig.write_html("Figures/Figure6.html")
fig.write_image("Figures/Figure6.png")


# Generate Figure 5 in manuscript --------------------------------------
# True weights
values = [2.4, -0.32, -1.8, 3.8, -0.9, 4.2, -1.2, 1.6]
list_x, list_val = [], []
for idx, item in enumerate(df_res_DPMRM.columns[3:]):
    list_x += [item] * 50
    list_val += [values[idx]] * 50

fig = go.Figure() 
x = list_x
fig.add_trace(go.Box( 
	y=df_res_DPMRM.iloc[:, 3:].values.T.flatten(), 
	x=x, 
	name='DPMRM', 
	marker_color=dict_color["DPMRM"],
    marker={"symbol":"square", "size":5},
    boxpoints="suspectedoutliers"
)) 

fig.add_trace(go.Box( 
	y=df_res_DPIRMRM.iloc[:, 3:].values.T.flatten(), 
	x=x, 
	name='DPIRMRM', 
	marker_color=dict_color["DPIRMRM"],
    marker={"symbol":"cross", "size":5},
    boxpoints="suspectedoutliers"
)) 

fig.add_trace(go.Box( 
	y=list_val, 
	x=x, 
	name='True', 
	marker_color="black",
    marker={"symbol":"square", "size":5},
    boxpoints="suspectedoutliers"
)) 

fig.add_trace(go.Box( 
	y=df_res_DPORMRM.iloc[:, 3:].values.T.flatten(), 
	x=x, 
	name='DPORMRM', 
	marker_color=dict_color["DPORMRM"],
    marker={"symbol":"cross", "size":5},
    boxpoints="suspectedoutliers"
)) 

fig.add_trace(go.Box( 
	y=df_res_DPR2MRM.iloc[:, 3:].values.T.flatten(), 
	x=x, 
	name='DPR2MRM', 
	marker_color=dict_color["DPR2MRM"],
    marker={"symbol":"cross", "size":5},
    boxpoints="suspectedoutliers"
)) 

fig.update_layout(boxmode='group') 
fig.update_layout(width=1000, height=500
                , paper_bgcolor='white', plot_bgcolor="white"
                , font=dict(family="Times New Roman", size=15))
# fig.update_layout(boxmode = "overlay")
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')
fig.show()
print("Save Figure 5 at Figures/Figure 5.png.")
fig.write_html("Figures/Figure5.html")
fig.write_image("Figures/Figure5.png")