currDict = {}
with open("Projects Practice\CurrencyChart.txt","r") as f:
    lines = f.readlines()
for line in lines:
    parsed = line.split("\t")
    currDict[parsed[0]] = parsed[1]
amount = int(input("Enter Amount: "))
[print(i) for i in currDict.keys()]
currency = input("Select Currency")
print(f"Inr:{amount} to {currency} is {amount*float(currDict[currency])}")