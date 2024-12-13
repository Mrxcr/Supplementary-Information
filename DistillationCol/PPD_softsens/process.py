import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
import statsmodels.api as sm 
import pylab as py 
import matplotlib.pyplot as plt
from scipy.stats import norm, probplot


def plot_MPD(df):
    '''
    Plot the predicted results of PPD on the testing set
    Parameters:
    df: predicted PPD on the testing set after anti-normalization
    start/end: plot_PPD will plot the samples in [start, end] of the testing set 
    '''
    lineWidth = 2
    start, end = 0, len(df)

    fig = make_subplots(rows=5, cols=1, vertical_spacing=0.05
                        , shared_xaxes=True
                        )

    fig.add_trace(go.Scatter(x=[i for i in range(start, end)], y=df["y_true"].iloc[start:end].values
                            , name="Real values", line_color="black", line={"width":lineWidth}), row=1, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)], y=df["GMR"].iloc[start:end].values
                            , name="GMR", line_color="red", line={"width":lineWidth}), row=1, col=1)


    fig.add_trace(go.Scatter(x=[i for i in range(start, end)]
                            , y=df["DPMRM_UB"].iloc[start:end].values
                            , line_color="#EFA8A3", fill="none", name="95% CI")
                            , row=2, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)]
                            , y=df["DPMRM_LB"].iloc[start:end].values
                            , line_color="#EFA8A3", fill="tonexty", name="95% CI")
                            , row=2, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)], y=df["y_true"].iloc[start:end].values
                            , name="Real values", line_color="black", line={"width":lineWidth}), row=2, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)], y=df["DPMRM"].iloc[start:end].values
                            , name="DPMRM", line_color="red", line={"width":lineWidth}), row=2, col=1)


    fig.add_trace(go.Scatter(x=[i for i in range(start, end)]
                            , y=df["DPIRMRM_UB"].iloc[start:end].values
                            , line_color="#EFA8A3", fill="none", name="95% CI")
                            , row=3, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)]
                            , y=df["DPIRMRM_LB"].iloc[start:end].values
                            , line_color="#EFA8A3", fill="tonexty", name="95% CI")
                            , row=3, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)], y=df["y_true"].iloc[start:end].values
                            , name="Real values", line_color="black", line={"width":lineWidth}), row=3, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)], y=df["DPIRMRM"].iloc[start:end].values
                            , name="DPIRMRM", line_color="red", line={"width":lineWidth}), row=3, col=1)

    fig.add_trace(go.Scatter(x=[i for i in range(start, end)]
                            , y=df["DPORMRM_UB"].iloc[start:end].values
                            , line_color="#EFA8A3", fill="none", name="95% CI")
                            , row=4, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)]
                            , y=df["DPORMRM_LB"].iloc[start:end].values
                            , line_color="#EFA8A3", fill="tonexty", name="95% CI")
                            , row=4, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)], y=df["y_true"].iloc[start:end].values
                            , name="Real values", line_color="black", line={"width":lineWidth}), row=4, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)], y=df["DPORMRM"].iloc[start:end].values
                            , name="DPORMRM", line_color="red", line={"width":lineWidth}), row=4, col=1)

    fig.add_trace(go.Scatter(x=[i for i in range(start, end)]
                            , y=df["DPR2MRM_UB"].iloc[start:end].values
                            , line_color="#EFA8A3", fill="none", name="95% CI")
                            , row=5, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)]
                            , y=df["DPR2MRM_LB"].iloc[start:end].values
                            , line_color="#EFA8A3", fill="tonexty", name="95% CI")
                            , row=5, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)], y=df["y_true"].iloc[start:end].values
                            , name="Real values", line_color="black", line={"width":lineWidth}), row=5, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(start, end)], y=df["DPR2MRM"].iloc[start:end].values
                            , name="DPR2MRM", line_color="red", line={"width":lineWidth}), row=5, col=1)

    fig.update_layout(height=1000, width=900
                , paper_bgcolor='white', plot_bgcolor='white'
                    , font=dict(family="Times New Roman"))
    fig.update_xaxes(range=[0, 320])
    fig.update_yaxes(range=[0,290])
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')

    fig.show()
    print("Save Figure 10 at SuppMaterial\DistillationCol\PPD_softsens\Figures\Figure10.png.")
    fig.write_html(f"Figures/Figure10.html")
    fig.write_image("Figures/Figure10.png")


