import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": [
        0.4661268353351671,
        0.053506308950430514,
        0.09095256554241021,
        0.32038042236935976,
        0.34541438249503337,
        0.08672733705663815,
        0.023094514140453826,
        0.09682721567525426,
        0.3283449787587172,
        0.13206381611022822,
        0.19212341206108685,
        0.5306287723621403,
        0.7989838133991178,
    ],  # 結合率
    "L": [
        5.495454545454545e-05,
        5.495454545454545e-05,
        0.00019234090909090907,
        0.00019234090909090907,
        0.00019234090909090907,
        5.495454545454545e-05,
        5.495454545454545e-05,
        0.00019234090909090907,
        0.00019234090909090907,
        5.495454545454545e-05,
        0.00019234090909090907,
        5.495454545454545e-05,
    ],  # リング周長
    "n_eff": 2.2,  # 実行屈折率
    "n_g": 4.4,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1520e-9, 1560e-9, 1e-12),
    "label": r"12th, E=14.04",
}
