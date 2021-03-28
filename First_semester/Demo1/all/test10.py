import csv
def setAmount():
    data_string = []
    with open('500_constituents_financial.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        check = False 
        for row in csv_reader:
            if check:
                data_string.append(row)
            check = True
    return data_string
     

def output_file(data_string):
    csvfile = None 
    with open("demofile2.csv", "w") as csvfile:
        A = [ "Symbol", "Name", "Sector", "Price", "Price/Earnings", "Dividend Yield", "Earnings/Share", "52 Week Low", "52 Week High", "Market Cap", "dag", "Price/Sales", "Price/Book", "SEC Filings"]
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(A)
        print(data_string)
        writer.writerows(data_string)


    # for i in data_string:
    #     temp = []
    #     for j in i:
    #         t = ""
    #         if j != ',':
    #             t += j
    #         else:
    #             temp.append(t)
    #             t = ""
    #     #print(temp)
    #     writer.writerows(temp)

print(123)

data = setAmount()

print(123)

output_file(data)
print(123)