def plot_scatter(df):
    fig = go.Figure()
    size = 6
    start = 0
    end = len(df)

    fig.add_trace(go.Scatter(x=df["y_true"].values[start:end], y=df["GMR"].values[start:end]
                            , name="GMR", mode="markers", marker={"size":size, "symbol":"cross"}))
    fig.add_trace(go.Scatter(x=df["y_true"].values[start:end], y=df["DPMRM"].values[start:end]
                            , name="DPMRM", mode="markers", marker={"size":size, "symbol":"circle-open"}))
    fig.add_trace(go.Scatter(x=df["y_true"].values[start:end], y=df["DPIRMRM"].values[start:end]
                            , name="DPIRMRM", mode="markers", marker={"size":size, "symbol":"square-open"}))
    fig.add_trace(go.Scatter(x=df["y_true"].values[start:end], y=df["DPORMRM"].values[start:end]
                            , name="DPORMRM", mode="markers", marker={"size":size, "symbol":"diamond-open"}))
    fig.add_trace(go.Scatter(x=df["y_true"].values[start:end], y=df["DPR2MRM"].values[start:end]
                            , name="DPR2MRM", mode="markers", marker={"size":size, "symbol":"triangle-down-open"}))
    fig.add_trace(go.Scatter(x=[i for i in range(0, 250)], y=[i for i in range(0, 250)], line_color="black", showlegend=False))

    fig.update_layout(height=600, width=900
                , paper_bgcolor='white', plot_bgcolor='white'
                    , font=dict(family="Times New Roman"))
    # fig.update_xaxes(range=[300, 1400])
    # fig.update_yaxes(range=[300, 1400])
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')

    fig.show()
    print("Save Figure 11 at SuppMaterial\DistillationCol\PPD_softsens\Figures\Figure11.png.")
    fig.write_html("Figures/Figure11.html")
    fig.write_image("Figures/Figure11.png")


if __name__ == "__main__":
    df = pd.read_csv("data/PPD.csv")

    # Plot Figure 10
    plot_MPD(df)

    # Plot Figure 11
    plot_scatter(df)

    # Table 2
    print("\n")
    print("-------------------------Table 2------------------------")
    mse_GMR = mse(df.loc[:, ["y_true"]].values, df.loc[:, ["GMR"]], squared=False)
    mae_GMR = mae(df.loc[:, ["y_true"]].values, df.loc[:, ["GMR"]])
    mae_DPMRM = mae(df.loc[:, ["y_true"]].values, df.loc[:, ["DPMRM"]])
    mse_DPMRM = mse(df.loc[:, ["y_true"]].values, df.loc[:, ["DPMRM"]], squared=False)
    mae_DPIRMRM = mae(df.loc[:, ["y_true"]].values, df.loc[:, ["DPIRMRM"]])
    mse_DPIRMRM = mse(df.loc[:, ["y_true"]].values, df.loc[:, ["DPIRMRM"]], squared=False)
    mae_DPORMRM = mae(df.loc[:, ["y_true"]].values, df.loc[:, ["DPORMRM"]])
    mse_DPORMRM = mse(df.loc[:, ["y_true"]].values, df.loc[:, ["DPORMRM"]], squared=False)
    mae_DPR2MRM = mae(df.loc[:, ["y_true"]].values, df.loc[:, ["DPR2MRM"]])
    mse_DPR2MRM = mse(df.loc[:, ["y_true"]].values, df.loc[:, ["DPR2MRM"]], squared=False)
    print(f"GMR on the testing set, RMSE: {mse_GMR:.2f}, MAE: {mae_GMR:.2f}")
    print(f"DPMRM on the testing set, RMSE: {mse_DPMRM:.2f}, MAE: {mae_DPMRM:.2f}")
    print(f"DPIRMRM on the testing set, RMSE: {mse_DPIRMRM:.2f}, MAE: {mae_DPIRMRM:.2f}")
    print(f"DPORMRM on the testing set, RMSE: {mse_DPORMRM:.2f}, MAE: {mae_DPORMRM:.2f}")
    print(f"DPR2MRM on the testing set, RMSE: {mse_DPR2MRM:.2f}, MAE: {mae_DPR2MRM:.2f}")

