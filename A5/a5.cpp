#include<iostream>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<vector>
#include<typeinfo>
#include<chrono>

using namespace std::chrono;
using namespace std;
void print(std::vector <int> const &a) {
   cout << "The vector elements are : ";
   for(int i=0; i < a.size(); i++)
	 cout << a[i] << ' ';
	 cout<<endl;
}
void print_graph(int* board){
	cout<<endl<<"--------------------------------------------"<<endl;
	for (int i = 0; i < 8; ++i)
	{
		for (int j = 0; j < 8; ++j)
		{
			if (board[i * 8 + j] == -1)
			{
				cout.width(4);
				cout<<"_";
				cout.width(4);
			}
			if (board[i * 8 + j] == 0)
			{
				cout.width(4);
				cout<<"O";
				cout.width(4);
			}
			if (board[i * 8 + j] == 1)
			{
				cout.width(4);
				cout<<"X";
				cout.width(4);
			}
		}
		cout<<endl;
	}
}

void check_other(int* board , vector<int>& temp, int i, int player){
	int up, bot , left, right;
	int left_top, right_top, left_bot, right_bot;
	int base, aim;
	vector<int> new_temp;

	if (player == 0) {
		 base = 1;
		 aim = 0;
	}
	else{
		 base = 0;
		 aim = 1;
	}
	// check up
	up = i;
	while ((up-8) <= 63 && (up-8) >= 0){
		up = up - 8;
		if (up > 63 || up < 0 || board[up] == -1) {
			new_temp.clear();
			break;
		}
		if(board[up] == base){
			new_temp.push_back(up);
		}
		else if (board[up] == aim) {
			new_temp.push_back(up);
			temp.insert(temp.end(), new_temp.begin(), new_temp.end());
			new_temp.clear();
			break;
		}
		else{
			continue;
		}
	}
	// check down
	bot = i;
	while ((bot+8) <= 63 && (bot+8) >= 0){
		bot = bot + 8;
		if (bot > 63 || bot < 0 || board[bot] == -1) {
			new_temp.clear();
			break;
		}
		if(board[bot] == base){
			new_temp.push_back(bot);
		}
		else if (board[bot] == aim) {
			new_temp.push_back(bot);
			temp.insert(temp.end(), new_temp.begin(), new_temp.end());
			new_temp.clear();
			break;
		}
		else{
			continue;
		}
	}
	// check left
	left = i;
	int left_borde = (i / 8) * 8;
	while ((left-1) <= 63 && (left-1) >= 0 && left-1 >= left_borde){
		left = left - 1;
		if (left > 63 || left < 0 || left < left_borde || board[left] == -1) {
			new_temp.clear();
			break;
		}
		if(board[left] == base){
			new_temp.push_back(left);
		}
		else if (board[left] == aim) {
			new_temp.push_back(left);
			temp.insert(temp.end(), new_temp.begin(), new_temp.end());
			new_temp.clear();
			break;
		}
		else{
			continue;
		}
	}
	// check right
	right = i;
	int right_borde = (i / 8) * 8 + 7;
	while ((right+1) <= 63 && (right+1) >= 0 && right+1 <= right_borde){
		right = right + 1;
		if (right > 63 || right < 0 || right > right_borde || board[right] == -1) {
			new_temp.clear();
			break;
		}
		if(board[right] == base){
			new_temp.push_back(right);
		}
		else if (board[right] == aim) {
			new_temp.push_back(right);
			temp.insert(temp.end(), new_temp.begin(), new_temp.end());
			new_temp.clear();
			break;
		}
		else{
			continue;
		}
	}
	// check left_top
	left_top = i;
	left_borde = ((i-8) / 8) * 8;
	while ((left_top-9) <= 63 && (left_top-9) >= 0 && left_top-9 >= left_borde){
		left_borde = ((left_top-8) / 8) * 8;
		left_top = left_top - 9 ;
		if (left_top > 63 || left_top < 0 || left_top < left_borde || board[left_top] == -1) {
			new_temp.clear();
			break;
		}
		if(board[left_top] == base){
			new_temp.push_back(left_top);
		}
		else if (board[left_top] == aim) {
			new_temp.push_back(left_top);
			temp.insert(temp.end(), new_temp.begin(), new_temp.end());
			new_temp.clear();
			break;
		}
		else{
			continue;
		}
	}
	// check right_top
	right_top = i;
	right_borde = ((i-8) / 8) * 8 + 7;
	while ((right_top-7) <= 63 && (right_top-7) >= 0 && right_top-7 <= right_borde){
		right_borde = ((right_top-8) / 8) * 8 + 7;
		right_top = right_top - 7 ;
		if (right_top > 63 || right_top < 0 || right_top > right_borde || board[right_top] == -1) {
			new_temp.clear();
			break;
		}
		if(board[right_top] == base){
			new_temp.push_back(right_top);
		}
		else if (board[right_top] == aim) {
			new_temp.push_back(right_top);
			temp.insert(temp.end(), new_temp.begin(), new_temp.end());
			new_temp.clear();
			break;
		}
		else{
			continue;
		}
	}

	// check left_bot
	left_bot = i;
	left_borde = ((i+8) / 8) * 8;
	while ((left_bot+7) <= 63 && (left_bot+7) >= 0 && left_bot+7 >= left_borde){
		left_borde = ((left_bot+8) / 8) * 8;
		left_bot = left_bot + 7 ;
		if (left_bot > 63 || left_bot < 0 || left_bot < left_borde || board[left_bot] == -1) {
			new_temp.clear();
			break;
		}
		if(board[left_bot] == base){
			new_temp.push_back(left_bot);
		}
		else if (board[left_bot] == aim) {
			new_temp.push_back(left_bot);
			temp.insert(temp.end(), new_temp.begin(), new_temp.end());
			new_temp.clear();
			break;
		}
		else{
			continue;
		}
	}

	// check right_bot
	right_bot = i;
	right_borde = ((i+8) / 8) * 8 + 7;
	while ((right_bot+9) <= 63 && (right_bot+9) >= 0 && right_bot+9 <= right_borde){
		right_borde = ((right_bot+8) / 8) * 8 + 7;
		right_bot = right_bot + 9 ;
		if (right_bot > 63 || right_bot < 0 || right_bot > right_borde || board[right_bot] == -1) {
			new_temp.clear();
			break;
		}
		if(board[right_bot] == base){
			new_temp.push_back(right_bot);
		}
		else if (board[right_bot] == aim) {
			new_temp.push_back(right_bot);
			temp.insert(temp.end(), new_temp.begin(), new_temp.end());
			new_temp.clear();
			break;
		}
		else{
			continue;
		}
	}
}

