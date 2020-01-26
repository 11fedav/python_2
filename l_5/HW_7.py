import json

firm = {}
ave_profit = []

with open('firm.txt') as f:
    lines = f.readlines()
    for line in lines:
        name_firm, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm[name_firm] = profit
        if profit > 0:
            ave_profit.append(profit)

ave_profit = sum(ave_profit) / len(ave_profit)
info = [firm, {'ave_profit': ave_profit}]

with open('firm.json', 'w') as f_json:
    json.dump(info, f_json)

with open('firm.json') as f_json:
     print(json.load(f_json))