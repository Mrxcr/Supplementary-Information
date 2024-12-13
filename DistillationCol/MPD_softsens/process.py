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


def plot_MPD(df, start, end):
    '''
    Plot the predicted results of MPD on the testing set
    Parameters:
    df: predicted MPD on the testing set after anti-normalization
    start/end: plot_MPD will plot the samples in [start, end] of the testing set 
    '''
    lineWidth = 1.2

    fig = make_subplots(rows=5, cols=1, vertical_spacing=0.1
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


    fig.update_layout(height=900, width=1200
                , paper_bgcolor='white', plot_bgcolor='white'
                    , font=dict(family="Times New Roman"))
    fig.update_xaxes(range=[start, end+200])
    fig.update_yaxes(range=[250, 1400])
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')

    fig.show()
    print(f"Save Figure 8 at SuppMaterial\DistillationCol\MPD_softsens\Figures\Figure8_{end-start}.png.")
    fig.write_html(f"Figures/Figure8_{end-start}.html")
    fig.write_image(f"Figures/Figure8_{end-start}.png")


def plot_component(df_DPMRM, df_DPIRMRM, df_DPORMRM, df_DPR2MRM):
    fig = make_subplots(rows=2, cols=2)
    fig.add_trace(go.Scatter(x=[i for i in range(len(df_DPMRM))], y=df_DPMRM.loc[:, "NumberofCluster"]
                            , name="model_DPMRM", line_color="black"), row=1, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(len(df_DPORMRM))], y=df_DPORMRM.loc[:, "NumberofCluster"]
                            , name="model_DPORMRM", line_color="black"), row=1, col=2)
    fig.add_trace(go.Scatter(x=[i for i in range(len(df_DPIRMRM))], y=df_DPIRMRM.loc[:, "NumberofCluster"]
                            , name="model_DPIRMRM", line_color="black"), row=2, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(len(df_DPR2MRM))], y=df_DPR2MRM.loc[:, "NumberofCluster"]
                            , name="model_DPR2MRM", line_color="black"), row=2, col=2)
    fig.update_layout(
                    height=600, width=1000
                , plot_bgcolor='white'
                , font=dict(family="Times New Roman"))
    fig.update_xaxes(showline=True, zeroline=True, zerolinecolor="black", showgrid=True, linewidth=2
                    , linecolor='black', gridcolor='lightgrey', mirror=True, ticks='outside')
    fig.update_yaxes(showline=True, zeroline=True, zerolinecolor="black", showgrid=True, linewidth=2
                    , linecolor='black', gridcolor='lightgrey', mirror=True, ticks='outside')
    fig.show()
    print("Save Figure 7 at SuppMaterial\DistillationCol\MPD_softsens\Figures\Figure7.png.")
    fig.write_html(f"Figures/Figure7.html")
    fig.write_image("Figures/Figure7.png")


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
    fig.add_trace(go.Scatter(x=[i for i in range(300, 1400)], y=[i for i in range(300, 1400)], line_color="black", showlegend=False))

    fig.update_layout(height=600, width=900
                , paper_bgcolor='white', plot_bgcolor='white'
                    , font=dict(family="Times New Roman"))
    fig.update_xaxes(range=[300, 1400])
    fig.update_yaxes(range=[300, 1400])
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='black', mirror=True, ticks='outside')

    fig.show()
    print("Save Figure 9 at SuppMaterial\DistillationCol\MPD_softsens\Figures\Figure9.png.")
    fig.write_html("Figures/Figure9.html")
    fig.write_image("Figures/Figure9.png")


def plot_QQ(df_qq):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 18  # 设置所有字体的大小为14

    plt.figure(figsize=(10, 10))
    plt.subplot(221)
    probplot(df_qq.iloc[:, 1].values, plot=plt)
    plt.gca().get_lines()[0].set_markersize(3)
    plt.title("")
    plt.xlabel("")
    plt.ylabel("T35111_MPD.PV")

    plt.subplot(222)
    probplot(df_qq.iloc[:, 2].values, plot=plt)
    plt.gca().get_lines()[0].set_markersize(3) 
    plt.title("")
    plt.xlabel("")
    plt.ylabel("TI35112.PV")

    plt.subplot(223)
    probplot(df_qq.iloc[:, 3].values, plot=plt)
    plt.gca().get_lines()[0].set_markersize(3) 
    plt.title("")
    plt.xlabel("")
    plt.ylabel("TI35111a3.PV")

    plt.subplot(224)
    probplot(df_qq.iloc[:, 4].values, plot=plt)
    plt.gca().get_lines()[0].set_markersize(3)
    plt.title("")
    plt.xlabel("")
    plt.ylabel("TI35111a9.PV")

    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    # plt.show()
    print("Save Figure G1 at SuppMaterial\DistillationCol\MPD_softsens\Figures\FigureG1.png.")
    plt.savefig('Figures/FigureG1.png', format='png')