int* available_index_black(int* board , vector<vector<int> >& result){
	vector<vector<int> > available;
	vector<int> res;
	int up, bot , left, right;
	int left_top, right_top, left_bot, right_bot;

	for (int i = 0; i < 64; ++i)
	{
		if (board[i] == 1)
		{
			vector<int> temp;
			//check up
			up = i - 8;
			if (up <= 63 && up >= 0 && board[up] == 0)
			{
				temp.push_back(up);
				up = up - 8;
				while(up <= 63 && up >= 0){
					if (board[up] == -1){
						temp.push_back(up);
						check_other(board , temp, up, 1);
						available.push_back(temp);
						temp.clear();
						break;
					}
					else if (board[up] == 1) {
						temp.clear();
						break;
					}
					else{
						up = up - 8;
					}
				}
			}
			//check bot
			bot = i + 8;
			if (bot <= 63 && bot >= 0 && board[bot] == 0)
			{
				temp.push_back(bot);
				bot = bot + 8;
				while(bot <= 63 && bot >= 0){
					if (board[bot] == -1){
						temp.push_back(bot);
						check_other(board , temp, bot, 1);
						available.push_back(temp);
						temp.clear();
						break;
					}
					else if (board[bot] == 1) {
						temp.clear();
						break;
					}
					else{
						temp.push_back(bot);
						bot = bot + 8;
					}

				}
			}
			//check left
			left = i - 1;
			int left_borde = (i / 8) * 8;
			if (left <= 63 && left >= 0 && board[left] == 0 && left >= left_borde)
			{
				temp.push_back(left);
				left = left - 1;
				while(left <= 63 && left >= 0 && left >= left_borde){
					if (board[left] == -1){
						temp.push_back(left);
						check_other(board , temp, left, 1);
						available.push_back(temp);
						temp.clear();
						break;
					}
					else if (board[left] == 1) {
						temp.clear();
						break;
					}
					else{
						temp.push_back(left);
						left = left - 1;
					}

				}
			}
			//check right
			right = i + 1;
			int right_borde = (i / 8) * 8 + 7;
			if (right <= 63 && right >= 0 && board[right] == 0 && right <= right_borde)
			{
				temp.push_back(right);
				right = right + 1;
				while(right <= 63 && right >= 0 && right <= right_borde){
					if (board[right] == -1){
						temp.push_back(right);
						check_other(board , temp, right, 1);
						available.push_back(temp);
						temp.clear();
						break;
					}
					else if (board[right] == 1) {
						temp.clear();
						break;
					}
					else{
						temp.push_back(right);
						right = right + 1;
					}

				}
			}
			// check left-top
			if (i > 7){
				left_top = i - 9;
				int left_borde = ((i-8) / 8) * 8;
				if (left_top <= 63 && left_top >= 0 && board[left_top] == 0 && left_top >= left_borde)
				{
					temp.push_back(left_top);
					while(left_top <= 63 && left_top >= 0 && left_top >= left_borde){
						if (board[left_top] == -1){
							temp.push_back(left_top);
							check_other(board , temp, left_top, 1);
							available.push_back(temp);
							temp.clear();
							break;
						}
						else if (board[left_top] == 1) {
							temp.clear();
							break;
						}
						else{
							temp.push_back(left_top);
							left_borde = ((left_top-8) / 8) * 8;
							left_top = left_top - 9;
						}

					}
				}
			}
			// check right-top
			if (i > 7){
				right_top = i - 7;
				int right_borde = ((i-8) / 8) * 8 + 7;
				if (right_top <= 63 && right_top >= 0 && board[right_top] == 0 && right_top <= right_borde)
				{
					temp.push_back(right_top);
					while(right_top <= 63 && right_top >= 0 && right_top <= right_borde){
						if (board[right_top] == -1){
							temp.push_back(right_top);
							check_other(board , temp, right_top, 1);
							available.push_back(temp);
							temp.clear();

							break;
						}
						else if (board[right_top] == 1) {
							temp.clear();
							break;
						}
						else{
							temp.push_back(right_top);
							right_borde = ((right_top-8) / 8) * 8 + 7;
							right_top = right_top - 7;
						}
					}
				}
			}

			// check left bottom
			if (i < 56){
				left_bot = i + 7;
				int left_borde = ((i+8) / 8) * 8;
				if (left_bot <= 63 && left_bot >= 0 && board[left_bot] == 0 && left_bot >= left_borde)
				{
					temp.push_back(left_bot);
					while(left_bot <= 63 && left_bot >= 0 && left_bot >= left_borde){
						if (board[left_bot] == -1){
							temp.push_back(left_bot);
							check_other(board , temp, left_bot, 1);
							available.push_back(temp);
							temp.clear();
							break;
						}
						else if (board[left_bot] == 1) {
							temp.clear();
							break;
						}
						else{
							temp.push_back(left_bot);
							left_borde = ((left_bot+8) / 8) * 8;
							left_bot = left_bot + 7;
						}
					}
				}
			}

			// check right bottom
			if (i < 56){
				right_bot = i + 9;
				int right_borde = ((i+8) / 8) * 8 + 7;
				if (right_bot <= 63 && right_bot >= 0 && board[right_bot] == 0 && right_bot <= right_borde)
				{
					temp.push_back(right_bot);
					while(right_bot <= 63 && right_bot >= 0 && right_bot <= right_borde){
						if (board[right_bot] == -1){
							temp.push_back(right_bot);
							check_other(board , temp, right_bot, 1);
							available.push_back(temp);
							temp.clear();
							break;
						}
						else if (board[right_bot] == 1) {
							temp.clear();
							break;
						}
						else{
							temp.push_back(right_bot);
							right_borde = ((right_bot+8) / 8) * 8 + 7;
							right_bot = right_bot + 9;
						}
					}
				}
			}

		}
	}
	for (int i = 0; i < available.size(); ++i)
	{
		int last_index = available[i].size() - 1;
		res.push_back(available[i][last_index]);
		result.push_back(available[i]);
	}

	int* ans = &res[0];
	return ans;
}

