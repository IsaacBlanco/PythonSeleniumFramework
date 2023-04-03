text = """
な  周 歩 廊 そ
る  囲 い 下 の
だ  の て にょ
る  邪 は 広 う
う  魔    が に
    に    っ
          て
"""

# Split the text into lines
lines = text.split('\n')

# Transpose the lines to convert columns to rows
rows = []
for i in range(len(lines[0])):
    row = ''
    for line in lines:
        row += line[i]
    rows.append(row)

# Join the rows into a single string
result = '\n'.join(rows)

# Print the result
print(result)