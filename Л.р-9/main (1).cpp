#include <iostream>
#include <cstring>

using namespace std;

void task26();
size_t find(const char* s, const char* point, size_t pos, size_t n);

void sstring32();
int countMatches(const string& S, const string& S0);


int main() {

	int choice = 0;

	while (choice != 3) {

		cout << "Choose task: "
			"\n1.Task26"  // size_t find (const char* s, size_t pos, size_t n) const;
			"\n2.String32"
			"\n3.Exit" << endl;

		cin >> choice;

		switch (choice) {
		case 1: {
			task26();		//Task task26
			break;
		}
		case 2: {
			sstring32();		//Task string32
			break;
		}
		case 3: {
			cout << "Program is end!";
			break;
		}
		default: {
			cout << "Wrong one, choose again!\n";
		}
		}
	}
}

void task26() {
    const char* s = "Hello, i'm a student Dikhtiarenko Mikhail, studying in Kharkov Aerospace Institute";
    const char* target = "studying";
    size_t pos = 0;
    size_t n = 120;

    size_t result = find(s, target, pos, n);

    if (result != string::npos) {
        cout << "Found at index: " << result << endl;
    }
    else {
        cout << "Not found" << endl;
    }
}


size_t find(const char* s, const char* point, size_t pos, size_t n) {
    size_t len_s = 0;
    size_t len_target = 0;

    while (s[len_s] != '\0') {
        len_s++;
    }

    while (point[len_target] != '\0') {
        len_target++;
    }

    if (len_target == 0) {
        return pos; 
    }

    if (pos >= len_s || len_target > n) {
        return string::npos; 
    }

    for (size_t i = pos; i <= len_s - len_target && i < pos + n; ++i) {
        size_t j = 0;
        while (j < len_target && s[i + j] == point[j]) {
            j++;
        }
        if (j == len_target) {
            return i; 
        }
    }

    return string::npos;
}

void sstring32() {
    string S, S0;

    cout << "Enter S: ";
    cin >> S;

    cout << "Enter S0: ";
    cin >> S0;

    int result = countMatches(S, S0);
    cout << "Count matches: " << result << endl;
}

int countMatches(const string& S, const string& S0) {
    if (S0.empty()) {
        return 0;
    }

    int count = 0;
    size_t pos = S.find(S0);

    while (pos != string::npos) {
        count++;
        pos = S.find(S0, pos + S0.length());
    }

    return count;
}