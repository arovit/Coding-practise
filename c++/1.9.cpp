#include<iostream>

int main(){

int start = 50;
int sum = 0;
while (start <= 100) {
    sum = sum + start;
    start ++;
}
std::cout << sum;
return 0;
}

