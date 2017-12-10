//
//  main.m
//  adventofcode
//
//  Created by Guillaume Borios on 12/4/17.
//  Copyright © 2017 Apple. All rights reserved.
//

#import <Foundation/Foundation.h>

static char * dataForDay(int day, int * length)
{
    if (day > 25) {
        return NULL;
    }
    char *buffer = NULL;
    const char * basePath = "/Users/gyom/adventofcode/";
    char * path = malloc(strlen(basePath) + 1 + 2 + 4 + 1);
    sprintf(path, "%s/%d.txt", basePath, day);
    FILE * fd = fopen(path, "r");
    if (fd) {
        fseek(fd, 0, SEEK_END);
        long size = ftell(fd);
        *length = (int)size;
        rewind(fd);
        buffer = malloc(size + 1);
        fread(buffer, size, 1, fd);
        fclose(fd);
        buffer[size] = 0;
    }
    free(path);
    
    return buffer;
}

static int readValue(char * input, int * i)
{
    int v = 0;
    int j = *i;
    char x = input[j++];
    BOOL neg = NO;
    if (x == '-') {
        neg = YES;
        x = input[j++];
    }
    while (x >= '0' && x <= '9') {
        v *= 10;
        v += x - '0';
        x = input[j++];
    }
    *i = j-1;
    return neg ? -v : v;
}

static int* readLine(char * input, int isize, int * i, int * size, BOOL full)
{
    int strl = 0;
    int j = *i;
    if (j+strl >= isize) {
        return NULL;
    }
    int valueCount = 0;
    while (j+strl < isize) {
        int value = input[j+strl];
        strl++;
        if (value != 10 || full) {
            if ((value < '0' || value > '9') && value != '-') {
                valueCount++;
            }
        } else if (!full) {
            valueCount++;
            break;
        }
    }
    if (full) {
        valueCount++;
    }
    int * output = malloc(sizeof(int)*valueCount);
    for (int k = 0; k < valueCount; k++) {
        output[k] = readValue(input, &j);
        j++;
    }
    *i += strl;
    *size = valueCount;
    return output;
}

unsigned long day1(BOOL part2) {
    int l = 0;
    const char * input = dataForDay(1, &l);
    unsigned long output = 0;
    for (int i = 0; i < l; i++) {
        unsigned long v = input[i] - '0';
        int offset = part2 ? l/2 : 1;
        unsigned long w = input[(i+offset) % l] - '0';
        if (v == w) {
            output += v;
        }
    }
    return output;
}

unsigned long day2(BOOL part2) {
    int l = 0;
    char * input = dataForDay(2, &l);
    int i = 0;
    unsigned long output = 0;

    if (!part2) {
        int count;
        int * line;
        while ((line = readLine(input, l, &i, &count, NO)) != NULL) {
            int x = line[0];
            int min = x;
            int max = x;
            for (int j = 1; j < count; j++) {
                x = line[j];
                if (x < min) {
                    min = x;
                } else if (x > max) {
                    max = x;
                }
            }
            output += max - min;
            free(line);
        }
    } else {
        int count;
        int * line;
        while ((line = readLine(input, l, &i, &count, NO)) != NULL) {
            bool done = false;
            for (int j = 0; j < count && !done; j++) {
                int lineJ = line[j];
                for (int k = 0; k < count && !done; k++) {
                    if (j != k) {
                        int lineK = line[k];
                        if ((lineK % lineJ) == 0) {
                            output += lineK / lineJ;
                            done = true;
                        }
                    }
                }
            }
            free(line);
        }
    }
    free(input);
    return output;
}

void locInSpiral(int v, int *x, int *y)
{
    if (v <= 1) {
        *x = 0;
        *y = 0;
    } else {
        int r = 1;
        int max = 1;
        do {
            int rc = 4*r*2;
            if (max+rc < v) {
                max += rc;
                r++;
            } else break;
        } while (true);
        v -= max;
        int rc = r*2;
        if (v <= rc) {
            *x = r;
            *y = v-r;
        } else if (v <= 2*rc) {
            *x = r-(v-rc);
            *y = r;
        } else if (v <= 3*rc) {
            *x = -r;
            *y = r-(v-2*rc);
        } else {
            *x = (v-3*rc)-r;
            *y = -r;
        }
    }
}

int indexInSpiral(int x, int y)
{
    int i = 1;
    int r = abs(x);
    if (r < abs(y)) r = abs(y);
    if (x != 0 || y != 0) {
        for (int j = 1; j < r; j++) {
            i += 4*j*2;
        }
        if (y == -r) {
            i += 3*2*r + r + x;
        } else if (x == -r) {
            i += 2*2*r + r - y;
        } else if (y == r) {
            i += 1*2*r + r - x;
        } else {
            i += 0*2*r + r + y;
        }
    }
    return i;
}

static int spiralValueIfDefined(int * spiral, int spiralSize, int x, int y)
{
    int index = indexInSpiral(x, y);
    if (index <= spiralSize && index > 0) return spiral[index-1];
    else return 0;
}

