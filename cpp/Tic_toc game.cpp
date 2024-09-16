//Tic-toc-toe game
#include<bits/stdc++.h>
using namespace std;
string player1,player2,player;
char m[7][7];
set<int>s;
void draw()
{
	cout<<"INTERFACE:"<<endl;
	cout<<"           - - - "<<endl;
	cout<<"          |1|2|3|"<<endl;
	cout<<"           - - - "<<endl;
	cout<<"          |4|5|6|"<<endl;
	cout<<"           - - - "<<endl;
	cout<<"          |7|8|9|"<<endl;
	cout<<"           - - - "<<endl;
}
int validaten(int x)
{
	if(x>=1 && x<=9) return x;
	cout<<"Please Enter a valid Number in between[1-9]\n";
	cin>>x;
	validaten(x);
}
void show()
{
	cout<<"game till now\n";
	for(int i=0;i<7;i++)
	{
		for(int j=0;j<7;j++)
		{
			cout<<m[i][j];
		}
		cout<<endl;
	}
}
int invalid(int pos)
{
	show();
	draw();
	cout<<player<<", Please enter a valid position\n";
	cin>>pos;
	return pos;
}
void play(char c,int pos)
{	
    system("cls");
    if(s.find(pos)!=s.end())
    {
    	int pos=invalid(pos);
    	play(c,pos);
	}
	else
	{
		s.insert(pos);
		if(pos==1) m[1][1]=c;
	else if(pos==2)  m[1][3]=c;
	else if(pos==3)  m[1][5]=c;
	else if(pos==4)  m[3][1]=c;
	else if(pos==5) m[3][3]=c;
	else if(pos==6) m[3][5]=c;
	else if(pos==7) m[5][1]=c;
	else if(pos==8) m[5][3]=c;
	else if(pos==9) m[5][5]=c;
	}
}
char validatec(char c)
{
	if(c=='y' || c=='n' || c=='Y' || c=='N')
	return c;
	cout<<"Please Enter a valid character in between[y/n]\n";
	scanf("%c",&c);
	validatec(c);
}
char res(char c)
{
	/*for x */
	if(c=='X')
	{
		//for horizontal
	for(int i=1;i<6;i+=2)
	if(m[i][1]=='X' && m[i][3]=='X' && m[i][5]=='X') return 'X';
	//for vertical
	for(int i=1;i<6;i+=2)
	if(m[1][i]=='X' && m[3][i]=='X' && m[5][i]=='X') return 'X';
	//for diagonals
	if(m[1][1]=='X' && m[3][3]=='X' && m[5][5]=='X') return 'X';
	if(m[5][1]=='X' && m[3][3]=='X' && m[1][5]=='X') return 'X';
	}
	/*for y */
	else if(c=='O')
	{
		//for horizontal
	for(int i=1;i<6;i+=2)
	if(m[i][1]=='O' && m[i][3]=='o' && m[i][5]=='O') return 'O';
	//for vertical
	for(int i=1;i<6;i+=2)
	if(m[1][i]=='O' && m[3][i]=='O' && m[5][i]=='O') return 'O';
	//for diagonals
	if(m[1][1]=='O' && m[3][3]=='O' && m[5][5]=='O') return 'O';
	if(m[5][1]=='O' && m[3][3]=='O' && m[1][5]=='O') return 'O';
		}	
}
int main()
{
	cout<<"              WELCOME TO PLAY TIC-TOC-TOE\n\n";
	cout<<"player1 wanna start the game with the symbol 'X'\n";
	cout<<"Enter player 1 name\n";
	getline(cin,player1);
	cout<<"Enter player 2 name\n";
	getline(cin,player2);
	int flag=0,win=0,j=0;
		m[0][0]=' ';m[0][1]='-';m[0][2]=' ';m[0][3]='-';m[0][4]=' ';m[0][5]='-';m[0][6]=' ';
	m[2][0]=' ';m[2][1]='-';m[2][2]=' ';m[2][3]='-';m[2][4]=' ';m[2][5]='-';m[2][6]=' ';
	m[4][0]=' ';m[4][1]='-';m[4][2]=' ';m[4][3]='-';m[4][4]=' ';m[4][5]='-';m[4][6]=' ';
	m[6][0]=' ';m[6][1]='-';m[6][2]=' ';m[6][3]='-';m[6][4]=' ';m[6][5]='-';m[6][6]=' ';

	m[1][0]='|';m[1][1]=' ';m[1][2]='|';m[1][3]=' ';m[1][4]='|';m[1][5]=' ';m[1][6]='|';
	m[3][0]='|';m[3][1]=' ';m[3][2]='|';m[3][3]=' ';m[3][4]='|';m[3][5]=' ';m[3][6]='|';
	m[5][0]='|';m[5][1]=' ';m[5][2]='|';m[5][3]=' ';m[5][4]='|';m[5][5]=' ';m[5][6]='|';
	while(j<9)
	{
	     j++;
	     draw();
	     show();
		if(flag==0)
		{
			cout<<player1<<"(X), select a number you wanna place\n";
			player=player1;
			int x;
	        cin>>x;
			int n=validaten(x);
			play('X',n);
			if(res('X')=='X')
			{
				win=1;
				cout<<"That's Great!,"<<player1<<" won the game\n";
				break;
			}
			flag=1;
			continue;
		}
		cout<<player2<<"(O), select a number you wanna place\n";
		player=player2;
			int x;
	        cin>>x;
			int n=validaten(x);
			play('O',n);
			if(res('O')=='O')
			{
				win=1;
				cout<<"That's Great!,"<<player2<<" won the game\n";
				break;
			}
			flag=0;
	}
	if(win==0) cout<<"oops! game is drawn...\n";	
}
