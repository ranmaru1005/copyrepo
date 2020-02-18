import numpy as np


class MRR:
    def __init__(
        self,
        eta,
        n,
        alpha,
        K,
        L
    ):
        self.eta = eta
        self.n = n
        self.a = np.exp(- alpha * L)
        self.K = K
        self.L = L

    def _C(self, K_k):
        return 1 / (-1j * self.eta * np.sqrt(K_k)) * np.matrix([
            [1, - self.eta * np.sqrt(self.eta - K_k)],
            [np.sqrt(self.eta - K_k) * self.eta, - self.eta ** 2]
        ])

    def _R(self, a_k, L_k, l):
        return np.matrix([
            [np.exp(1j * np.pi * L_k * self.n / l) / np.sqrt(a_k), 0],
            [0, np.exp(-1j * np.pi * L_k * self.n / l) * np.sqrt(a_k)]
        ])

    def _reverse(self, arr):
        return arr[::-1]

    def _M(self, l):
        product = 1
        for _K, _a, _L in zip(
            self._reverse(self.K[1:]),
            self._reverse(self.a),
            self._reverse(self.L)
        ):
            product = product * self._C(_K) * self._R(_a, _L, l)
        product = product * self._C(self.K[0])
        return product

    def _D(self, l):
        return 1 / self._M(l)[0, 0]

    def print_parameters(self):
        print('eta:', self.eta)
        print('n:', self.n)
        print('a:', self.a)
        print('K:', self.K)
        print('L:', self.L)

    def simulate(self, l):
        y = 20 * np.log10(np.abs(self._D(l)))
        return y.reshape(y.size)
