
# equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z 

# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.

# Constraints
# Print the list in lexicographic increasing order.

# Sample Input
# 1
# 1
# 1
# 2

# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


# Enter your code here. Read input from STDIN. Print output to STDOUT
def function(x,y,z,n):
    ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    return ans
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    t=function(x,y,z,n)
    print(t)
