# Advent Of Code 2022
I probably shouldn't have ignored this the past two years

### Day 1
A python list initialized to [0], then go through each line in a loop. If the line is empty then append a new 0 to the list, otherwise add the number to the last index. The variable currentElf wasn't even needed, I could have just done elves[-1]. Then max(elves) gets the highest one and for the three highest just sort it and get the three highest. If I had to optimize it I wouldn't keep an array with all of them, just keep the highest value, then at each empty line compare the current elf with the best elf and choose the larger one. For part 2 maybe keep an array of 3 initialized to [0,0,0], compare each elf to the third one and if larger move it there, then the second one and then first. That works fine for the 3 best but for a large amount like 100000 maybe a balanced binary tree for fast insertions? Anyway that's too much thinking about this problem.
