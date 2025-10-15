# Suma máxima de productos adyacentes
# Estrategia: greedy con deque (colocar cada elemento donde aporte más).
# Tie-break: a la IZQUIERDA para lograr lexicográfica menor.

import sys
from collections import deque

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    t = int(data[idx]); idx += 1

    out_lines = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n])); idx += n

        # 1) ordenar desc
        a.sort(reverse=True)

        # 2) construir con deque
        dq = deque([a[0]])
        total = 0

        for x in a[1:]:
            left = dq[0]
            right = dq[-1]
            gainL = x * left
            gainR = x * right

            if gainL > gainR:
                dq.appendleft(x)
                total += gainL
            elif gainR > gainL:
                dq.append(x)
                total += gainR
            else:
                # Empate: empujar a la IZQUIERDA para favorecer lexicográfica menor
                dq.appendleft(x)
                total += gainL

        out_lines.append(str(total))
        out_lines.append(" ".join(map(str, dq)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
