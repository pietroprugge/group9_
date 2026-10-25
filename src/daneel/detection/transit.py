import batman
import numpy as np
import matplotlib.pyplot as plt

#parametri WASP-39 b
params = batman.TransitParams()
params.t0 = 0.0                     # tempo centrale transito
params.per = 4.055259               # per orb
params.rp = 0.1399                  # raggio
params.a = 11.056                    # semiax max 
params.inc = 87.73                  # inclinazione
params.ecc = 0.0                    # eccentricita
params.w = 90.0                     # periastro
params.limb_dark = "quadratic"      
params.u = [0.693, 0.110]             # coefficienti limb dark

#vettore temp e curve lux
t = np.linspace(-0.08, 0.08, 100)

m = batman.TransitModel(params, t)
flux = m.light_curve(params)

plt.figure(figsize=(8, 5))
plt.plot(t * 24, flux, label='Batman model (WASP-39 b)', color='navy', lw=2)
plt.xlabel("Hours from mid-transit")
plt.ylabel("Normalized Flux")
plt.title("Theoretical Light Curve for WASP-39 b")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig("wasp39b_assignment1_taskF.png", dpi=300)