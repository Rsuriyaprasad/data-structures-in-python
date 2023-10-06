solution 1

# reverse
l = 0
r = len(matrix) -1
while l < r:
	matrix[l], matrix[r] = matrix[r], matrix[l]
	l += 1
	r -= 1
# transpose 
for i in range(len(matrix)):
	for j in range(i):
		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

solution 2
(time limit exceeded)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left,right= 0,len(matrix)-1
        while left < right:
         for i in range(right-1):
            top,bottom=left,right
            # storing top left
            topleft=matrix[top][left+i]

            #moving bottom left to top left
            matrix[top][left+i]=matrix[bottom-i][left]

            #moving bottom right to bottom left
            matrix[bottom-i][left]=matrix[bottom][right-i]

            #moving top right to bottom right
            matrix[bottom][right-i]=matrix[top+i][right]

            #moving top left to top right
            matrix[top+i][right]=topleft
         right-=1
         left-=1

