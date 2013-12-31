//Prints binary representation of number

#include<stdio.h>
void toBin(int n);

int main(void)
{
	int num;
	scanf("%d",&num);
	toBin(num);
}

void toBin(int n)
{
	if(n==1 || n==2)
		printf("%d\n",n%2);
	
	else
	{
		printf("%d",(n%2));
		toBin(n/2);
	}
}