unsigned long day3(BOOL part2) {
    int l = 0;
    char * input = dataForDay(3, &l);
    unsigned long output = 0;
    if (input) {
        int i = 0;
        int v = readValue(input, &i);
        free(input);
        if (part2) {
            int spiralCapacity = 256*256;
            int * spiral = malloc(spiralCapacity);
            spiral[0] = 1;
            int spiralSize = 1;
            int newValue;
            do {
                int x,y;
                locInSpiral(spiralSize+1, &x, &y);
                newValue = 0;
                newValue += spiralValueIfDefined(spiral, spiralSize, x-1, y-1);
                newValue += spiralValueIfDefined(spiral, spiralSize, x, y-1);
                newValue += spiralValueIfDefined(spiral, spiralSize, x+1, y-1);
                newValue += spiralValueIfDefined(spiral, spiralSize, x-1, y);
                newValue += spiralValueIfDefined(spiral, spiralSize, x+1, y);
                newValue += spiralValueIfDefined(spiral, spiralSize, x-1, y+1);
                newValue += spiralValueIfDefined(spiral, spiralSize, x, y+1);
                newValue += spiralValueIfDefined(spiral, spiralSize, x+1, y+1);
                if (spiralSize+1 > spiralCapacity) {
                    spiralCapacity += 256*256;
                    spiral = realloc(spiral, spiralCapacity);
                }
                spiral[spiralSize] = newValue;
                spiralSize++;
            } while (newValue < v);
            output = newValue;
            free(spiral);
        } else {
            int x, y;
            locInSpiral(v, &x, &y);
            output = abs(x)+abs(y);
//            fprintf(stderr,"v=%d x=%d y=%d\n", (int)output, x, y);
        }
    }
    return output;
}

NSString * anagramNormalize(NSString * str)
{
    NSUInteger l = [str lengthOfBytesUsingEncoding:NSASCIIStringEncoding];
    char * buf = malloc(l+1);
    [str getCString:buf maxLength:l+1 encoding:NSASCIIStringEncoding];
    qsort_b(buf, l, 1, ^int(const void * b, const void * a) {
        return *((char *)b) - *((char *)a);
    });
    NSString * nor = [[NSString alloc] initWithBytesNoCopy:buf length:l encoding:NSASCIIStringEncoding freeWhenDone:YES];
    return nor;
}

BOOL passphraseWordMatch(BOOL includesAnagrams, NSString * word, NSString * testedword)
{
    if (includesAnagrams) {
        word = anagramNormalize(word);
        testedword = anagramNormalize(testedword);
    }
    return [word isEqualToString:testedword];
}

unsigned long day4(BOOL part2) {
    int l = 0;
    char * input = dataForDay(4, &l);
    NSString * str = [NSString stringWithUTF8String:input];
    NSArray * phrases = [str componentsSeparatedByString:@"\n"];
    int count = 0;
    for (NSString * phrase in phrases) {
        NSArray * words = [phrase componentsSeparatedByString:@" "];
        NSString * dupe = nil;
        for (NSString * word in words) {
            int wcount = 0;
            for (NSString * testedword in words) {
                if (passphraseWordMatch(part2, word, testedword)) {
                    wcount++;
                    if (wcount > 1) {
                        dupe = word;
                        break;
                    }
                }
            }
            if (dupe) {
                break;
            }
        }
        if (dupe == nil && words.count > 1) {
            count++;
        }
    }
    return count;
}

unsigned long day5(BOOL part2) {
    int l = 0;
    char * input = dataForDay(5, &l);
    int i = 0;
    unsigned long output = 0;
    int count;
    int * line = readLine(input, l, &i, &count, YES);
    if (line == NULL) return 0;
    
    int position = 0;
    int steps = 0;
    while (position >= 0 && position < count) {
        int offset = line[position];
        if (part2 && offset >= 3) {
            line[position] = offset - 1;
        } else {
            line[position] = offset + 1;
        }
        position += offset;
        steps++;
    }
    free(line);
    output = steps;
    free(input);
    return output;
}

static void banksAddValue(int index, char value, NSUInteger *banks)
{
    banks[index/8] += ((NSUInteger)value) << (((index/8)*8+7-index)*8);
}

