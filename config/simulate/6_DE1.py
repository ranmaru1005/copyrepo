import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array([0.99593624, 0.3996031, 0.09408226, 0.05060384, 0.0622486, 0.08218834, 0.31024059]),  # 結合率
    "L": np.array(
        [7.80069539e-04, 8.35788791e-05, 8.35788791e-05, 8.35788791e-05, 8.35788791e-05, 8.35788791e-05]
    ),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    'lambda_limit': np.arange(1525e-9, 1555e-9, 1e-12)
}
