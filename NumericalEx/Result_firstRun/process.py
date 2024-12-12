import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_models(name, mat_epl, mean_pred, list_idx, list_unique):
    '''
    Plot the results of mode identification in the input space by different models
    '''
    fig = go.Figure()
    for idx_cluster in list_unique:
        idx_sample = [i for i, item in enumerate(list_idx) if item == idx_cluster]
        fig.add_trace(go.Scatter(x=Xt[idx_sample, 0], y=Xt[idx_sample, 1], mode="markers"
                                , marker={"color":[colorlist[idx_cluster] for idx in list_idx]
                                        , "size":5, "opacity":0.5}
                                , showlegend=False
                                , name=f"Mode {idx_cluster}"
                                ))

    for idx, i in enumerate(list_unique):
        fig.add_trace(go.Scatter(x=mat_epl[idx, 0, :], y=mat_epl[idx, 1, :]
                                , line_color=colorlist[i]
                                , line={"width":3}
                                , showlegend=True
                                , name=f"Mode {i+1}"
                                ))
        fig.add_trace(go.Scatter(x=[mean_pred[idx, 0]], y=[mean_pred[idx, 1]], mode="markers"
                                , marker={"size":10, "color":"red"
                                        , "symbol":"star", "opacity":0.8}
                                        , showlegend=False
                                ))

    # True Mean
    for idx, item in enumerate(list_mean):
        fig.add_trace(go.Scatter(x=[item[0]], y=[item[1]], mode="markers"
                                , marker={"size":10, "color":"black", "symbol":"cross", "opacity":0.7}
                                , name="True Mean"
                                , showlegend=True if idx == 0 else False
                                ))


    # True covariance
    for i in range(4):
        fig.add_trace(go.Scatter(x=mat_epl_true[i, 0, :], y=mat_epl_true[i, 1, :]
                                , line_color="black"
                                , line={"width":2}
                                , showlegend=True 
                                , name="True"
                                ))
        

    fig.update_layout(yaxis_range=[-7, 8], title=name)
    fig.update_layout(xaxis_title="X1", yaxis_title="X2", width=800, height=600, plot_bgcolor='white')
    fig.update_xaxes(showline=True, zeroline=True, zerolinecolor="black", showgrid=True, linewidth=2
                    , linecolor='black', gridcolor='black', mirror=True, ticks='outside')
    fig.update_yaxes(showline=True, zeroline=True, zerolinecolor="black", showgrid=True, linewidth=2
                    , linecolor='black', gridcolor='black', mirror=True, ticks='outside')

    fig.show()
    print(f"Save Figure 3 at Figures/Figure3_{name}.png.")
    fig.write_html(f"Figures/Figure3_{name}.html")
    fig.write_image(f"Figures/Figure3_{name}.png")


def plot_component(list_com_DPMRM, list_com_DPORMRM, list_com_DPIRMRM, list_com_DPR2MRM):
    fig = make_subplots(rows=2, cols=2)
    fig.add_trace(go.Scatter(x=[i for i in range(len(list_com_DPMRM))], y=list_com_DPMRM
                            , name="model_DPMRM", line_color="black"), row=1, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(len(list_com_DPORMRM))], y=list_com_DPORMRM
                            , name="model_DPORMRM", line_color="black"), row=1, col=2)
    fig.add_trace(go.Scatter(x=[i for i in range(len(list_com_DPIRMRM))], y=list_com_DPIRMRM
                            , name="model_DPIRMRM", line_color="black"), row=2, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(len(list_com_DPR2MRM))], y=list_com_DPR2MRM
                            , name="model_DPR2MRM", line_color="black"), row=2, col=2)
    fig.update_layout(
                    height=600, width=1000
                , plot_bgcolor='white'
                , font=dict(family="Times New Roman"))
    fig.update_xaxes(showline=True, zeroline=True, zerolinecolor="black", showgrid=True, linewidth=2
                    , linecolor='black', gridcolor='lightgrey', mirror=True, ticks='outside')
    fig.update_yaxes(showline=True, zeroline=True, zerolinecolor="black", showgrid=True, linewidth=2
                    , linecolor='black', gridcolor='lightgrey', mirror=True, ticks='outside')
    print("Save Figure 4 at Figures/Figure 4.png.")
    fig.write_html(f"Figures/Figure4.html")
    fig.write_image(f"Figures/Figure4.png")
    fig.show()


