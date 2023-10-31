import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array([
        0.1452012509975275,
        0.061510556664707505,
        0.049046743348673594,
        0.033775533530559676,
        0.04125280519384927,
        0.0846085601600361,
        0.565551089227188
    ]),  # 結合率
    "L": np.array(
        [
        7.749999999999999e-05,
        7.749999999999999e-05,
        6.2e-05,
        6.2e-05,
        6.2e-05,
        6.2e-05
    ]
    ),  # リング周長
    "n_eff": 2.2,  # 実行屈折率
    "n_g": 4.4,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1510e-9, 1555e-9, 1e-12)
}
