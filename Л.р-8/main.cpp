#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

#define N 20

using namespace std;

void array91();
void get_nums(int size, int array[N]);
bool checkfiles(string in, string out);
void editNewSize(int*& arr, int n, string output, int K, int M);


void matrix40();
bool checkfile(string in);
void fillArray(string f_in, int**& arr, const int rows, const int cols);
void searchNumbers(int** arr, const int rows, const int columns, string f_out);

void sort21();
void insertionSort(float arr[N], int n, string in);

int main() {

	int choice = 0;

	while (choice != 4) {

		cout << "Choose the task! : "
			"\n1.Array#91"
			"\n2.Matrix#40"
			"\n3.Sort#21"
			"\n4.Exit" << endl;

		cin >> choice;

		switch (choice) {
		case 1: {
			array91();		//Task array91
			break;
		}
		case 2: {
			matrix40();		//Task matrix40
			break;
		}
		case 3: {
			sort21();		//Task sort21
			break;
		}
		case 4: {
			cout << "Program is end!";
			break;
		}
		default: {
			cout << "Wrong one, try again";
		}
		}
	}
}

//Task Array91

void array91() {

	int n = 0, startPos = 0, size = 0;
	int mas[N];

	get_nums(size, mas);
}


void get_nums(int size, int array[N]) {

	string filename_in = "array_in_91.txt";
	string filename_out = "array_out_91.txt";

	int startPos = 0;

	ifstream f;

	if (checkfiles(filename_in, filename_out)) {

		f.open(filename_in);

		string lenght;

		getline(f, lenght);
		int size = stoi(lenght);

		int* arr = new int(size);

		getline(f, lenght);

		int K = stoi(lenght);

		getline(f, lenght);

		int L = stoi(lenght);

		cout << "K = " << K << "\n L = " << L;

		if (K > L) {
			cout << "K cannot be > than L";
			exit(0);
		}

		string tempor[N];
		getline(f, tempor[0]);

		for (int i = 0; i < size; i++) {
			int spacePos = tempor[0].find(' ', startPos);
			std::string numStr = tempor[0].substr(startPos, spacePos - startPos);
			arr[i] = stoi(numStr);
			startPos = spacePos + 1;
		}

		for (int i = 0; i < size; i++) {
			cout << "arr[" << i << "] = " << arr[i] << endl;
		}

		f.close();

		editNewSize(arr, size, filename_out, K, L);

	}
	else {
		cout << "File not found";
	}
}

bool checkfiles(string in, string out) {

	ifstream f_in;
	ifstream f_out;

	f_in.open(in);
	f_out.open(out);

	if (!f_in.is_open() || !f_out.is_open()) {
		f_in.close();
		f_out.close();
		return 0;
	}
	else if (f_in.is_open() && f_out.is_open()) {
		return 1;
	}
	else {
		return 0;
	}
}

void editNewSize(int*& arr, int n, string filename_out, int K, int L) {

	int save = n-(L-K);

	int* temp = new int(save);

	for (int i = 0; i < K; i++) {
		temp[i] = arr[i];
	}
	for (int i = L; i < n; i++,K++) {
		temp[K] = arr[i];
	}
	

	cout << "New Array\n";

	for (int i = 0; i < save; i++) {
		cout << "Arr[" << i << "] = " << temp[i] << endl;
	}

	ofstream outp(filename_out);
	if (!outp)
	{
		cerr << "Cannot open a file!" << endl;
		exit(1);
	}
	else {
		outp << "New Array: " << endl;
		for (int i = 0; i < save; i++) {
			outp << temp[i] << " ";
		}
	}
}

//Task Matrix40

void matrix40() {
	int n = 0, startPos = 0, rows = 0, cols = 0, skip = 0;
	string filename;

	string filename_in = "matr_in_40.txt";


	ifstream f;

	if (checkfile(filename_in)) {
		f.open(filename_in);

		string size;

		getline(f, size);

		for (int i = 0; i < size.size(); i++) {
			if (size[i] == ' ') {
				skip = i;
			}
		}
		rows = stoi(size);
		if (rows > 20) {
			cout << "Rows < 20!" << endl;
			exit(0);
		}
		else {
			for (int i = 0; i < size.size() - skip; i++) {
				size[i] = size[skip + i];
				size[skip + i] = 0;
			}

			cols = stoi(size);
			if (cols > 20) {
				cout << "Columns < 20!" << endl;
				exit(0);
			}
			else {
				cout << "ROWS = " << rows << endl << "COLS = " << cols << endl;
				int** arr = new int* [rows];
				for (int i = 0; i < rows; i++) {
					arr[i] = new int[cols];
				}
				fillArray(filename_in, arr, rows, cols);
				searchNumbers(arr, rows, cols, filename_in);
			}
		}
	}
	else {
		cout << "File do not found";
	}
}

void fillArray(string f_in, int**& arr, const int rows, const int cols) {
	string out;
	float num = 0;
	int numRows = 0, numCols = 0;

	ifstream f;

	istringstream iss(out);
	f.open(f_in);

	std::getline(f, out);

	while (getline(f, out) && numRows < rows) {
		istringstream iss(out);
		numCols = 0;

		while (iss >> num && numCols < cols) {
			arr[numRows][numCols] = num;
			numCols++;
		}
		numRows++;
	}

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			cout << arr[i][j] << " ";
		}
		cout << "\n";
	}
}

bool checkfile(string in) {

	ifstream f_in;
	f_in.open(in);

	if (f_in.is_open()) {
		return 1;
	}
	else {
		return 0;
	}
}

void searchNumbers(int** arr, const int rows, const int columns, string f_out) {
	
	for (int i = 0; i < rows; i++) {
		int MAX = 3E+5;
		int MIN = 0;
		int MAXtemp = 0;
		int MINtemp = 0;
		for (int j = 0; j < columns; j++) {
			if (arr[i][j] < MAX) {
				MAX = arr[i][j];
				MAXtemp = j;
			}
			if (arr[i][j] > MIN) {
				MIN = arr[i][j];
				MINtemp = j;
			}
		}
		swap(arr[i][MAXtemp], arr[i][MINtemp]);
	}

	ofstream outp;
	outp.open(f_out, ios::app);

	if (!outp)
	{
		cerr << "Can't open a file" << std::endl;
		exit(1);
	}
	else {
		outp << "\nEdited array:";
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < columns; j++) {
				outp << arr[i][j] << " ";
			}
			outp << "\n";
		}
	}
}

//Task Sort21

void sort21() {
	const int M = 20;

	float arr[M];
	string filename;

	string filename_in = "sort_in_21.txt";

	ifstream f;
	istringstream iss(filename_in);

	int count = 0;

	if (checkfile(filename_in)) {
		f.open(filename_in);

		while (count < M && f >> arr[count]) {
			count++;
		}

		for (int i = 0; i < count; i++) {
			cout << arr[i] << " ";
		}

		insertionSort(arr, count, filename_in);
	}
	else {
		cout << "File does not found";
	}
}

void insertionSort(float arr[N], int n, string f_in)
{
		for (int i = 1; i < n; ++i) {
			int key = arr[i];
			int j = i - 1;

			while (j >= 0 && arr[j] > key) {
				arr[j + 1] = arr[j];
				j = j - 1;
			}
			arr[j + 1] = key;
		}

	ofstream outp;
	outp.open(f_in, ios::app);

	if (!outp)
	{
		cerr << "Cannot open a file!" << std::endl;
		exit(1);
	}
	else {
		outp << "\n";
		for (int i = 0; i < n; i++) {
			outp << arr[i] << " ";
		}
	}
}

//End