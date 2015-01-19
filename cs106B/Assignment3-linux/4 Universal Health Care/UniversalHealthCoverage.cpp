/*
 * File: UniversalHealthCoverage.cpp
 * ----------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the UniversalHealthCoverage problem
 * on Assignment #3.
 * [TODO: extend the documentation]
 */
#include <iostream>
#include <string>
#include "set.h"
#include "vector.h"
//#include "console.h"
using namespace std;

/* Function: canOfferUniversalCoverage(Set<string>& cities,
 *                                     Vector< Set<string> >& locations,
 *                                     int numHospitals,
 *                                     Vector< Set<string> >& result);
 * Usage: if (canOfferUniversalCoverage(cities, locations, 4, result)
 * ==================================================================
 * Given a set of cities, a list of what cities various hospitals can
 * cover, and a number of hospitals, returns whether or not it's
 * possible to provide coverage to all cities with the given number of
 * hospitals.  If so, one specific way to do this is handed back in the
 * result parameter.
 */
bool canOfferUniversalCoverage(Set<string>& cities,
                               Vector< Set<string> >& locations,
                               int numHospitals,
                               Vector< Set<string> >& result);


int main() {
  Set<string> cities;
  cities.add("A");
  cities.add("B");
  cities.add("C");
  cities.add("D");
  cities.add("E");
  cities.add("F");
  Set<string> HospitalOne;
  HospitalOne += "A","B","C";
  Set<string> HospitalTwo;
  HospitalTwo += "A","D","C";
  Set<string> HospitalThree;
  HospitalThree +="E", "B","F";
  Set<string> HospitalFour;
  HospitalFour += "F","C";
  Vector< Set<string> > locations;
  Vector< Set<string> > result;
  locations +=HospitalOne, HospitalTwo, HospitalThree, HospitalFour;
  int numHospitals=3;
  bool tag = canOfferUniversalCoverage(cities, locations, numHospitals, result);
  if(tag)
    cout<<1<<endl;
  return 0;
}


bool canOfferUniversalCoverage(Set<string>& cities,
			       Vector< Set<string> >& locations,
			       int numHospitals,
			       Vector< Set<string> >& result){
  if(cities.isEmpty()) { cout<<result<<endl; return true;}
  if(numHospitals==0) return false;
  if(locations.isEmpty()) return false;
  else{
    Set<string> firstSet=locations[0];
    Set<string> citiesWithFirst = cities-firstSet;
    Vector< Set<string> > oriResult = result;
    result += firstSet;
    locations.remove(0);
    bool withFirst = canOfferUniversalCoverage(citiesWithFirst, locations, numHospitals-1, result);
    bool withOutFirst = canOfferUniversalCoverage(cities, locations, numHospitals, oriResult);
    return withFirst||withOutFirst;
  }
}

