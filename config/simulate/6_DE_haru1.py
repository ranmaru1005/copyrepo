import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array([
        0.22889138542075615,
        0.0405207855678823,
        0.015973226425724296,
        0.023820780441116185,
        0.08105384780149838,
        0.03836179613752966,
        0.2935998269163348
    ]),  # 結合率
    "L": np.array(
        [
        0.00032972727272727266,
        0.000494590909090909,
        0.0002472954545454545,
        0.000989181818181818,
        0.0004396363636363636,
        0.0004396363636363636
    ]
    ),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1525e-9, 1555e-9, 1e-12)
}