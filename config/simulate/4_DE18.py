import numpy as np

config = {
    "eta": 0.996,
    "alpha": 52.96,
    "K": [0.12395188629725941, 0.030807624452130217, 0.03493053701137464, 0.02301971078881386, 0.44123167392946],
    "L": [2.7477272727272726e-05, 0.0001099090909090909, 2.7477272727272726e-05, 2.7477272727272726e-05],
    "n_eff": 2.2,
    "n_g": 4.4,
    "center_wavelength": 1.55e-06,
    "lambda_limit": np.arange(1520e-9, 1560e-9, 1e-12),
    "label": "\\(\\times 1.000\\)",
}
