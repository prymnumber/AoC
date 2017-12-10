
import sys
import pdb

def inverse_captcha(input_file):
    l_input_file = sys.argv[1]
    fo = open(input_file, 'r')
    l_data = fo.read().rstrip()
    fo.close()
    print(l_data)
    pdb.set_trace()
    final_sum = 0
    file_len = len(l_data)


    for i in range(file_len):
        num1 = int(l_data[i])
        if i == file_len:
            num2 = int(l_data[0])
        else:
            num2 = int(l_data[i+1])

        if num1 == num2:
            final_sum += num1
            print('num1: ',num1,'num2: ',num2)

    return final_sum

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])

result = inverse_captcha(l_file)
print('Result:',str(result))
