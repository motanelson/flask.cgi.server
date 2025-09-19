#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    printf("Content-type:plain-text\r\n\r\n");
    printf("<html><head><title>hello</title></head><body bgcolor= Yellow><h1>");
    printf("hello world ...<br>");
    printf("</h1></body></html>\r\n");
    return 0;
}