void day6(void) {
    int l = 0;
    char * input = dataForDay(6, &l);
    int i = 0;
    unsigned long output = 0;
    int count;
    int * line = readLine(input, l, &i, &count, NO);
    free(input);
    if (line == NULL || count > 16) return;
    
    NSUInteger banks[2] = {0,0};
    for (int j = 0; j < count; j++) {
        banksAddValue(j, (char)line[j], banks);
    }
    free(line);
    
#define banksAsObject [[NSData alloc] initWithBytes:banks length:sizeof(banks)]

    NSMutableDictionary * states = [[NSMutableDictionary alloc] init];
    do {
        [states setObject:@(output) forKey:banksAsObject];
        // Find the largest value index
        int max = 0;
        int index = 0;
        for (int j = 0; j < count; j++) {
            char v = (banks[j/8] >> (((j/8)*8+7-j)*8)) & 0xFF;
            if (v > max) {
                max = v;
                index = j;
            }
        }
        banks[index/8] &= ~(((NSUInteger)0xFF) << (((index/8)*8+7-index)*8));
        for (int j = 0; j < max; j++) {
            index = (index + 1) % count;
            banksAddValue(index, 1, banks);
        }
        output++;
    } while (states[banksAsObject] == nil);
    fprintf(stderr,"Answer 6A is %lu\n", output);
    fprintf(stderr,"Answer 6B is %lu\n", output - [states[banksAsObject] integerValue]);
}

@interface TowerLevel : NSObject
@property NSString * name;
@property NSInteger weight;
@property NSArray<NSString *> *childrenNames;
@property NSMutableArray<TowerLevel *> *children;
@property TowerLevel * parent;
- (NSInteger)towerWeight:(BOOL*)found;
@end

@implementation TowerLevel
- (NSInteger)towerWeight:(BOOL*)found
{
    NSInteger towerWeight = 0;
    NSInteger childrenCount = self.children.count;
    NSInteger weights[childrenCount];
    for (NSInteger i = 0; i < childrenCount; i++) {
        TowerLevel * level = self.children[i];
        NSInteger branchHeight = [level towerWeight:found];
        weights[i] = branchHeight;
        towerWeight += branchHeight;
    }
    if (!*found) {
        NSInteger refWeight = weights[0];
        if (childrenCount > 2) {
            if ((weights[0] == weights[1]) || (weights[0] == weights[2])) {
                // already done
            } else if (weights[1] == weights[2]) {
                refWeight = weights[1];
            } else {
                NSLog(@"Unexpected...");
            }
        }
        for (NSInteger i = 0; i < childrenCount; i++) {
            if (weights[i] != refWeight) {
                *found = YES;
                fprintf(stderr,"Answer 7B is %ld\n", weights[i] - refWeight);
//                NSLog(@"found %@ (parent is %@) - %ld", self.children[i].name, self.children[i].parent.name, weights[i] - refWeight);
            }
        }
    }
    towerWeight += self.weight;
    return towerWeight;
}

@end

void day7(void) {
    int l = 0;
    char * input = dataForDay(7, &l);
    NSString * inputString = [NSString stringWithUTF8String:input];
    NSArray * lines = [inputString componentsSeparatedByString:@"\n"];
    NSMutableArray <TowerLevel *> * allLevels = [NSMutableArray new];
    for (NSString * line in lines) {
        TowerLevel * level = [TowerLevel new];
        NSArray * workArray = [line componentsSeparatedByString:@" ("];
        if (workArray.count > 1) {
            level.name = workArray[0];
            workArray = [workArray[1] componentsSeparatedByString:@")"];
            level.weight = [workArray[0] integerValue];
            workArray = [workArray[1] componentsSeparatedByString:@"-> "];
            if (workArray.count > 1) {
                level.childrenNames = [workArray[1] componentsSeparatedByString:@", "];
            }
            [allLevels addObject:level];
        }
    }
    
    NSInteger levelCount = allLevels.count;
    for (NSInteger j = 0; j < levelCount; j++) {
        TowerLevel * level = allLevels[j];
        if (level.childrenNames.count > 0 && level.children == 0) {
            for (NSString * childName in level.childrenNames) {
                for (NSInteger i = 0; i < levelCount; i++) {
                    TowerLevel * foundLevel = allLevels[i];
                    if ([foundLevel.name isEqualToString:childName]) {
                        if (level.children == nil) {
                            level.children = [NSMutableArray new];
                        }
                        foundLevel.parent = level;
                        [level.children addObject:foundLevel];
                        break;
                    }
                }
            }
        }
    }
    TowerLevel * root = nil;
    for (TowerLevel * level in allLevels) {
        if (level.parent == nil) {
            root = level;
            fprintf(stderr,"Answer 7A is %s\n", level.name.UTF8String);
            break;
        }
    }
    BOOL found = NO;
    (void)[root towerWeight:&found];
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        fprintf(stderr,"Answer 1A is %lu\n", day1(false));
        fprintf(stderr,"Answer 1B is %lu\n", day1(true));
        fprintf(stderr,"Answer 2A is %lu\n", day2(false));
        fprintf(stderr,"Answer 2B is %lu\n", day2(true));
        fprintf(stderr,"Answer 3A is %lu\n", day3(false));
        fprintf(stderr,"Answer 3B is %lu\n", day3(true));
        fprintf(stderr,"Answer 4A is %lu\n", day4(false));
        fprintf(stderr,"Answer 4B is %lu\n", day4(true));
        fprintf(stderr,"Answer 5A is %lu\n", day5(false));
        fprintf(stderr,"Answer 5B is %lu\n", day5(true));
        day6();
        day7();
    }
    return 0;
}
