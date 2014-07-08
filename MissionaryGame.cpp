//============================================================================
// Name        : MissionaryGame.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include "Person.h"
using namespace std;

string toLowerCase(string&);
Person intro();

string hobbyList[] = {"Basketball", "Computers", "Music", "Art", "League of Legends"};
string trialList[] = {"Family Opposition", "Financial Need", "No Time", "Not interested"};
string scriptMasteryList[] = {"1 Ne 3:7", "Alma: 32:21", "2 Ne 8:3"};

int main() {
	cout << "<<<<<<Welcome to the Missionary Game!>>>>>" << endl;
	Person player = intro();
	cout << player.toString() << endl;
	player.incrObedience(1);
	player.incrCharity(-1);
	cout << player.toString() << endl;
	//srand(time(NULL));
	//cout << rand() % 1000 + 1 << endl;
	//Person player1 = new Person(Adams);
	return 0;
}

Person intro() {

	string name;
	string gender;
	int age;
	bool convert;
	int yearsBaptized;
	string hobby;

	//First determines gender/title
    bool response = false;
    string title = "";
    while (response == false) {
        cout << "Are you Male or Female? (M/F): ";
        cin >> gender;
        if (toLowerCase(gender) == "m") {
            title = "Elder";
            response = true;
        } else if (toLowerCase(gender) == "f") {
            title = "Sister";
            response = true;
        }
    }

    //asks last name, creates name combined with title
    response = false;
    while (response == false) {
    	cout << "What's your last name, " << title << "? ";
    	string lastName;
    	cin >> lastName;
        name = title + " " + lastName;
        if (name.length() != 0) {
            string confirmName;
            cout << "You said " << name << ", was it? (y/n) ";
            cin >> confirmName;
            if (toLowerCase(confirmName) == "y") {
                response = true;
            } else if (toLowerCase(confirmName) == "n") {
                response = false;
            } else {
                cout << "I'm sorry, can you respond with (y/n)?" << endl;
            }
        }
    }
    cout << "Hello, " << name << "! Thanks for trying out the missionary game!" << endl;
    cout << "So we need to ask you some questions before you can embark on your journey!" << endl;

    //This part determines Age
    bool eligible = false;
    while (eligible == false) {
        cout << "How old are you?: ";
    	cin >> age;
        if(age < 18) {
            cout << "Wait, come again? Have you even graduated high school?" << endl;
            eligible = false;
        } else if (age == 18) {
            cout << "A youngster, huh? Thanks for being willing to serve!" << endl;
            eligible = true;
        } else if (age <= 27) {
            cout << "Thank you for being willing to serve!" << endl;
            eligible = true;
        } else if (age > 27) {
            cout << "I'm sorry, you might be a little too old..." << endl;
            eligible = false;
        }
    }

    //This part determines if they are a convert
    bool convertConfirm = false;
    while (convertConfirm == false) {
    	cout << "Are you a convert to the church?(y/n) ";
        string convertAnswer;
        cin >> convertAnswer;
        if (toLowerCase(convertAnswer) == "n") {
            convert = false;
            convertConfirm = true;
            cout << "That's wonderful! We're glad to have you here!" << endl;
            yearsBaptized = age - 8;
        } else if (convertAnswer == "y") {
            convert = true;
            convertConfirm = true;
            cout << "How many years ago did you get baptized? ";
            cin >> yearsBaptized;
            cout << "Wow!" << endl;

            if (yearsBaptized == 1) {
                cout << "1 year, huh?" << endl;
            } else if (yearsBaptized < age - 8) {
                cout << yearsBaptized << " years? " << endl;
            }
            cout << "You'll bring a lot of fire to the mission for sure!" << endl;
        } else {
            cout << "I'm sorry, can you respond with (y/n)?" << endl;
        }
    }

    //Choosing a hobby
    bool chosen = false;
    int hobbyNum;
    while (chosen == false) {
        for (unsigned i = 0; i < sizeof(hobbyList)/sizeof(*hobbyList); i++) {
            cout << i + 1 << " " << hobbyList[i] << endl;
        }
        cout << "So what do you like to do for fun?: (1-5) ";
        cin >> hobbyNum;
        if (cin.fail() || hobbyNum > 5 || hobbyNum < 1) {
            cout << "Can you say that again?" << endl;
        } else {
            hobby = hobbyList[hobbyNum-1];
            if (hobby.length() > 0) {
                chosen = true;
            }
        }
    }

    //This last part creates the character
    Person player(name, age, gender, convert, yearsBaptized, hobby);

    return player;
}

string toLowerCase(string& w) {
  /*for(char& c : w)
    {
      c = tolower(c);
    }*/
  for(unsigned i = 0; i < w.size(); ++i) {
      w[i] = tolower(w[i]);
  }
  return w;
}
