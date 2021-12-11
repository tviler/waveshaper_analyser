import numpy as np
import scipy.io.wavfile as wav
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def wavread(filename):
    data = wav.read(filename)
    return data[1][0:10000]/(2**16/2)

def f_sin(x, a, b):
    return a*np.sin(b*np.pi*x)

def f_tanh(x, a, b):
    return a*np.tanh(b*x)

def f_poly4(x, a, b, c, d, e):
    return(e*x**4 + d*x**3 + c*x**2 + b*x + a)

def f_poly3(x, a, b, c, d):
    return(d*x**3 + c*x**2 + b*x + a)

def f_poly2(x, a, b, c):
    return(c*x**2 + b*x + a)

def main():
    dry = wavread("TEST.wav")
    wet = wavread("RESULT.wav")

    plt.figure(figsize = (12, 9), dpi = 150)
    plt.plot(dry, wet, label="Waveshape")
    plt.axis([-1, 1, -1, 1])
    plt.savefig("results/waveshape.png")

    functions = [f_sin, f_tanh, f_poly4]
    coeff = {}

    mask_pos = dry >= 0

    for func in functions:
        try:
            popt, pcov = curve_fit(func, dry[mask_pos], wet[mask_pos], maxfev = 20000)
        except RuntimeError:
            coeff[f"{func.__name__}"] = [[np.nan for i in range(5)], np.nan]
            continue
        coeff[f"{func.__name__}"] = [popt, np.sqrt(np.diag(pcov))]
        plt.plot(dry, func(dry, *popt), label=f"{func.__name__}")

    plt.legend()
    plt.axis([0,1,0,1])
    plt.savefig("results/curve_fit.png")
    plt.axis([0.6,1,0.6,1])
    plt.savefig("results/curve_fit_zoom.png")

    report = f"""Curve fitting coeffecients:

A*sin(B*pi*x)
A = {coeff["f_sin"][0][0]:.6f}, B = {coeff["f_sin"][0][1]:.6f}

A*tanh(B*x)
A = {coeff["f_tanh"][0][0]:.6f}, B = {coeff["f_tanh"][0][1]:.6f}

E*x^4 + D*x^3 + c*x^2 + b*x + a
E = {coeff["f_poly4"][0][4]:.6f}, D = {coeff["f_poly4"][0][3]:.6f}, c = {coeff["f_poly4"][0][2]:.6f}, B = {coeff["f_poly4"][0][1]:.6f}, A = {coeff["f_poly4"][0][0]:.6f}
"""

    """
D*x^3 + c*x^2 + b*x + a
D = {coeff["f_poly3"][0][3]:.6f}, c = {coeff["f_poly3"][0][2]:.6f}, B = {coeff["f_poly3"][0][1]:.6f}, A = {coeff["f_poly3"][0][0]:.6f}

c*x^2 + b*x + a
c = {coeff["f_poly2"][0][2]:.6f}, B = {coeff["f_poly2"][0][1]:.6f}, A = {coeff["f_poly2"][0][0]:.6f}
"""

    with open("results/curve_fit.txt", "w") as file:
        file.write(report)

if __name__ == "__main__":
    main()
