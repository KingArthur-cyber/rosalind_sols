filename = "3sum.txt"
with open(filename) as f:
    lines  = f.readlines()
    num_size = lines[0].rstrip("\n").split(" ")
    arrays = []
    for line in lines:
        line = line.rstrip("\n").split(" ")
        arrays.append(line)
arrays = arrays[1:]
num = int(num_size[0])
size = int(num_size[1])
new_arrays = []
for i in range(0,num):
    temp = []
    for j in range(0,size):
        te = int(arrays[i][j])
        temp.append(te)
    new_arrays.append(temp)

def threeSum(nums):
    # Sort the given array
    nums.sort()
    # Length of the array
    n = len(nums)
    # Resultant list
    triplets = list()
    # Loop for each character in the array
    for i in range(0, n):
        # Avoid duplicates due to i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Left and right pointers
        j = i + 1
        k = n - 1
        # Loop for remaining pairs
        while j < k:
            if (nums[i] + nums[j] + nums[k] == 0) and (i < j < k):
                return [i+1,j+1,k+1]
                j += 1
                # Avoid duplicates for j
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1
    return [-1]
for i in range(0,len(new_arrays)):
    print(*threeSum(new_arrays[i]))