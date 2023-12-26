#include <iostream>
using namespace std;
#include <cmath>
void task_if22 ();
void task_geom16 ();
void task_geom16_2 ();

int main () {
    int menu;
    cout << "Обери завдання:"<<endl;
    cout << "1. Визначити номер координатної чверті, в якій знаходиться дана точка"<<endl;
    cout << "2. Чи потрапляє точка в фігуру?"<<endl;
    cout << "3. Площа та периметр фігури"<<endl;
    cin >> menu;
    switch (menu) { // перемикання між завданнями
    case 1: task_if22 (); break; // Завдання 1
    case 2: task_geom16 (); break; // Завдання 2
    case 3: task_geom16_2 (); break; // Завдання 3
    default: cout << "Неіснуюче завдання (1-3 тільки!)" << endl; //повідомлення про помилку
    }
    return 0;
}

void task_if22 () {
    double x, y; // Створення змінних для введення координат
    cout << "Введіть координату х: "; //Введення координат
    cin >> x;
    cout << "Введіть координату y: ";
    cin >> y;
    int q; 
    if (x>0&&y>0) { //Визначення номеру координатної чверті 
        q =1;
    }
    else if (x<0&&y>0){
        q=2;
    }
    else if (x<0&&y<0){
        q=3;
    }
    else if (x>0&&y<0){
        q=4;
    }
    else {
        cout<<"Точка лежить на координатних осях або в початку координат"<<endl;
    }
    cout << "Точка знаходиться в "<< q<<" координатній чверті."<<endl; // Виведення результату
}


void task_geom16 () {
    double x,y;  //Створення змінних
    cout<< "Введіть координату x: "; //Введення координат точки
    cin>>x;
    cout<< "Введіть координату y: ";
    cin>>y;
    double circleR; 
    cout <<"Введіть радіус зони кола: "; //Введення радіуса
    cin>>circleR;
    if (x<0&&y<0&&std::sqrt(x*x+y*y)<=circleR){
    cout <<"Точка потрапляє в зону"<<endl; 
    }
    else{
    cout <<"Точка не потрапляє в зону кола"<<endl;    
        }
}

void task_geom16_2 () {
    double R;
    cout <<"Введіть радіус: ";
    cin>>R;
    double Pl = M_PI * std::pow(R,2)/2;
    double P = M_PI*R+2*R;
    cout <<"Площа напівкола: "<<Pl<<endl;
    cout <<"Периметр напівкола: "<<P<<endl;
}