#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cstring>

using namespace std;

// Class to represent a hotel room
class Room {
public:
    int roomNumber;
    char customerName[50];
    double roomRate;
    bool isBooked;

    // Function to initialize the room
    void initializeRoom(int number, double rate) {
        roomNumber = number;
        roomRate = rate;
        isBooked = false;
        strcpy(customerName, "");
    }
};

// Class to manage hotel operations
class HotelManagementSystem {
private:
    Room rooms[100];  // Assuming there are 100 rooms in the hotel

public:
    // Function to display menu
    void displayMenu() {
        cout << "\n***** Hotel Management System *****\n";
        cout << "1. Book a Room\n";
        cout << "2. Search for Customer Details\n";
        cout << "3. View Total Allotted Rooms\n";
        cout << "4. Modify Record\n";
        cout << "5. Delete Record\n";
        cout << "6. Display Total Bill\n";
        cout << "7. Exit\n";
    }

    // Function to display available rooms
    void displayAvailableRooms() {
        cout << "\nAvailable Rooms:\n";
        cout << "-----------------\n";
        for (int i = 0; i < 100; ++i) {
            if (!rooms[i].isBooked) {
                cout << "Room " << rooms[i].roomNumber << "\n";
            }
        }
    }

    // Function to book a room
    void bookRoom() {
        int roomNumber;
        cout << "Enter Room Number: ";
        cin >> roomNumber;

        if (roomNumber < 1 || roomNumber > 100) {
            cout << "Invalid room number.\n";
            return;
        }

        if (rooms[roomNumber - 1].isBooked) {
            cout << "Room already booked.\n";
        } else {
            cout << "Enter Customer Name: ";
            cin.ignore(); // Clear the input buffer
            cin.getline(rooms[roomNumber - 1].customerName, 50);
            rooms[roomNumber - 1].isBooked = true;
            cout << "Room booked successfully.\n";
        }
    }

    // Function to search for customer details
    void searchCustomerDetails() {
        int roomNumber;
        cout << "Enter Room Number: ";
        cin >> roomNumber;

        if (roomNumber < 1 || roomNumber > 100) {
            cout << "Invalid room number.\n";
            return;
        }

        if (rooms[roomNumber - 1].isBooked) {
            cout << "Customer Name: " << rooms[roomNumber - 1].customerName << "\n";
        } else {
            cout << "Room is not booked.\n";
        }
    }

    // Function to view total allotted rooms
    void viewTotalAllottedRooms() {
        int totalBookedRooms = 0;
        for (int i = 0; i < 100; ++i) {
            if (rooms[i].isBooked) {
                totalBookedRooms++;
            }
        }
        cout << "Total Allotted Rooms: " << totalBookedRooms << "\n";
    }

    // Function to modify record
    void modifyRecord() {
        int roomNumber;
        cout << "Enter Room Number to Modify: ";
        cin >> roomNumber;

        if (roomNumber < 1 || roomNumber > 100) {
            cout << "Invalid room number.\n";
            return;
        }

        if (rooms[roomNumber - 1].isBooked) {
            cout << "Enter new Customer Name: ";
            cin.ignore(); // Clear the input buffer
            cin.getline(rooms[roomNumber - 1].customerName, 50);
            cout << "Record modified successfully.\n";
        } else {
            cout << "Room is not booked. Cannot modify record.\n";
        }
    }

    // Function to delete record
    void deleteRecord() {
        int roomNumber;
        cout << "Enter Room Number to Delete: ";
        cin >> roomNumber;

        if (roomNumber < 1 || roomNumber > 100) {
            cout << "Invalid room number.\n";
            return;
        }

        if (rooms[roomNumber - 1].isBooked) {
            rooms[roomNumber - 1].isBooked = false;
            strcpy(rooms[roomNumber - 1].customerName, "");
            cout << "Record deleted successfully.\n";
        } else {
            cout << "Room is not booked. Cannot delete record.\n";
        }
    }

    // Function to display total bill
    void displayTotalBill() {
        int roomNumber;
        cout << "Enter Room Number to Display Total Bill: ";
        cin >> roomNumber;

        if (roomNumber < 1 || roomNumber > 100) {
            cout << "Invalid room number.\n";
            return;
        }

        if (rooms[roomNumber - 1].isBooked) {
            cout << "Total Bill for Room " << roomNumber << ": $" << rooms[roomNumber - 1].roomRate << "\n";
        } else {
            cout << "Room is not booked. Cannot display total bill.\n";
        }
    }
};

int main() {
    HotelManagementSystem hotel;
    int choice;

    do {
        hotel.displayMenu();
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                hotel.bookRoom();
                break;
            case 2:
                hotel.searchCustomerDetails();
                break;
            case 3:
                hotel.viewTotalAllottedRooms();
                break;
            case 4:
                hotel.modifyRecord();
                break;
            case 5:
                hotel.deleteRecord();
                break;
            case 6:
                hotel.displayTotalBill();
                break;
            case 7:
                cout << "Exiting program.\n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }

        // Pause to see the output
        cout << "\nPress Enter to continue...";
        cin.ignore(); // Clear the input buffer
        cin.get();

    } while (choice != 7);

    return 0;
}
