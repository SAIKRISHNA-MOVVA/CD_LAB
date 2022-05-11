/*Aim: To develop a program to eliminate left recursion.
Algorithm:
1.Start the program. 
2.Initialize the arrays for taking input from the user. 
3.Prompt the user to input the no. of non-terminals having left recursion and no. of productions for these non-terminals. 
4.Prompt the user to input the production for non-terminals. 
5.Eliminate left recursion using the following rules: 
A->Aα|β
Then replace it by
A-> βA’ 
A’-> αA’
A’-> Ɛ
6.After eliminating the left recursion by applying these rules, display the productions without left recursion. 
Stop.
Code: 
*/
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
void main()
{
	char a[10],b[50][10]={""},d[50][10]={""},ch;
	int i,n,c[10]={0},j,k,t,n1;
	printf("\nEnter the left production(s) (NON TERMINALS) : ");
	scanf("%s",a);
	n=strlen(a);
	for(i=0;i<n;i++)
	{
		printf("\nEnter the number of productions for %c : ",a[i]);
		scanf("%d",&c[i]);
	}
	t=0;
	for(i=0;i<n;i++)
	{
		printf("\nEnter the right productions for %c",a[i]);
		k=t;
		for(j=0;j<c[i];j++)
		{
			printf("\n%c->",a[i]);
			do
			{
				scanf("%s",b[k]);
				k++;
			}while(k<j);
		}
		t=t+10;
	}
	t=0;
	for(i=0;i<n;i++)
	{
		if(a[i]==b[t][0])
		{
			n1=strlen(b[t]);
			for(k=1;k<n1;k++)
			{
				d[t][k-1]=b[t][k];
			}
		}
		t=t+10;
	}
	t=0;
	printf("\n\nThe resulting productions after eliminating Left Recursion are : \n");
	for(i=0;i<n;i++)
	{
		if(a[i]==b[t][0])
		{
			for(j=1;j<c[i];j++)
			{
				printf("\n%c -> %s%c'",a[i],b[t+j],a[i]);
			}
		}
		t=t+10;
	}
	t=0;
	for(i=0;i<n;i++)
	{
		if(a[i]==b[t][0])
			printf("\n%c' -> %s%c'|\u03B5",a[i],d[t],a[i]);
		else
			for(j=0;j<c[i];j++)
				printf("\n%c -> %s",a[i],b[t+j]);
		t=t+10;
	}
	getch();
}
