#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

void readLines(char *fileName, char ***linesArray, int *size) {
    FILE *fp;
    fp = fopen(fileName, "r");
    *size = 0;
    *linesArray = (char **)malloc(sizeof(char *) * 1000);
    while (1) {
        char line[100];
        (*linesArray)[*size] = (char *)malloc(sizeof(char) * 100);
        if (!fgets(line, 999, fp)) {
            return;
        }
        // don't want newline included in each line
        if (line[strlen(line)-1] == '\n') {
            line[strlen(line)-1] = '\0';
        }
        
        strcpy((*linesArray)[*size], line);
        *size += 1;
    }
    fclose(fp);
}

//timing stuff
struct timespec tms;
unsigned long long getMicros() {
    clock_gettime(CLOCK_MONOTONIC_RAW, &tms);
    return tms.tv_sec * 1000000 + tms.tv_nsec/1000;
}

int getCharValue(char c) {
    if (c >= 'a') {
        return c-96;
    }
    else {
        return c-64+26;
    }
}

int charInString(char c, char *string) {
    for (int i=0; i<(strlen(string)); i++) {
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
        
        char *half2 = thisLine + strlen(thisLine)/2;
        for (int j=0; j<strlen(thisLine)/2; j++) {
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
        
        for (int j=0; j<strlen(line1); j++) {
            if (charInString(line1[j], line2) && charInString(line1[j], line3)) {
                common = line1[j];
            }
        }
        
        total += getCharValue(common);
    }
    return total;
}

void initSet(int *set) {
    for (int i=65; i<=90; i++) {
        set[i] = 0;
    }
    for (int i=97; i<=122; i++) {
        set[i] = 0;
    }
}

char oneIntersectionTwo(int *set1, int *set2) {
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

char oneIntersectionThree(int *set1, int *set2, int *set3) {
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
    int set1[150];
    int set2[150];
    
    int total = 0;
    for (int i=0; i<linesNum; i++) {
        initSet(set1);
        initSet(set2);
        
        char *thisLine = lines[i];

        for (int j=0; j<strlen(thisLine)/2; j++) {
            set1[thisLine[j]] = 1;
        }
        for (int j=strlen(thisLine)/2; j<strlen(thisLine); j++) {
            set2[thisLine[j]] = 1;
        }
        
        total += getCharValue(oneIntersectionTwo(set1, set2));
    }
    return total;
}

int part2Fast(char **lines, int linesNum) {
    // only useful for this problem in particular
    int set1[150];
    int set2[150];
    int set3[150];
    
    int total = 0;
    for (int i=0; i<linesNum/3; i++) {
        initSet(set1);
        initSet(set2);
        initSet(set3);
        
        char *line1 = lines[3*i];
        char *line2 = lines[3*i+1];
        char *line3 = lines[3*i+2];

        for (int j=0; j<strlen(line1); j++) {
            set1[line1[j]] = 1;
        }
        for (int j=0; j<strlen(line2); j++) {
            set2[line2[j]] = 1;
        }
        for (int j=0; j<strlen(line3); j++) {
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
    unsigned long long start, end;
    
    start = getMicros();
    int pt1s = part1Slow(lines, linesNum);
    end = getMicros();
    printf("Microseconds part 1 slow: %f\n", (float)(end - start));
    printf("Microseconds per line: %f\n\n", (float)(end - start) / linesNum);
    
    start = getMicros();
    int pt2s = part2Slow(lines, linesNum);
    end = getMicros();
    printf("Microseconds part 2 slow: %f\n", (float)(end - start));
    printf("Microseconds per line: %f\n\n", (float)(end - start) / linesNum);
    
    start = getMicros();
    int pt1f = part1Fast(lines, linesNum);
    end = getMicros();
    printf("Microseconds part 1 fast: %f\n", (float)(end - start));
    printf("Microseconds per line: %f\n\n", (float)(end - start) / linesNum);
    
    start = getMicros();
    int pt2f = part2Fast(lines, linesNum);
    end = getMicros();
    printf("Microseconds part 2 fast: %f\n", (float)(end - start));
    printf("Microseconds per line: %f\n\n", (float)(end - start) / linesNum);

    printf("\n");
    printf("Star 1: %d\n", pt1s);
    printf("Star 2: %d\n", pt2s);
    printf("Star 1: %d\n", pt1f);
    printf("Star 2: %d\n", pt2f);
}
