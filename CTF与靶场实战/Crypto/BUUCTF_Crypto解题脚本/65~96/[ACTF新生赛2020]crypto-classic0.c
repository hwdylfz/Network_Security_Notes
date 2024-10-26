#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    char enc[]="Ygvdmq[lYate[elghqvakl}";
    for (int i=0;i<25;i++)
    {
        enc[i]^=0x7;
        enc[i]+=3;
        printf("%c",enc[i]);
    }
    return 0;
}