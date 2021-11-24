import json
with open('data.json', 'r') as f:
    obj = json.loads(f.read())
toRemove = []
def cleanIdx(obj, j):
    obj[j] = obj[j].replace('%', '').strip()
    if '>=' in obj[j]:
        obj[j] = float(obj[j].replace('>=','').strip())
    elif '<=' in obj[j]:
        obj[j] = float(obj[j].replace('<=','').strip())
    elif '-' in obj[j]:
        x,y = map(lambda x: float(x.strip()), obj[j].split(' - '))
        obj[j] = (x + y) / 2
for idx, i in enumerate(obj):
    curr = i["Composition"]
    if curr == 'MISSING':
        toRemove.append(idx)
        continue
    for j in curr:
        print(j,curr)
        print(curr[j], type(curr[j]))
        cleanIdx(curr, j)
    cleanIdx(i, "Elongation at Break")
for i in toRemove[::-1]:
    del obj[i]
with open('data3.json', 'w') as convert_file:
    convert_file.write(json.dumps(obj))