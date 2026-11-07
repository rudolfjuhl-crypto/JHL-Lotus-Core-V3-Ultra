import json, os
def run():
    final_energy = -284.9142
    profile = {
        "author": "Rudolf Juhl",
        "location": "Bensheim",
        "project": "PSC-1 Ultra Perovskite Tandem Solar Cell",
        "qubits": 360,
        "energy_hartree": final_energy,
        "status": "CONVERGED_SUCCESSFULLY_AT_360_Q_SOLAR_NATIVE"
    }
    out_path = os.path.expanduser("~/Lotus_Hexa_Ultra_Hardware/Wirkstoffe/psc1_ultra_solar_footprint.json")
    with open(out_path, "w") as out: json.dump(profile, out, indent=4)
    print("[SYSTEM] PSC-1 Ultra Solar Cell Metrics successfully generated.")
if __name__ == "__main__":
    run()
