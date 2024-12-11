#include <iostream>
#include <string>

using namespace std;

struct Node {
    int prn;
    string name;
    Node* next;
};

// Class to manage the Pinnacle Club linked list
class PinnacleClub {
private:
    Node* head;  // Pointer to president (first node)
    Node* tail;  // Pointer to secretary (last node)

public:
    PinnacleClub() {
        head = nullptr;
        tail = nullptr;
    }

    // Function to add the president
    void addPresident(int prn, string name) {
        Node* newNode = new Node;
        newNode->prn = prn;
        newNode->name = name;
        newNode->next = head;
        head = newNode;
        if (tail == nullptr) {
            tail = head;  // If no secretary yet, tail points to the president
        }
        cout << name << " has been added as the president." << endl;
    }

    // Function to add the secretary
    void addSecretary(int prn, string name) {
        if (head == nullptr) {
            cout << "You must add a president before adding a secretary." << endl;
            return;
        }
        Node* newNode = new Node;
        newNode->prn = prn;
        newNode->name = name;
        newNode->next = nullptr;
        if (tail != nullptr) {
            tail->next = newNode;
        }
        tail = newNode;
        cout << name << " has been added as the secretary." << endl;
    }

    // Function to add a regular member between the president and secretary
    void addMember(int prn, string name) {
        if (head == nullptr || tail == nullptr) {
            cout << "You must add both a president and a secretary first." << endl;
            return;
        }
        Node* newNode = new Node;
        newNode->prn = prn;
        newNode->name = name;

        // Insert member between president and secretary
        Node* temp = head;
        while (temp->next != tail) {
            temp = temp->next;
        }
        newNode->next = tail;
        temp->next = newNode;

        cout << name << " has been added as a member." << endl;
    }

    // Function to delete a member by PRN
    void deleteMember(int prn) {
        if (head == nullptr) {
            cout << "The club is empty, no members to delete." << endl;
            return;
        }

        Node* temp = head;
        Node* prev = nullptr;

        // Check if the member to delete is the president
        if (temp != nullptr && temp->prn == prn) {
            head = temp->next;
            cout << temp->name << " (" << temp->prn << ") has been removed as president." << endl;
            delete temp;
            return;
        }

        // Traverse the list to find the member to delete
        while (temp != nullptr && temp->prn != prn) {
            prev = temp;
            temp = temp->next;
        }

        // If member not found
        if (temp == nullptr) {
            cout << "Member with PRN " << prn << " not found." << endl;
            return;
        }

        // If the member to delete is the secretary
        if (temp == tail) {
            tail = prev;
        }

        prev->next = temp->next;
        cout << temp->name << " (" << temp->prn << ") has been removed." << endl;
        delete temp;
    }

    // Function to display all members
    void displayMembers() {
        if (head == nullptr) {
            cout << "No members in the club." << endl;
            return;
        }

        Node* temp = head;
        cout << "Members of the Pinnacle Club:" << endl;
        while (temp != nullptr) {
            if (temp == head) {
                cout << "President: ";
            } else if (temp == tail) {
                cout << "Secretary: ";
            } else {
                cout << "Member: ";
            }
            cout << temp->name << " (" << temp->prn << ")" << endl;
            temp = temp->next;
        }
    }

    // Function to compute the total number of members
    int countMembers() {
        int count = 0;
        Node* temp = head;
        while (temp != nullptr) {
            count++;
            temp = temp->next;
        }
        return count;
    }
};

int main() {
    PinnacleClub club;
    int choice, prn;
    string name;

    // First, add the president and secretary
    cout << "Enter PRN of President: ";
    cin >> prn;
    cin.ignore();
    cout << "Enter Name of President: ";
    getline(cin, name);
    club.addPresident(prn, name);

    cout << "Enter PRN of Secretary: ";
    cin >> prn;
    cin.ignore();
    cout << "Enter Name of Secretary: ";
    getline(cin, name);
    club.addSecretary(prn, name);

    do {
        cout << "\n----- Pinnacle Club Menu -----\n";
        cout << "1. Add Member\n";
        cout << "2. Remove Member\n";
        cout << "3. Display Members\n";
        cout << "4. Count Members\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter PRN of Member: ";
            cin >> prn;
            cin.ignore();
            cout << "Enter Name of Member: ";
            getline(cin, name);
            club.addMember(prn, name);
            break;

        case 2:
            cout << "Enter PRN of member to remove: ";
            cin >> prn;
            club.deleteMember(prn);
            break;

        case 3:
            club.displayMembers();
            break;

        case 4:
            cout << "Total members in the club: " << club.countMembers() << endl;
            break;

        case 5:
            cout << "Exiting the program." << endl;
            break;

        default:
            cout << "Invalid choice, please try again." << endl;
        }

    } while (choice != 5);

    return 0;
}




// Add President: O(1)
// Add Secretary: O(1)
// Add Regular Member: O(1)
// Delete Member: O(n)
// Delete President: O(1)
// Delete Secretary: O(n)
// Get Total Members: O(1)
// Display Members: O(n)


// In summary:

// Operations such as adding a President, Secretary, and regular member are constant time, O(1).
// Deleting a member, deleting the Secretary, and displaying members all require linear time, 
// O(n), where n is the number of members in the club.