int* available_index_white(int* board , vector<vector<int> >& result){
	vector<vector<int> > available;
	vector<int> res;
	int up, bot , left, right;
	int left_top, right_top, left_bot, right_bot;
	int score;

	for (int i = 0; i < 64; ++i)
	{
		if (board[i] == 0)
		{
			vector<int> temp;
			//check up
			up = i - 8;
			if (up <= 63 && up >= 0 && board[up] == 1)
			{
				temp.push_back(up);
				up = up - 8;
				while(up <= 63 && up >= 0){
					if (board[up] == -1){
						temp.push_back(up);
						check_other(board , temp, up, 0);
						temp.push_back(temp.size());
						available.push_back(temp);
						temp.clear();
						break;
					}
					else if (board[up] == 0) {
						temp.clear();
						break;
					}
					else{
						temp.push_back(up);
						up = up - 8;
					}

				}
			}
			//check bot
			bot = i + 8;
			if (bot <= 63 && bot >= 0 && board[bot] == 1)
			{
				temp.push_back(bot);
				bot = bot + 8;
				while(bot <= 63 && bot >= 0){
					if (board[bot] == -1){
						temp.push_back(bot);
						check_other(board , temp, bot, 0);
						temp.push_back(temp.size());
						available.push_back(temp);
						temp.clear();
						break;
					}
					else if (board[bot] == 0) {
						temp.clear();
						break;
					}
					else{
						temp.push_back(bot);
						bot = bot + 8;
					}

				}
			}
			//check left
			left = i - 1;
			int left_borde = (i / 8) * 8;
			if (left <= 63 && left >= 0 && board[left] == 1 && left >= left_borde)
			{
				temp.push_back(left);
				left = left - 1;
				while(left <= 63 && left >= 0 && left >= left_borde){
					if (board[left] == -1){
						temp.push_back(left);
						check_other(board , temp, left, 0);
						temp.push_back(temp.size());
						available.push_back(temp);
						temp.clear();
						break;
					}
					else if (board[left] == 0) {
						temp.clear();
						break;
					}
					else{
						temp.push_back(left);
						left = left - 1;
					}

				}
			}
			//check right
			right = i + 1;
			int right_borde = (i / 8) * 8 + 7;
			if (right <= 63 && right >= 0 && board[right] == 1 && right <= right_borde)
			{
				temp.push_back(right);
				right = right + 1;
				while(right <= 63 && right >= 0 && right <= right_borde){
					if (board[right] == -1){
						temp.push_back(right);
						check_other(board , temp, right, 0);
						temp.push_back(temp.size());
						available.push_back(temp);
						temp.clear();
						break;
					}
					else if (board[right] == 0) {
						temp.clear();
						break;
					}
					else{
						temp.push_back(right);
						right = right + 1;
					}

				}
			}
			// check left-top
			if (i > 7){
				left_top = i - 9;
				int left_borde = ((i-8) / 8) * 8;
				if (left_top <= 63 && left_top >= 0 && board[left_top] == 1 && left_top >= left_borde)
				{
					temp.push_back(left_top);
					while(left_top <= 63 && left_top >= 0 && left_top >= left_borde){
						if (board[left_top] == -1){
							temp.push_back(left_top);
							check_other(board , temp, left_top, 0);
							temp.push_back(temp.size());
							available.push_back(temp);
							temp.clear();
							break;
						}
						else if (board[left_top] == 0) {
							temp.clear();
							break;
						}
						else{
							temp.push_back(left_top);
							left_borde = ((left_top-8) / 8) * 8;
							left_top = left_top - 9;
						}

					}
				}
			}
			// check right-top
			if (i > 7){
				right_top = i - 7;
				int right_borde = ((i-8) / 8) * 8 + 7;
				if (right_top <= 63 && right_top >= 0 && board[right_top] == 1 && right_top <= right_borde)
				{
					temp.push_back(right_top);
					while(right_top <= 63 && right_top >= 0 && right_top <= right_borde){
						if (board[right_top] == -1){
							temp.push_back(right_top);
							check_other(board , temp, right_top, 0);
							temp.push_back(temp.size());
							available.push_back(temp);
							temp.clear();

							break;
						}
						else if (board[right_top] == 0) {
							temp.clear();
							break;
						}
						else{
							temp.push_back(right_top);
							right_borde = ((right_top-8) / 8) * 8 + 7;
							right_top = right_top - 7;

						}
					}
				}
			}

			// check left bottom
			if (i < 56){
				left_bot = i + 7;
				int left_borde = ((i+8) / 8) * 8;
				if (left_bot <= 63 && left_bot >= 0 && board[left_bot] == 1 && left_bot >= left_borde)
				{
					temp.push_back(left_bot);
					while(left_bot <= 63 && left_bot >= 0 && left_bot >= left_borde){
						if (board[left_bot] == -1){
							temp.push_back(left_bot);
							check_other(board , temp, left_bot, 0);
							temp.push_back(temp.size());
							available.push_back(temp);
							temp.clear();
							break;
						}
						else if (board[left_bot] == 0) {
							temp.clear();
							break;
						}
						else{
							temp.push_back(left_bot);
							left_borde = ((left_bot+8) / 8) * 8;
							left_bot = left_bot + 7;
						}
					}
				}
			}

			// check right bottom
			if (i < 56){
				right_bot = i + 9;
				int right_borde = ((i+8) / 8) * 8 + 7;
				if (right_bot <= 63 && right_bot >= 0 && board[right_bot] == 1 && right_bot <= right_borde)
				{
					temp.push_back(right_bot);
					while(right_bot <= 63 && right_bot >= 0 && right_bot <= right_borde){
						if (board[right_bot] == -1){
							temp.push_back(right_bot);
							check_other(board , temp, right_bot, 0);
							temp.push_back(temp.size());
							available.push_back(temp);
							temp.clear();
							break;
						}
						else if (board[right_bot] == 0) {
							temp.clear();
							break;
						}
						else{
							temp.push_back(right_bot);
							right_borde = ((right_bot+8) / 8) * 8 + 7;
							right_bot = right_bot + 9;
						}
					}
				}
			}

		}
	}
	for (int i = 0; i < available.size(); ++i)
	{
		int last_index = available[i].size() - 2;
		res.push_back(available[i][last_index]);
		result.push_back(available[i]);
	}

	int* ans = &res[0];
	return ans;
}

