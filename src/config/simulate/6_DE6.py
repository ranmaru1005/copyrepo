import numpy as np

config = {
    'eta': 0.996,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([
        0.49286763,
        0.09295679,
        0.04864514,
        0.1154788,
        0.17765715,
        0.09735724,
        0.45886766
    ]),  # 結合率
    'L': np.array([
        2.87730568e-05,
        2.87730568e-05,
        2.87730568e-05,
        8.63191703e-05,
        2.87730568e-05,
        1.15092227e-04
    ]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'center_wavelength': 1550e-9,
    # 'lambda': np.arange(1525e-9, 1555e-9, 1e-12)
}