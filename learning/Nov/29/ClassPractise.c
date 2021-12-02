#include <stdio.h>
int main(){
    int n;
    printf("请输入一个数");
    scanf("%d",&n);
    int i = 0;
    while (i<10)
    {
        i += 1;
        if (i!=n){
            printf("%d",i);
        }
        if (i == n) {
            continue;
        }
        

    }
    return 0 ;
}