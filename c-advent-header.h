void readLines(char *fileName, char ***linesArray, int *size) {
    FILE *fp;
    fp = fopen(fileName, "r");
    *size = 0;
    int linesAllocated = 10;
    *linesArray = (char **)malloc(sizeof(char *) * linesAllocated);
    while (1) {
        if (*size == linesAllocated) {
            linesAllocated *= 2;
            *linesArray = (char **)realloc(*linesArray, sizeof(char *) * linesAllocated);
        }
        char line[999];
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

unsigned long long start, end;
void startBenchmark() {
    start = getMicros();
}

void endBenchmark(int iterations, int linesNum, char *text) {
    end = getMicros();
    printf("Microseconds %s: %f\n", text, (float)(end - start) / iterations);
    printf("Microseconds per line: %f\n\n", (float)(end - start) / iterations / linesNum);
}
