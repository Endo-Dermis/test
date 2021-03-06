#include <iostream>

using namespace std;

namespace get_output{
	void print(string text){
		cout << "First text: " << text << endl;
	}
}

namespace get_other_output{
	void print(string text){
		cout << "Other text: " << text << endl;
	}
}


int main(){
	get_output::print("Jason");
	get_other_output::print("Kyle");


	return 0;
}