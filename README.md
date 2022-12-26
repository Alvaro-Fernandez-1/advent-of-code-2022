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

### Day 7
Hardest day yet, but still straightforward. Also I'm not used to working with graphs. I can but I don't do it often. For this just build a tree and keep track of your position, add all the directories and files to the tree in your current position as you move, and then search it for whatever you need. Star 1 40:34, top 3528. Star 2 1:02:34, top 5013. Top 100 was 10:49, 14:47.

### Day 8
Overslept again, but it took a while. Around 1 hour for star 1 and 1:21 for star 2. Top 100 was 4:30 and 10:12. I could have done it faster by checking everything up to each border in part 1, but I was afraid it would be too slow so instead I added a dictionary with info about the largest tree up to that point in all directions, so the next one would only have to check that. I'm going to relearn the basics of C++ that I learned about 5 years ago, then learn templates and whatever other features, and I'll switch from python to C++ because many people say it's the best language for this stuff due to being very fast and having a lot of standard library functions and classes. Also macros can shorten for loops and maybe other stuff.

### Day 9
For part 2 I got the wrong result and was looking for where the bug could be, and then I realized I was only taking 8 points after the head instead of 9. Star 1 20:21, star 2 50:49. Top 100 was 7:32 and 14:08. The concept was simple, first move the head according to the input and then move the tail according to where the head is and save the new position to a set and at the end print the length of the set. For a longer chain move the head the same as before and then every node after that moves according to the position of the previous node.

### Day 10
Pretty easy but I messed up a bit with the placement of the +1s at the beginning. I got 17:01 top 3119 and 29:17 top 2099. Top 100 was 5:17 and 12:17.

### Day 11
Part 2 was the first time this year that something wasn't straightforward. As always, just parse the input and do what this says. The stress levels in part 1 mever go too high, but in part 2 as soon as you stop dividing by 3 it goes wild. All that matters for the monkeys is if it's divisible by some number. For that all you need is the stress level modulo that number. To keep the info for all monkeys we can just multiply all their stress checks and use that as modulo to stop stress from crashing the python program or overflowing in a fixed length int. If there were 1000 monkeys that number would also be big, but then we could store the stress level as an array where the ith position is the stress modulo the ith monkey's stress check. I got 45:30, top 4042 and 56:09, top 2350. Top 100 was 13:07 and 18:05.

### Day 12
Easy as soon as you realize it's just dijkstra after building a graph with edges representing the moves you can make. Still took a few seconds to realize, and then a long time to take the dijkstra i once coded in python for practice and adapt it to this node class I made for advent of code. I got 01:04:31 top 4612, 01:15:25 top 4607. Top 100 was 7:39 and 9:46.

### Day 13
At first i was hoping to just parse this to a list but after a while of being stuck I decided to use a tree and be done with it. Once parsed just make a compare function and sorting can be done with the compare function. Star 1 54:10 top 3808 star 2 01:06:16 top 3598. Top 100 was 8:16, 12:56.

### Day 14
Made a dict with coordinates as keys, walls being "#" and sand being "o". The floor in the second part isn't in the dictionary, it's just a collision check with a coordinate. For part 1 searched the lowest rock so that I can check when sand goes below it meaning that new sand will fall from now on. Star 1 26:21 top 1403, star 2 33:54 top 1452. Top 100 was 10:33, 13:54.

### Day 15
For part 1 I made a set and for each sensor added the coordinates it touches in that line and then took the siz eof the difference with the set of beacons in that line. For part 2 I started again with sets, but it was incredibly slow. My idea was to add every coordinate touching the border of each diamond coming from a sensor and then check each coordinate with all other sensors. However that set constantly had millions of elements so it was very slow and took over half an hour to give an incorrect answer. I had to leave Aberystwyth that day and prepare some stuff so I gave up for the moment and went to do something else. In the meantime I thought of using a quadtree, but that would have actually been just as slow as this. In the end I decided to go line by line joining the segments that each sensor sees and stop when you find a line that isn't entirely covered. I used an n^2 algorithm for joining segments, but later Maxim told me it can be done in n log n by sorting them first, so that will be in the faster version. It's possible to do this faster than going line by line. By checking the diagonals spanned by each diamond's side and joining the segments given by the other sensors it can be done in n^2 log n with n being the number of sensors. Sorting the sensors in both diagonals brings it to n^2 and sorting their potential segments since the beginning I think can bring it down to n log n average with worst case being n^2. I got star 1 25:10 top 1043, star 2 6:14:30 top 8410. Top 100 was 10:40, 27:14.