int check_win(int* board){
	int black = 0;
	int white = 0;
	vector<vector<int> > arr1;
	vector<vector<int> > arr2;
	available_index_black(board,arr1);
	available_index_white(board,arr2);
	if( arr1.size()==0 || arr2.size()==0){
		for (int i = 0; i < 64; i++) {
			if (board[i] == 0) {
				white++;
			}
			else if (board[i] == 1) {
				black++;
			}
			else
				continue;
		}
		if (black>white){

			return 1;
		}
		else if (black<white){

			return 2;
		}
		else{
			return 3;
		}
	}
	return -1;
}
// 1("X") act as mcs
void monte_carlo_search_black_turn(int* board, vector<int>& mcs_index){
	vector<vector<int> > arr;
	int *originalboard = new int [64];
	int randomIndex = 0;
	available_index_black(board,arr);
	int score[arr.size()];
	vector<vector<int> > arr_temp;
	srand(time(0));
	for (int j = 0; j < arr.size(); j++) {
		for (int i = 0; i < 64; ++i)
		{
			originalboard[i] = board[i];
		}
		for (int i = 0; i < arr[j].size(); i++) {
			originalboard[arr[j][i]] = 1;
		}
		while(true) {
			//check win for black
			if (check_win(originalboard) == 1) {
				score[j]++;
				break;
			}
			//white move
			arr_temp.clear();
			available_index_white(originalboard,arr_temp);
			if (arr_temp.size() != 0) {
				randomIndex = rand() % arr_temp.size();

				for (int x = 0; x < arr_temp[randomIndex].size()-1; x++) {
					originalboard[arr_temp[randomIndex][x]] = 0;
				}
			}
			// print_graph(board);
			//check win for white
			if (check_win(originalboard)==2 || check_win(originalboard)==3) {
				break;
			}
			arr_temp.clear();
			//black move
			if (arr_temp.size() != 0){
				available_index_black(originalboard,arr_temp);
				randomIndex = rand() % arr_temp.size() ;

				for (int x = 0; x < arr_temp[randomIndex].size()-1; x++) {
					originalboard[arr_temp[randomIndex][x]] = 1;
				}
			}
			// print_graph(board);
		}
	}
	int max = 0;
	int black_index;
	for (int i = 0; i < arr.size(); ++i)
	{
		if (score[i] >= max)
		{
			max = score[i];
			black_index = i;
		}
		//cout << "all possible of black scores: " << score[i] << "and their index " << arr[i][0]<<endl;
	}
	if (max != 0)
	{
		//cout << "monte_carlo search choose: " << arr[black_index][0] << endl;;
		for (int i = 0; i < arr[black_index].size(); ++i)
		{
			mcs_index.push_back(arr[black_index][i]);
		}
	}

}

