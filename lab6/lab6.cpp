#include <iostream>
using namespace std;
#include <cmath>
const int MAX_SIZE = 100;
// Функція для введення масиву та його розміру
void inputArray(int arr[], int &size) {
    cout << "Введіть розмір масиву: ";
    cin >> size;

    cout << "Введіть елементи масиву: ";
    for (int i = 0; i < size; ++i) {
        cin >> arr[i];
    }
}

// Функція для виведення масиву
void printArray(int arr[], int size) {
    cout << "Масив: ";
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Завдання 1: Аналіз і виведення елементів масиву
void analyzeAndPrint(int arr[], int size) {
    printArray(arr, size);

    int result = 0;
    for (int i = 1; i < size; ++i) {
        if ((arr[i - 1] > 0 && arr[i] < 0) || (arr[i - 1] < 0 && arr[i] > 0)) {
            result = 0;
            break;
        }
        result = i + 1;
    }

    if (result == 0) {
        cout << "0 (чергуються додатні і негативні числа)" << endl;
    } else {
        cout << result << " (порушено закономірність)" << endl;
    }
}

// Завдання 2: Перетворення масиву
void transformArray(int arr[], int &size) {
    int K, L;
    cout << "Введіть значення K та L (1 ≤ K < L ≤ N): ";
    cin >> K >> L;

    if (K >= 1 && L < size && K < L) {
        for (int i = L; i >= K; --i) {
            for (int j = i; j < size - 1; ++j) {
                arr[j] = arr[j + 1];
            }
            size--;
        }

        cout << "Розмір нового масиву: " << size << endl;
        printArray(arr, size);
    } else {
        cout << "Некоректні значення K та L." << endl;
    }
}

int main() {
    int arr[MAX_SIZE];
    int size;

    int choice;

    do {
        cout << "Оберіть завдання (1 або 2, 0 - вихід): ";
        cin >> choice;

        switch (choice) { //перемикання між завданнями 
            case 1:
                inputArray(arr, size);
                analyzeAndPrint(arr, size);
                break;
            case 2:
                inputArray(arr, size);
                transformArray(arr, size);
                break;
            case 0:
                cout << "Програма завершила роботу." << endl;
                break;
            default:
                cout << "Невірний вибір. Спробуйте знову." << endl;
        }
    } while (choice != 0);

    return 0;
}