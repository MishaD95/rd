#include <iostream>

using namespace std;

struct TTime {
	int hrs, min, sec;
};

struct VVariables {
	int A, B;
};

struct NNums {
	int A, B, C;
};

void param79();
void func(TTime& T);
void AddSec(TTime& T);

void begin22();
void Reverse(VVariables& V);

void boolean12();
void is(NNums& n);
bool isPositive(int A, int B, int C);

int main() {

	int choice = 0;

	while (choice != 4) {

		cout << "Choose task: "
			"\n1.Param79"
			"\n2.Begin22"
			"\n3.Boolean14"
			"\n4.Exit" << endl;

		cin >> choice;

		switch (choice) {
		case 1: {
			param79();		//Task param79
			break;
		}
		case 2: {
			begin22();		//Task begin22
			break;
		}
		case 3: {
			boolean12();		//Task boolean12
			break;
		}
		case 4: {
			cout << "Program is end!";
			break;
		}
		default: {
			cout << "Wrong one, choose again!\n";
		}
		}
	}
}

//Start param79

void param79() {
	TTime t1, t2, t3, t4, t5;
	func(t1);
	func(t2);
	func(t3);
	func(t4);
	func(t5);

}

void func(TTime& T) {
	cout << "Enter hours: ";
	cin >> T.hrs;

	cout << "Enter minutes: ";
	cin >> T.min;

	cout << "Enter a seconds: ";
	cin >> T.sec;


	if (T.hrs < 24 && T.min < 60 && T.sec < 60) {
		AddSec(T);
		cout << "Edited hours:\n ";
		cout << T.hrs << ":" << T.min << ":" << T.sec << "\n";
	}
	else if (T.hrs > 23) {
		cout << "\nHours > 24!";
	}
	else if (T.min > 59) {
		cout << "\nMinutes > 59!";
	}
	else if (T.hrs > 59) {
		cout << "\nSeconds > 59!";
	}
}

void AddSec(TTime& T) {
	int N;

	cout << "How much secs you want to add: ";
	cin >> N;
	int temp = 0;

	do {
		N -= 60;
		T.min++;
	} while (N > 60);
	T.sec += N;
	if (T.sec >= 60) {
		temp = T.sec / 60;
		T.sec %= 60;
		T.min += temp;
	}
	if (T.min >= 60) {
		temp = T.min / 60;
		T.min %= 60;
		T.hrs += temp;
	}
	if (T.hrs >= 24) {
		temp = T.hrs / 24;
		T.hrs %= 24;
	}
	do {
		T.hrs;
		T.min - 60;
	} while (T.min > 60);
}

//End Param79

//Start begin22

void begin22() {
	VVariables V;
	Reverse(V);
}

void Reverse(VVariables& V) {
	cout << "Enter A: ";
	cin >> V.A;
	cout << "Enter B: ";
	cin >> V.B;

	swap(V.A, V.B);

	cout << "A = " << V.A << endl;
	cout << "B = " << V.B << endl;

}

//End begin22

//Start boolean12
void boolean12() {
	NNums n;
	is(n);

}

void is(NNums& N) {
	cout << "Enter A: ";
	cin >> N.A;
	cout << "Enter B: ";
	cin >> N.B;
	cout << "Enter C: ";
	cin >> N.C;

	cout << "Each number from these are positive =  " << boolalpha << isPositive(N.A, N.B, N.C) << endl;
}

bool isPositive(int A, int B, int C) {
	return (A > 0 && B > 0 && C > 0);
}

//End boolean12