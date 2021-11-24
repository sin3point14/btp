import matplotlib.pyplot as plt
import json
with open('data3.json', 'r') as f:
    obj = json.loads(f.read())
y_axes = ['Tensile Strength, Ultimate', "Elongation at Break %", "Tensile Strength, Yield"]
for y_idx in y_axes:
    plt.figure()
    plt.xlabel('Magnesium, Mg %')
    plt.ylabel(y_idx)

    for i in obj:
        try:
            x = float(i["Composition"]['Magnesium, Mg'])
            # uncomment according to the required graph
            # y = float(i['Tensile Strength, Ultimate'])
            # y = float(i["Elongation at Break"])
            y = float(i[y_idx])
        except:
            continue
        p = plt.plot(x, y, 'ro')
    plt.savefig('./graphs/' + 'Magnesium, Mg vs ' + y_idx + '.png')
print("Find graphs in graphs/ folder")