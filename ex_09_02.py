# Entering file name and making sure there won't be traceback with try/except
fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print("File not found")
    exit()

# Creating a new list, and appending the index 2 item from each line that starts with 'From '
lst = list()
for line in fhandle:
    if not line.startswith("From ") : continue
    words = line.split()
    lst.append(words[2])

# Creating a new dictionary and adding all items from the previous list with count values
daysCount = dict()
for day in lst:
    daysCount[day] = daysCount.get(day, 0) + 1

print(daysCount)