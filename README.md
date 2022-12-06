# Advent Of Code 2022
I probably shouldn't have ignored this the past two years

### Day 1
A python list initialized to [0], then go through each line in a loop. If the line is empty then append a new 0 to the list, otherwise add the number to the last index. The variable currentElf wasn't even needed, I could have just done elves[-1]. Then max(elves) gets the highest one and for the three highest just sort it and get the three highest. If I had to optimize it I wouldn't keep an array with all of them, just keep the highest value, then at each empty line compare the current elf with the best elf and choose the larger one. For part 2 maybe keep an array of 3 initialized to [0,0,0], compare each elf to the third one and if larger move it there, then the second one and then first. That works fine for the 3 best but for a large amount like 100000 maybe a balanced binary tree for fast insertions? Anyway that's too much thinking about this problem.

### Day 2
Check each case except for loss (0 points) and add the corresponding result. In part 2 check all 9 cases and add the value corresponding to the play. It feels so wrong but it's about doing it quickly. Also I was up at 5 in the morning for this one so I have accurate times now. 6:28 for 1 star, top 983 global, 13:25 for both stars, top 1906 global. Maybe I should have hesitated less about making horrible hacky code but it still wouldn't have made me top 100. That was 3:43 for one star, 6:16 for both. If I had to do rock paper scissors again I'm not sure if I would use a bunch of if statements from the beginning or use the cleaner code that is shorter but harder to remember. Also the cleaner code version is definitely better but specific to rps. If there were more possible moves with a more complex graph of wins and losses then using modulo is useless. Instead I think I would use a function or class to make each play have a winsVS set with all the other plays it wins against. Then check if p1 is in p2's winsVS, if p2 is in p1's winsVS and if neither then it's a draw.

### Day 3
This one felt better than yesterday. Using sets and then calculating their intersections to find the one element present in both halves of the line or in the three lines. Although I didn't know how to get the only element from the set so I googled it and found `(common,) = a.intersection(b)`. However `common = a.intersection(b).pop()` feels more natural. I lost time on googling that and even using sets at all. While using sets makes it O(n) where n is the number of characters per line, the slower O(n^2) alternative approach of going through every character in one string and checking `char in string2` is faster to type than sets. Also lost a bit of time by forgetting to set value to 0 after part 1. Got 5:58 for star 1, top 879, and 12:35 for star 2, top 1500. Top 100 1 star is 3:03 and 2 stars is 5:24.

Day 4 edit: Just found out about how something like `set(str1).intersection(set(str2))` also computes the intersection. Definitely consider the possibility of casting to another type because of course python can probably do it.

### Day 4
Very easy problem, did it too slowly. Lost to Maxim on both stars today so I have to win twice now to get top 1. I'm not even sure where I lost so much time. 9:39 for star 1, top 4381, 11:29 for star 2, top 3173. Top 100 1 star is 2:12 and 2 stars is 3:22. This problem was easier than yesterday's but I did star 1 way slower. Definitely not just about how short the code is, most of it has to be thinking slowly, but I made a shorter version of the code too. That would be faster to code, especially given the ints function being coded before starting, which I will have from now at the beginning and remove it for github if unused. Also some of the time lost was from failing the test because I copy and paste it without a newline at the end so the line reading code takes that and removes the last int as opposed to the newline. I changed that code a bit to be more robust against missing newlines.

### Day 5
Still very easy, but more annoying to parse than the previous ones. 1 star 30:44, 2 stars 37:36. Top 100 was 6:42 and 7:58. Yesterday I recorded myself solving a few easy kattis problems and tried to find where i'm too slow. One of the things I need to do is use 1 or 2 letter variables which is why the code is so horrendous. Also I think I should look at some convenient python features like list comprehensions and the map function to reduce my usage of for loops. For example extracting the crates from a line could be simply done with `[line[i] for i in range(1, len(line), 4]`. Another hard thing is managing the level of stress. If I stress myself too much to do it fast I may type something very fast and then have to pause. Also sometimes with bugs I get stuck for a second looking at the error without thinking of anything. Ideally I should be relaxed and alert so I can calmly recognize what to do next without stopping to think of where I left.

As for the problem, parse everything and just do operations on a bunch of stacks. Part 1 is popping several times from stack X and pushing to Y, part 2 is like popping from X into temp and then from temp into Y. Forgot that the + operator can concatenate lists.

### Day 6
I overslept so my times were 01:44:09 and 01:45:00. However I recorded this one and starting from the point where I open the problem my times are 4:05 and 4:55. Top 100 was 1:52, 2:25. My times were pretty slow considering how trivial today's problem was in python. No chance to use list comprehensions and maps either. Most of my time loss was reading because I wasn't sure if I got it right. For optimization in C I think I would take the char pointer, get a temp char variable, and in a for loop set the character 4 (or 14) positions later to 0 while saving it in temp, check if the current string has different characters, then set the 0 character to temp again and increase the pointer by 1.
