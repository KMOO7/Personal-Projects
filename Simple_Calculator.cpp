#include <iostream>
using namespace std;
int main()
{
    int operation;
    int num1, num2;
    
    do
    {
        cout << "\n===== Calculator Menu =====" << endl;
        cout << "\nMenu for Arithmeitc Operators \nPlease select the arithmetic operation  \n1. For Addition \n2. For Subtraction \n3. For Multiplication \n4. For Divsion \n5. Exit \n";
        cout << "Enter your choice ";
        cin >> operation;

        if (operation < 1 || operation > 5)
        {
            cout << "Error!! Invalid Choice please select again\n";
            continue;
        }

        if (operation == 5)
        {
            cout << "Successfully exited from the software";
            break;
        }

        cout << "Enter the first number ";
        cin >> num1;
        cout << "Enter the second number ";
        cin >> num2;

        if (operation == 1)
        {
            printf("\nSum of %d and %d is:%d \n", num1, num2, num1 + num2);
        }

        else if (operation == 2)
        {
            printf("\nDifference of %d and %d is:%d \n", num1, num2, num1 - num2);
        }

        else if (operation == 3)
        {
            printf("\nProduct of %d and %d is:%d \n", num1, num2, num1 * num2);
        }

        else
        {
            if(num2==0){
                cout<<"\nError!!\n"
                "Enter a non-zero second number";
            }
            else {
                  printf("\nDivisor of %d after dividing with %d is:%d \n", num1, num2, num1 / num2);
            }
          
        }

    } while (true);
    return 0;
}