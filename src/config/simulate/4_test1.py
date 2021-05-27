import numpy as np

config = {
    'eta': 1,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([0.14461252, 0.10823955, 0.54928258, 0.59230675, 0.90126621]),  # 結合率
    'L': np.array([8.35788791e-05, 5.29332901e-04, 5.29332901e-04, 5.29332901e-04]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'center_wavelength': 1550e-9,
    # 'lambda': np.arange(1525e-9, 1575e-9, 1e-12)
}