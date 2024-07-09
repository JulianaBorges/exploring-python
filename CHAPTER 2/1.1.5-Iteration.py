    #interagindo com a lista 'concatenação + laço de repetição for'
    
bin_colors = ['red','green','blue','yellow']
for aColor in bin_colors:
    print(aColor+ " square")

numbers = [1,2,3]
letters = ['a','b','c']
combined = zip (numbers,letters)
combined_list = list(combined)
print(combined_list)