if __name__ == "__main__":
    # True values
    list_mean = [[-5., 2.], [0.5, 4.9], [2.4, -1.2], [-2.4, -0.9]]
    list_cov = [np.array([[0.5, 0.2], [0.2, 0.2]]), np.array([[0.3, 0.1], [0.1, 0.9]])
                , np.array([[0.4, 0.25], [0.25, 0.4]]), np.array([[0.3, -0.25], [-0.25, 0.45]])]

    # Input space
    Xt = np.load("data/DPMRM/Xt.npy")
    colorlist = ["magenta", "brown", "blue", "olive", "purple", "orange"]
    mat_epl_true = np.load("data/DPMRM/mat_epl_true.npy")

    # GMR
    colorlist = ["brown", "magenta", "blue", "purple", "olive", "orange", "red", "green"]
    mat_epl = np.load("data/GMR/mat_epl.npy")
    mean_pred = np.load("data/GMR/mean_pred.npy", )
    list_idx = list(np.load("data/GMR/list_idx.npy"))
    list_unique = np.unique(list_idx)
    plot_models("GMR", mat_epl, mean_pred, list_idx, list_unique)

    # DPMRM -------------------------------------------
    colorlist = ["magenta", "brown", "blue", "olive", "purple", "orange"]
    mat_epl = np.load("data/DPMRM/mat_epl.npy")
    mean_pred = np.load("data/DPMRM/mean_pred.npy", )
    list_idx = list(np.load("data/DPMRM/list_idx.npy"))
    list_unique = np.unique(list_idx)
    plot_models("DPMRM", mat_epl, mean_pred, list_idx, list_unique)

    # DPIRMRM -------------------------------------------
    mat_epl = np.load("data/DPIRMRM/mat_epl.npy")
    mean_pred = np.load("data/DPIRMRM/mean_pred.npy", )
    list_idx = list(np.load("data/DPIRMRM/list_idx.npy"))
    list_unique = np.unique(list_idx)
    plot_models("DPIRMRM", mat_epl, mean_pred, list_idx, list_unique)

    # DPORMRM -------------------------------------------
    mat_epl = np.load("data/DPORMRM/mat_epl.npy")
    mean_pred = np.load("data/DPORMRM/mean_pred.npy", )
    list_idx = list(np.load("data/DPORMRM/list_idx.npy"))
    list_unique = np.unique(list_idx)
    plot_models("DPORMRM", mat_epl, mean_pred, list_idx, list_unique)

    # DPR2MRM -------------------------------------------
    mat_epl = np.load("data/DPR2MRM/mat_epl.npy")
    mean_pred = np.load("data/DPR2MRM/mean_pred.npy", )
    list_idx = list(np.load("data/DPR2MRM/list_idx.npy"))
    list_unique = np.unique(list_idx)
    plot_models("DPR2MRM", mat_epl, mean_pred, list_idx, list_unique)


    # Dirichlet process for component number determination 
    list_com_DPMRM = np.load("data/DPMRM/list_com_DPMRM.npy")
    list_com_DPIRMRM = np.load("data/DPIRMRM/list_com_DPIRMRM.npy")
    list_com_DPORMRM = np.load("data/DPORMRM/list_com_DPORMRM.npy")
    list_com_DPR2MRM = np.load("data/DPR2MRM/list_com_DPR2MRM.npy")
    plot_component(list_com_DPMRM, list_com_DPORMRM, list_com_DPIRMRM, list_com_DPR2MRM)




