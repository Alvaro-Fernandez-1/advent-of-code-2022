#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "c-advent-header.h"

int getCharValue(char c) {
    if (c >= 'a') {
        return c-96;
    }
    else {
        return c-64+26;
    }
}

int charInString(char c, char *string) {
    int len = strlen(string);
    for (int i=0; i<len; i++) {
        if (c == string[i]) {
            return 1;
        }
    }
    return 0;
}

int part1Slow(char **lines, int linesNum) {
    int total = 0;
    for (int i=0; i<linesNum; i++) {
        char *thisLine = lines[i];
        char common;
        
        int halfLen = strlen(thisLine)/2;
        char *half2 = thisLine + halfLen;
        for (int j=0; j<halfLen; j++) {
            if (charInString(thisLine[j], half2)) {
                common = thisLine[j];
            }
        }
        
        total += getCharValue(common);
    }
    return total;
}

int part2Slow(char **lines, int linesNum) {
    int total = 0;
    for (int i=0; i<linesNum/3; i++) {
        char *line1 = lines[3*i];
        char *line2 = lines[3*i+1];
        char *line3 = lines[3*i+2];
        char common;
        
        int len1 = strlen(line1);
        for (int j=0; j<len1; j++) {
            if (charInString(line1[j], line2) && charInString(line1[j], line3)) {
                common = line1[j];
            }
        }
        
        total += getCharValue(common);
    }
    return total;
}

void initSet(char *set) {
    for (int i=65; i<=90; i++) {
        set[i] = 0;
    }
    for (int i=97; i<=122; i++) {
        set[i] = 0;
    }
}

char oneIntersectionTwo(char *set1, char *set2) {
    for (int i=65; i<=90; i++) {
        if (set1[i] && set2[i]) {
            return i;
        }
    }
    for (int i=97; i<=122; i++) {
        if (set1[i] && set2[i]) {
            return i;
        }
    }
}

char oneIntersectionThree(char *set1, char *set2, char *set3) {
    for (int i=65; i<=90; i++) {
        if (set1[i] && set2[i] && set3[i]) {
            return i;
        }
    }
    for (int i=97; i<=122; i++) {
        if (set1[i] && set2[i] && set3[i]) {
            return i;
        }
    }
}

int part1Fast(char **lines, int linesNum) {
    // only useful for this problem in particular
    char set1[150];
    char set2[150];
    
    int total = 0;
    for (int i=0; i<linesNum; i++) {
        initSet(set1);
        initSet(set2);
        
        char *thisLine = lines[i];

        int halfLen = strlen(thisLine)/2;
        int len = halfLen*2;
        for (int j=0; j<halfLen; j++) {
            set1[thisLine[j]] = 1;
        }
        for (int j=halfLen; j<len; j++) {
            set2[thisLine[j]] = 1;
        }
        
        total += getCharValue(oneIntersectionTwo(set1, set2));
    }
    return total;
}

int part2Fast(char **lines, int linesNum) {
    // only useful for this problem in particular
    char set1[150];
    char set2[150];
    char set3[150];
    
    int total = 0;
    for (int i=0; i<linesNum/3; i++) {
        initSet(set1);
        initSet(set2);
        initSet(set3);
        
        char *line1 = lines[3*i];
        char *line2 = lines[3*i+1];
        char *line3 = lines[3*i+2];

        int len1 = strlen(line1);
        int len2 = strlen(line2);
        int len3 = strlen(line3);
        for (int j=0; j<len1; j++) {
            set1[line1[j]] = 1;
        }
        for (int j=0; j<len2; j++) {
            set2[line2[j]] = 1;
        }
        for (int j=0; j<len3; j++) {
            set3[line3[j]] = 1;
        }
        
        total += getCharValue(oneIntersectionThree(set1, set2, set3));
    }
    return total;
}

int main() {
    char **lines;
    int linesNum;
    readLines("Day3-input.txt", &lines, &linesNum);
    int iterations = 100000;
    
    //use volatile because apparently that prevents the compiler from optimizing the loop away
    startBenchmark();
    volatile int pt1s;
    for (int i=0; i<iterations; i++) {
        pt1s = part1Slow(lines, linesNum);
    }
    endBenchmark(iterations, linesNum, "part 1 slow");
    
    startBenchmark();
    volatile int pt2s;
    for (int i=0; i<iterations; i++) {
        pt2s = part2Slow(lines, linesNum);
    }
    endBenchmark(iterations, linesNum, "part 2 slow");
    
    startBenchmark();
    volatile int pt1f;
    for (int i=0; i<iterations; i++) {
        pt1f = part1Fast(lines, linesNum);
    }
    endBenchmark(iterations, linesNum, "part 1 fast");
    
    startBenchmark();
    volatile int pt2f;
    for (int i=0; i<iterations; i++) {
        pt2f = part2Fast(lines, linesNum);
    }
    endBenchmark(iterations, linesNum, "part 2 fast");
    
    printf("\n");
    printf("Star 1: %d\n", pt1s);
    printf("Star 2: %d\n", pt2s);
    printf("Star 1: %d\n", pt1f);
    printf("Star 2: %d\n", pt2f);
}
