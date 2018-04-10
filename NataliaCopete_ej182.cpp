#include <iostream>

using std::cout;
using std::endl;


int main(){


float y;
float h;
float N;
float x;
float z;

h=0.1;
x=0;
y=1;
N=10/h;
z=0;


for(int i=0;i<N;i++){
z=-h*y+z;
y= h*z+y;
x=x+h;
cout<<x<<" "<<y<<" "<<z<<endl;

}



return 0;
}
