#include <stdio.h>

int main(int argc, char const *argv[])
{
    int i;
    for (int j = i; j <= 0; j++)
        printf("此时运行第一个循环：j = %d\n", j);

    for (int j = i; j > 0; j--)
        printf("此时运行第二个循环：j = %d\n", j);

    return 0;
}
