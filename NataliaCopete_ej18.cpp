#include <iostream>

using std::cout;
using std::endl;


int main(){


float y;
float h;
float N;
float x;

h=0.1;
x=0;
y=1;
N=3/h;


for(int i=0;i<N;i++){
y= -h*y+y;
x=x+h;
cout<<x<<" "<<y<<endl;

}



return 0;
}
