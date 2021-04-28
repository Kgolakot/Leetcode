#include<iostream>

int palindrome(int n)
{
	if(n<0)
		return 0;
	long my_num = 0;
	while(n>0)
	{
		my_num = my_num*10 + n%10;
		n = n/10;
	}
	return my_num;
}

int main()
{
int number = 0;
std::cout<<"Please enter the number you would like to check:"<<std::endl;
std::cin>>number;

if(number == palindrome(number))
	std::cout<<"Its a palindrome number";
else
	std::cout<<"Its not a palindrome number";
return 0;
}
