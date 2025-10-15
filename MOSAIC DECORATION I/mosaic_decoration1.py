import sys

def solve():
    try:
        N, CB, CP = map(int, sys.stdin.readline().split())
    except:
        return

    total_black_tiles = 0
    total_pink_tiles = 0
    
    for _ in range(N):
        try:
            B_i, P_i = map(int, sys.stdin.readline().split())
            total_black_tiles += B_i
            total_pink_tiles += P_i
        except:
            break
            
    TILES_PER_PILE = 10
    
    black_piles = total_black_tiles // TILES_PER_PILE
    if total_black_tiles % TILES_PER_PILE != 0:
        black_piles += 1

    pink_piles = total_pink_tiles // TILES_PER_PILE
    if total_pink_tiles % TILES_PER_PILE != 0:
        pink_piles += 1
        

    total_cost = (black_piles * CB) + (pink_piles * CP)
    
    print(total_cost)

if __name__ == "__main__":
    solve()
