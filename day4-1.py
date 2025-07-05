target_word = "XMAS"
lentarget_word = len(target_word)
count = 0

# read txt file
with open("wordsearch.txt", "r") as file:
    lines = file.readlines()

grid = [line.strip() for line in lines]

directions = [ (0,1) #right
              ,(0,-1) #left
              ,(-1,0) #up
              ,(1,0) #down
              ,(1,1) #down,right
              ,(1,-1) #down,left
              ,(-1,1) #up,right
              ,(-1,-1) #up,left
]

for row in range(len(grid)):
    for col in range (len(grid[0])):
        for vert, hori in directions:
            match = True
            for i in range(lentarget_word):
                new_r, new_c = row + i * vert, col + i * hori

                # handle case where coordinate is out of bounds
                if not (0 <= new_r < len(grid)) or not (0 <= new_c < len(grid[0])):
                    match = False
                    break

                if grid[new_r][new_c] != target_word[i]:
                    match = False
                    break
            if match:
                count += 1
print(count)      
            
            