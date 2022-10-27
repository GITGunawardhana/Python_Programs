original_list = [12, 67, 98, 34]

print("The original list = " + str(original_list))

result = []
for element in original_list:
    sum = 0
    for digit in str(element):
        sum += int(digit)
    result.append(sum)
    
print ("List Integer Summation = " + str(result))
