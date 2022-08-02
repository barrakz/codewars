lower_text = text.lower()

count = []

for x in lower_text:
    if not x in count and lower_text.count(x) > 1:
        count.append(x)

print(len(count))
