import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


if __name__ == "__main__":
    # Generate simulation data in the numerical example
    len_simulation = 800
    list_mean = [[-5., 2.], [0.5, 4.9], [2.4, -1.2], [-2.4, -0.9]]
    list_cov = [np.array([[0.5, 0.2], [0.2, 0.2]]), np.array([[0.3, 0.1], [0.1, 0.9]])
                , np.array([[0.4, 0.25], [0.25, 0.4]]), np.array([[0.3, -0.25], [-0.25, 0.45]])]

    # You can do multiple simulations by changing the random seed
    np.random.seed(2003)

    Xt1 = np.random.multivariate_normal(mean=[-5., 2.], cov=[[0.5, 0.2], [0.2, 0.2]], size=200)
    Xt2 = np.random.multivariate_normal(mean=[0.5, 4.9], cov=[[0.3, 0.1], [0.1, 0.9]], size=200)
    Xt3 = np.random.multivariate_normal(mean=[2.4, -1.2], cov=[[0.4, 0.25], [0.25, 0.4]], size=200)
    Xt4 = np.random.multivariate_normal(mean=[-2.4, -0.9], cov=[[0.3, -0.25], [-0.25, 0.45]], size=200)

    # Add outliers to X
    Out_amount = int(800 * 0.05 / 4)
    Xt1[np.random.randint(low=0, high=200, size=(Out_amount,))] = np.hstack([np.random.uniform(low=-8, high=0, size=(Out_amount,1))
                                                                            , np.random.uniform(low=-2, high=6, size=(Out_amount,1))])
    Xt2[np.random.randint(low=0, high=200, size=(Out_amount,))] = np.hstack([np.random.uniform(low=-2.5, high=4., size=(Out_amount,1))
                                                                            , np.random.uniform(low=1.5, high=8, size=(Out_amount,1))])
    Xt3[np.random.randint(low=0, high=200, size=(Out_amount,))] = np.hstack([np.random.uniform(low=-1, high=6, size=(Out_amount,1))
                                                                            , np.random.uniform(low=-5, high=2.5, size=(Out_amount,1))])
    Xt4[np.random.randint(low=0, high=200, size=(Out_amount,))] = np.hstack([np.random.uniform(low=-6, high=1, size=(Out_amount,1))
                                                                            , np.random.uniform(low=-4.5, high=3, size=(Out_amount,1))])
    Xt = np.concatenate([Xt1
                        , Xt2
                        , Xt3
                        , Xt4
                        ], axis=0)

    theta1 = np.array([[2.4, -0.32]]).T  
    theta2 = np.array([[-1.8, 3.8]]).T
    theta3 = np.array([[-0.9, 4.2]]).T
    theta4 = np.array([[-1.2, 1.6]]).T

    Out_amount = int(800 * 0.05 / 4)
    noise1 = np.random.normal(loc=0, scale=0.5, size=(Xt1.shape[0], 1))
    noise2 = np.random.normal(loc=0, scale=0.5, size=(Xt1.shape[0], 1))
    noise3 = np.random.normal(loc=0, scale=0.5, size=(Xt1.shape[0], 1))
    noise4 = np.random.normal(loc=0, scale=0.5, size=(Xt1.shape[0], 1))
    yt_true = np.concatenate([
        Xt1 @ theta1 + noise1,
        Xt2 @ theta2 + noise2,
        Xt3 @ theta3 + noise3,
        Xt4 @ theta4 + noise4,
    ]).ravel()

    # Add outliers to Y
    noise1[np.random.randint(low=0, high=200, size=(Out_amount,))] = np.random.uniform(low=-20, high=-15., size=(Out_amount,1))
    noise2[np.random.randint(low=0, high=200, size=(Out_amount,))] = np.random.uniform(low=-20, high=-15., size=(Out_amount,1))
    noise3[np.random.randint(low=0, high=200, size=(Out_amount,))] = np.random.uniform(low=-20, high=-15., size=(Out_amount,1))
    noise4[np.random.randint(low=0, high=200, size=(Out_amount,))] = np.random.uniform(low=-20, high=-15., size=(Out_amount,1))

    yt = np.concatenate([
        Xt1 @ theta1 + noise1,
        Xt2 @ theta2 + noise2,
        Xt3 @ theta3 + noise3,
        Xt4 @ theta4 + noise4,
    ]).ravel()

    # Save simulation data
    df = pd.DataFrame(np.hstack([Xt, yt[:, np.newaxis]]), columns=["x1", "x2", "y"])
    print(r"Save simulation data at SuppMaterial\NumericalEx\Simulation\data\simulation.csv.")
    df.to_csv("data/simulation.csv")

    # Generate Figure F1 in the Supplementary material 
    list_index = [0] * 200 + [1] * 200 + [2] * 200 + [3] * 200
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Xt[:, 0], y=Xt[:, 1], mode="markers"
                            , marker={"color":list_index}, text=list_index))

    fig.update_layout(width=800, height=600, title="生成数据:X域", plot_bgcolor='white')
    fig.update_xaxes(showline=True, zeroline=True, zerolinecolor="black", showgrid=True, linewidth=2
                    , linecolor='black', gridcolor='black', mirror=True, ticks='outside')
    fig.update_yaxes(showline=True, zeroline=True, zerolinecolor="black", showgrid=True, linewidth=2
                    , linecolor='black', gridcolor='black', mirror=True, ticks='outside')

    fig.show()
    print(r"Save Figure F1 at SuppMaterial\NumericalEx\Simulation\Figures\Figure F1.png.")
    fig.write_html("Figures/FigureF1.html")
    fig.write_image("Figures/FigureF1.png")


    # Generate Figure F2 in the Supplementary material 
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[i for i in range(len(yt))], y=yt.ravel(), line_color="black"))
    fig.update_layout(width=800, height=400, plot_bgcolor='white')
    fig.update_layout(yaxis_range=[-50,30])
    fig.update_xaxes(showline=True, zeroline=True, zerolinecolor="black", showgrid=True, linewidth=2
                    , linecolor='black', gridcolor='black', mirror=True, ticks='outside')
    fig.update_yaxes(showline=True, zeroline=True, zerolinecolor="black", showgrid=True, linewidth=2
                    , linecolor='black', gridcolor='black', mirror=True, ticks='outside')
    fig.show()
    print(r"Save Figure F2 at SuppMaterial\NumericalEx\Simulation\Figures\Figure F2.png.")
    fig.write_html("Figures/FigureF2.html")
    fig.write_image("Figures/FigureF2.png")