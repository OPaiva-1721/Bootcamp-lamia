lockdown = True
grana = 30

status = "Em casa" if lockdown or grana <= 100 else "Fora de casa"

print(f"Status: {status}")