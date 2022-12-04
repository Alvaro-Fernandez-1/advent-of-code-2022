#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "c-advent-header.h"

void parseInts(char *line, int *nums) {
    char *thisLinePtrCopy = line;
    int len = strlen(line);
    int nextNum = 0;
    for (int j=0; j<len+1; j++) {
        // set - and , to '\0' so atoi can read that int and then reset that character to not mess the lines
        if (line[j] == '-' || line[j] == ',' || line[j] == 0) {
            char temp = line[j];
            line[j] = 0;
            nums[nextNum] = atoi(thisLinePtrCopy);
            thisLinePtrCopy = line + j + 1;
            nextNum++;
            line[j] = temp;
        }
    }
}

int checkContains(int min1, int max1, int min2, int max2) {
    if (min1 >= min2 && max1 <= max2) {
        return 1;
    }
    if (min1 <= min2 && max1 >= max2) {
        return 1;
    }
    return 0;
}

int checkOverlaps(int min1, int max1, int min2, int max2) {
    if (min1 >= min2 && min1 <= max2) {
        return 1;
    }
    if (min2 >= min1 && min2 <= max1) {
        return 1;
    }
    return 0;
}

int part1(char **lines, int linesNum) {
    int total = 0;
    int nums[4];
    
    for (int i=0; i<linesNum; i++) {
        parseInts(lines[i], nums);
        if (checkContains(nums[0], nums[1], nums[2], nums[3])) {
            total++;
        }
    }
    return total;
}

int part2(char **lines, int linesNum) {
    int total = 0;
    int nums[4];
    
    for (int i=0; i<linesNum; i++) {
        parseInts(lines[i], nums);
        if (checkOverlaps(nums[0], nums[1], nums[2], nums[3])) {
            total++;
        }
    }
    return total;
}

int main() {
    char **lines;
    int linesNum;
    readLines("Day4-input.txt", &lines, &linesNum);
    int iterations = 100000;
    
    //use volatile because apparently that prevents the compiler from optimizing the loop away
    startBenchmark();
    volatile int pt1;
    for (int i=0; i<iterations; i++) {
        pt1 = part1(lines, linesNum);
    }
    endBenchmark(iterations, linesNum, "part 1");
    
    startBenchmark();
    volatile int pt2;
    for (int i=0; i<iterations; i++) {
        pt2 = part2(lines, linesNum);
    }
    endBenchmark(iterations, linesNum, "part 2");
    
    printf("\n");
    printf("Star 1: %d\n", pt1);
    printf("Star 2: %d\n", pt2);
}
