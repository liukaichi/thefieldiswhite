/*
 * Person.h
 *
 *  Created on: Jul 3, 2014
 *      Author: Nicholas
 */

#ifndef PERSON_H_
#define PERSON_H_

#include <string>
#include <sstream>

namespace std {

class Person {

	string name;
	int age;
	string gender;
	bool convert;
	int yearsBaptized;
	string hobby;

	int fth, hop, cha, obd, pat, knw, hum, spr, end, chr;


public:
	Person();
	Person(string n, int a, string g, bool c, int y, string h) {
		name = n;
		age = a;
		gender = g;
		convert = c;
		yearsBaptized = y;
		hobby = h;
		fth = hop = cha = obd = pat = knw = hum = spr = end = chr = 5;
	}

	int getAge() {
		return age;
	}

	int getYearsBaptized() {
		return yearsBaptized;
	}

	//A bunch of public functions to raise or lower the stat by m
	void incrFaith(int m) {
		fth = fth + m;
	}
	void incrHope(int m) {
		hop = hop + m;
	}
	void incrCharity(int m) {
		cha = cha + m;
	}
	void incrObedience(int m) {
		obd = obd + m;
	}
	void incrPatience(int m) {
		pat = pat + m;
	}
	void incrKnowledge(int m) {
		knw = knw + m;
	}
	void incrHumility(int m) {
		hum = hum + m;
	}
	void incrSpirit(int m) {
		spr = spr + m;
	}
	void incrEndurance(int m) {
		end = end + m;
	}
	void incrCharisma(int m) {
		chr = chr + m;
	}

	string toString() {
	  stringstream out;
	  out << "Name: " << name << endl;
	  out << "Age: " << age << endl;
	  out << "Gender: " << gender << endl;
	  out << "Convert: " << boolToString(convert) << endl;
	  out << "Years Baptized: " << yearsBaptized << endl;
	  out << "Hobby: " << hobby << endl;
	  out << "-- Stats -- " << endl;
	  out << "Faith: " << fth << endl;
	  out << "Hope: " << hop << endl;
	  out << "Charity: " << cha << endl;
	  out << "Obedience: " << obd << endl;
	  out << "Patience: " << pat << endl;
	  out << "Knowledge: " << knw << endl;
	  out << "Humility: " << hum << endl;
	  out << "Spirit: " << spr << endl;
	  out << "Endurance: " << end << endl;
	  out << "Charisma: " << chr;
	  return out.str();
	}

	string boolToString(bool b) {
		if(b)
			return "Yes";
		else
			return "No";
	}

	virtual ~Person(){}
};

} /* namespace std */

#endif /* PERSON_H_ */
