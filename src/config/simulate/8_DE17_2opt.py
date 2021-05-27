import numpy as np

config = {
    'eta': 0.996,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([
        0.7637372464596878, 0.16776249759321427, 0.08671318058558053, 0.05751629972455663, 0.03470450865668595, 0.03429601168925189, 0.07082759391161564, 0.24681617015680252, 0.8383268808372397
    ]),  # 結合率
    'L': np.array([
        8.243181818181816e-05, 8.243181818181816e-05, 8.243181818181816e-05, 8.243181818181816e-05, 5.495454545454545e-05, 5.495454545454545e-05, 5.495454545454545e-05, 5.495454545454545e-05
    ]),  # リング周長
    'n_eff': 2.2,  # 実行屈折率
    'n_g': 4.4,  # 群屈折率
    'center_wavelength': 1550e-9,
    # 'lambda': np.arange(1520e-9, 1560e-9, 1e-12)
}
