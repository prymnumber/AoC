import math
import pdb
import sys

def find_radius_corner(input_num = 1):
    idx = 0
    odd_num = 1
    ret_val = 1
    if input_num == 1:
        ret_val = 1
    else:
        while ret_val <= input_num:
            odd_num += 2
            ret_val = odd_num**2
            idx += 1

    return idx,ret_val

def find_row_col(input_radius,input_corner,input_num):
    r = input_radius
    #pdb.set_trace()
    if input_radius == 0:
        c = 0
    else:
        sqr_num = input_corner
        diff_num = sqr_num - input_num

        sqr_rt_num = math.sqrt(sqr_num)
        half_rad = sqr_rt_num//2
        c = (diff_num%(sqr_rt_num-1))-half_rad
        if input_num <= (input_corner/2):
            c = abs(c)

    return int(c),int(r)

class coord :
    def __init__(self,xi,yi,vali):
        self.x = xi
        self.y = yi
        #self.val = vali

class spiral :
    def __init__(self,coord,val):
        self.spiral_coords = zip(coord,val)

    def get(coord):
        for item in self.spiral_coords:
            if coord.x == item.x and coord.y == item.y:
                return item.val

    def set(coord):
        self.spiral_coords.append(coord)


def find_neighbors(r,c):
    neighbors = []
    if r==0 and c==0:
        neighbors = [r,c]
        return neighbors
    xr  = r
    neg_xr = r-1
    pos_xr = r+1
    xc = c
    neg_xc = c-1
    pos_xc = c+1

    neighbors.append([xr,pos_xc]) #up
    neighbors.append([xr,neg_xc]) #down
    neighbors.append([pos_xr,xc]) #right
    neighbors.append([neg_xr,xc]) #left

    neighbors.append([neg_xr,neg_xc]) #diag left down
    neighbors.append([neg_xr,pos_xc]) #diag left up

    neighbors.append([pos_xr,pos_xc]) #diag right up
    neighbors.append([pos_xr,neg_xc]) #diag right down
    return neighbors

def get_val(coord,coord_list):
    ret_val = 1
    x=coord[0]
    y=coord[1]
    pdb.set_trace()
    if (x==0 and y==0) or (coord_list is None):
        return ret_val
    else:
        for item in coord_list:
            if len(item) == 2:
                ret_val += item[1]
    return ret_val


# radius, corner = find_radius_corner(2)
# r,c = find_row_col(radius,corner,2 )
# print('value:',2,'Row:',r,'Column:',c)
#
# radius, corner = find_radius_corner(3)
# r,c = find_row_col(radius,corner,3)
# print('value:',3,'Row:',r,'Column:',c)
#
# radius, corner = find_radius_corner(4)
# r,c = find_row_col(radius,corner,4)
# print('value:',4,'Row:',r,'Column:',c)
#
# radius, corner = find_radius_corner(5)
# r,c = find_row_col(radius,corner,5)
# print('value:',5,'Row:',r,'Column:',c)

#print('Radius:',radius)
#print('Corner:',corner)

d3_num = int(sys.argv[1])

l_list = []
print('l_list:',l_list)
pdb.set_trace()

for i in range(d3_num):
    print("")
    print('i:',i)
    radius, corner = find_radius_corner(i)
    r,c = find_row_col(radius,corner,i)
    nb = find_neighbors(r,c)
    #print('Neighbors found: ',nb)
    v = get_val([r,c],l_list)
    l_list.append([[r,c],v])

print('final_list:',l_list)
# r,c = find_row_col(radius,corner,2 )
# print('value:',2,'Row:',r,'Column:',c)


#nbval = zip(nb,range(len(nb)))
#print('nbval',nbval)