if __name__ == "__main__":
    # Load predicted MPD results by different models (normalized)
    df = pd.read_csv("data/MPD.csv")

    # restore the MinMaxScaler trained on the training set
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler.min_ = 0.
    scaler.scale_ = 0.0005

    # Inverse transform
    df["DPMRM_UB"] = df.loc[:, "DPMRM"] + np.sqrt(df.loc[:, "DPMRM_var"]) * 1.96
    df["DPMRM_LB"] = df.loc[:, "DPMRM"] - np.sqrt(df.loc[:, "DPMRM_var"]) * 1.96
    df["DPIRMRM_UB"] = df.loc[:, "DPIRMRM"] + np.sqrt(df.loc[:, "DPIRMRM_var"]) * 1.96
    df["DPIRMRM_LB"] = df.loc[:, "DPIRMRM"] - np.sqrt(df.loc[:, "DPIRMRM_var"]) * 1.96
    df["DPORMRM_UB"] = df.loc[:, "DPORMRM"] + np.sqrt(df.loc[:, "DPORMRM_var"]) * 1.96
    df["DPORMRM_LB"] = df.loc[:, "DPORMRM"] - np.sqrt(df.loc[:, "DPORMRM_var"]) * 1.96
    df["DPR2MRM_UB"] = df.loc[:, "DPR2MRM"] + np.sqrt(df.loc[:, "DPR2MRM_var"]) * 1.96
    df["DPR2MRM_LB"] = df.loc[:, "DPR2MRM"] - np.sqrt(df.loc[:, "DPR2MRM_var"]) * 1.96
    df.loc[:, ['y_true', 'GMR', 'DPORMRM', 'DPIRMRM', 'DPMRM', 'DPR2MRM', ]] \
        = df.loc[:, ['y_true', 'GMR', 'DPORMRM', 'DPIRMRM', 'DPMRM', 'DPR2MRM']].apply(lambda x: scaler.inverse_transform(x.values[:, np.newaxis]).flatten())
    df.loc[:, ["DPMRM_UB", "DPMRM_LB", "DPIRMRM_UB", "DPIRMRM_LB", "DPORMRM_UB", "DPORMRM_LB", "DPR2MRM_UB", "DPR2MRM_LB"]] \
        = df.loc[:, ["DPMRM_UB", "DPMRM_LB", "DPIRMRM_UB", "DPIRMRM_LB", "DPORMRM_UB", "DPORMRM_LB"
                    , "DPR2MRM_UB", "DPR2MRM_LB"]].apply(lambda x: scaler.inverse_transform(x.values[:, np.newaxis]).flatten())
    df.set_index("Time", drop=True, inplace=True)

    print("Save the predicted values for MPD at SuppMaterial\DistillationCol\MPD_softsens\data\MPD_inversed.csv.")
    df.to_csv("data/MPD_inversed.csv")

    # RMSE and MAE (Table 1)
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
    print("\n")
    print("-------------------------Table 1------------------------")
    print(f"GMR on the testing set, RMSE: {mse_GMR:.2f}, MAE: {mae_GMR:.2f}")
    print(f"DPMRM on the testing set, RMSE: {mse_DPMRM:.2f}, MAE: {mae_DPMRM:.2f}")
    print(f"DPIRMRM on the testing set, RMSE: {mse_DPIRMRM:.2f}, MAE: {mae_DPIRMRM:.2f}")
    print(f"DPORMRM on the testing set, RMSE: {mse_DPORMRM:.2f}, MAE: {mae_DPORMRM:.2f}")
    print(f"DPR2MRM on the testing set, RMSE: {mse_DPR2MRM:.2f}, MAE: {mae_DPR2MRM:.2f}")
    print("\n")

    # Component number selection process for the distillation column by the DPM-based models (Figure 7)
    df_DPMRM = pd.read_csv("data/train_DPMRM.csv")
    df_DPIRMRM = pd.read_csv("data/train_DPIRMRM.csv")
    df_DPORMRM = pd.read_csv("data/train_DPORMRM.csv")
    df_DPR2MRM = pd.read_csv("data/train_DPR2MRM.csv")
    plot_component(df_DPMRM, df_DPIRMRM, df_DPORMRM, df_DPR2MRM)

    # Plot the MPD results on a snippet of the testing set (Figure 8)
    # You can changed the parameters "start" and "end" in order to plot the arbitrary range of the testing set
    plot_MPD(df, 0, 2176) # There are in total 2176 samples in the testing set
    plot_MPD(df, 0, 1500)

    # Scatter plot of MPD predictions vs true values (FIgure 9)
    plot_scatter(df)    

    # QQplot (Figure G1)
    df_qq = pd.read_csv("data/df_qq.csv")
    plot_QQ(df_qq)



     

