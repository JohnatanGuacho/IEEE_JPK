# 🪲 Problema: Bolsa de Escarabajo
# Solución optimizada - Programación Dinámica 0/1
# Compatible con jueces como IEEE Xtreme o CS Academy

import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return  # no hay entrada (caso en blanco)
    
    idx = 0
    t = int(data[idx]); idx += 1  # número de casos de prueba
    
    for _ in range(t):
        # capacidad c y número de gadgets n
        c = int(data[idx]); idx += 1
        n = int(data[idx]); idx += 1
        
        gadgets = []
        for _ in range(n):
            w = int(data[idx]); idx += 1
            f = int(data[idx]); idx += 1
            gadgets.append((w, f))
        
        # dp[i] = máximo poder de combate con capacidad i
        dp = [0] * (c + 1)
        
        for w, f in gadgets:
            for cap in range(c, w - 1, -1):
                dp[cap] = max(dp[cap], dp[cap - w] + f)
        
        print(dp[c])

if __name__ == "__main__":
    main()