### Day 16
This one is the bane of my existence. I've solved 4 dynamic programming problems, the first one was the knapsack problem in algorithms and data structures in year 2 (which I didn't actually solve, just implemented) and three random problems from codeforces to at least be able to do basic dp. In part 1 I made a graph with edges going from one valve to the ones it leads to. Then went through the nodes pushing to the next nodes the max if you release and the max if you don't. Then stop when no nodes change anymore and search all of them for the max value. For part 2 I made a graph where each node is a possible position of me and the elephant and the edges are towards all the next possible positions. I got the small input right but not the actual input. I think I know where the error is, but I haven't fixed it yet because it's a massive pain. Also I didn't even do star 1 at the beginning because I had to leave soon to catch a flight. I got star 1 over 24h top 14831, star 2 still nothing. I definitely need to get more comfortable with dynamic programming.

### Day 17
Part 1 is just a simulation. Part 2 took me a moment to think about what to do but I got it. I took some point where the first piece is dropped at the same left/right move index for the second time, meaning this was probably a loop from here (and it happened to be). Then skip that loop until the end and simulate the last loop that is left unfinished. It didn't work so I also checked that the loop started and ended witht he first 15 lines being the same, but that didn't work either. The problem was just that I started the last loop on left/right move index 0 instead of the one at the ends of the loops so I think I didn't need to do that. I got star 1 01:03:24 top 1491, star 2 03:04:26 top 1881.

### Day 18
I noticed that the input never goes past 25 in any coordinate so I made a 3d list with length 25 in every dimension and set every entry to False. Then for each cube made the entry corresponding its coordinate True and took the number of sides to be the number of cubes * 6. Then I went through every coordinate and checked the coordinates 1 more in each dimension. If both are a cube then remove 2 from sides. No need to check 1 less in each dimension because checking 1 more also checks 1 less of any of the potential cubes that come after. For part 2 I started in the coordinates 0,0,0 (and 25,25,25 just in case) knowing those are outside of the cubes and for each cube of air touching those, set them to -1 and check them later. When it's done then check the coordinates that are still set to False, check all the coordinates touching those and remove 1 side for each one. I got star 1 16:25 top 2200, star 2 33:05 top 1036. Top 100 was 2:55, 12:29.

### Day 19
I got stuck and had to unspoiler a discord message saying branch and bound works to even start doing anything. At first I thought it was another dynamic programming problem but I couldn't think of anything. I take a best of 0, then for each branch I check an upper bound with a quick heuristic and if it's lower than the current best then remove the branch. When I woke up I was stuck so I just went to sleep and did it later so I got 10:30:31 top 5007, 10:54:15 top 4150. Top 100 was 48:27, 57:45.

### Day 20
This was really easy, just a bit tricky in that going down to position 0 brings you to the end and going up to the end brings you to 0. Just use the modulus to get the new position. I got 32:48 top 663, 00:43:42 top 707. Top 100 was 15:41, 21:14.

### Day 21
I overslept again. In the first part I parsed all the monkeys so that they hold either numbers or operations. Then for each monkey I solve its operation by using the two monkeys it references. If one of the other monkeys also has an operation then solve that etc recursively. By the end all operations are solved. For part 2 I got a path from root to humn and calculated the number I needed in each step. I got 03:58:49 top 8156, 04:30:53 top 5840. Top 100 was 4:28, 16:15.

### Day 22
Part 1 was an easy simulation. Part 2 was a massive pain because I had to hardcode where all the edges go and the change of direction and had a sneaky bug that I couldn't find until I printed the entire jungle to a file and went step by step to see where it failed. I got 01:03:58 top 1664, 13:33:37 top 4764. Top 100 was 19:04, 01:14:31.

### Day 23
At this point I stopped waking up early because I can't get top 1 but also I'll stay at top 3 even if I'm missing a star. This one is just a simulation. First run it 10 steps then run it until nothing moves. I got 05:28:16 top 5635, 05:32:43 top 5400. Top 100 was 21:46, 24:43.

### Day 24
Another simulation without anything hard. I got 05:50:01 top 4423, 06:08:57 top 4273.

### Day 25
This one caught me by surprise. Part 1 was just making a function to transform from decimal to snafu and snafu to decimal, but part 2 was getting all previous stars so I couldn't get it because I don't have day 16 part 2 yet. This means Georgi can take top 2 from me when he decides to finish after he stopped in day 22 part 2, so I need to do finish day 16. I got 06:19:51, top 7050. Top 100 was 7:54, 08:30.
