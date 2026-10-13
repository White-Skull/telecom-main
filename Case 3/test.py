
import numpy as np
from scipy.special import erfinv
def calc_req_eb_over_n0(BER):
        Q_inv = np.sqrt(2) * erfinv(1.0 - 2.0 * BER)
        print(Q_inv)
        req_eb_over_n0 = 10 * np.log10(((Q_inv)**2)/2 )

        return req_eb_over_n0
rate = 1e-6
print(calc_req_eb_over_n0(rate))