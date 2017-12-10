
import sys
import pdb
from common import get_file as get_file

def inverse_captcha(input_data, start_num, step_num):

    final_sum = 0
    file_len = len(input_data)

    pdb.set_trace()
    for i in range(file_len):
        num1 = int(l_data[i])
        if i+step_num > file_len-1:
            #num2 = int(l_data[-file_len+step_num+i-1])
            num2 = int(l_data[i+step_num-file_len])
        else:
            num2 = int(l_data[i+step_num])

        if num1 == num2:
            final_sum += num1
            print('num1: ',num1,'num2: ',num2)


    return final_sum

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])

l_data = get_file(l_file)
print(l_data)
#pdb.set_trace()

# l_step = 1
# print('day 1 part 1 l_step',l_step)
# result = inverse_captcha(l_data,0,l_step)
# print('Day 1 part 1 Result:',str(result))

print('')
l_step = (len(l_data)/2)
print('day 1 part 2 l_step',l_step)
result = inverse_captcha(l_data,0,l_step)
print('Day 1 part 2 Result:',str(result))