// 0 ("O") act as heuristic
void heuristic_white_turn(int* board , vector<int>& heuristic_index){
	vector<vector<int> > arr;
	available_index_white(board,arr);
	int max_score = 0;
	//cout << "heuristic have these options to choose: ";
	for (int i = 0; i < arr.size(); ++i)
	{
		int score_index = arr[i].size() - 1;
		//cout<<" "<<arr[i][score_index-1];
		if (arr[i][score_index] > max_score)
		{
			max_score = arr[i][score_index];
			heuristic_index = arr[i];
		}
	}
	cout << endl;

}


// 0 ("O") is white, 1 ("X") is black, -1 ("_") is blank
// 1 ("X") act as monte_carlo; 0 ("O") act as heuristic
int main()
{
	int round_number;
	int monte = 0;
	int heuristic = 0;
	int draw = 0;
	cout<<endl<<"number of times you want them to play: ";
  cin>>round_number;
	for (int i = 0; i < round_number; i++) {
		int init_board[] = {
												//0                    7
												-1,-1,-1,-1,-1,-1,-1,-1,
												-1,-1,-1,-1,-1,-1,-1,-1,
												-1,-1,-1,-1,-1,-1,-1,-1,
												-1,-1,-1, 0, 1,-1,-1,-1,
												-1,-1,-1, 1, 0,-1,-1,-1,
												-1,-1,-1,-1,-1,-1,-1,-1,
												-1,-1,-1,-1,-1,-1,-1,-1,
												-1,-1,-1,-1,-1,-1,-1,-1};
			print_graph(init_board);
		cout<<"round: "<<i<<endl;
	  while(check_win(init_board) == -1) {
			vector<int> mcs_index;
			monte_carlo_search_black_turn(init_board,mcs_index);
			if (mcs_index.size() > 0){
				cout << "monte_carlo_search_black_turn"<< '\n';
				for (int i = 0; i < mcs_index.size()-1; ++i)
				{
					init_board[mcs_index[i]] = 1;
				}
				print_graph(init_board);
				mcs_index.clear();

				if (check_win(init_board) != -1) {
					break;
				}
			}

			vector<int> heuristic_index;
			heuristic_white_turn(init_board,heuristic_index);
			if (heuristic_index.size() > 0){
				cout << "heuristic_white_turn"<< '\n';
				for (int i = 0; i < heuristic_index.size() - 1; ++i)
				{
					init_board[heuristic_index[i]] = 0;
				}
				//cout << "heuristic choose index: " << heuristic_index[heuristic_index.size() - 2] << endl;
				print_graph(init_board);
				heuristic_index.clear();
			}

	  }
		if (check_win(init_board) == 1) {
			cout << "monte_carlo_search win" << '\n';
			monte++;
		}
		else if (check_win(init_board) == 2) {
			cout << "heuristic win" << '\n';
			heuristic++;
		}
		else  {
			cout << " draw" << '\n';
			draw++;
		}

	}
  cout << "Monte wins: " << monte << '\n';
	cout << "Heuristic wins: " << heuristic << '\n';
	cout << "Draw: " << draw << '\n';
	return 0;
}
