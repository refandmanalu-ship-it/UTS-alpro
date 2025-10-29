# Cetak papan Minesweeper 5x5 kosong

n = 5  # ukuran papan (5x5)

def print_board():
    print("\n\t\tMINESWEEPER", f"{n}x{n}\n")
    print("    " + "   ".join([str(i+1) for i in range(n)]))
    print("  +" + "---+" * n)
    for i in range(n):
        row = f"{i+1:2} | " + " | ".join([" " for _ in range(n)]) + " |"
        print(row)
        print("  +" + "---+" * n)

print_board() 