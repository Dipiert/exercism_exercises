from string import ascii_uppercase


def rows(letter: str) -> list[str]:
    res = []
    
    if letter == "A":
        return ["A"]
    
    n = ascii_uppercase.index(letter) + 1
    
    for i in range(n):
        row = []
        for j in range(n):
            if i + j == n - 1:
                row.append(ascii_uppercase[i])
            else:
                row.append(" ")
        row += list(reversed(row[:len(row) - 1]))
        res.append("".join(row))

    return res + list(reversed(res[:len(res) - 1]))
        