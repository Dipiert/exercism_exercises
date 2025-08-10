from string import ascii_uppercase


def rows(letter: str) -> list[str]:
    res = []

    n = ascii_uppercase.index(letter) + 1
    blank_row = [ " " for _ in range(n * 2 - 1)]
    
    for row_letter in ascii_uppercase[:n]:
        row = blank_row.copy()
        j = ascii_uppercase.index(row_letter)
        row[n - j - 1] = row_letter
        row[-n + j] = row_letter
        res.append("".join(row))

    return res + list(reversed(res[:len(res) - 1]))