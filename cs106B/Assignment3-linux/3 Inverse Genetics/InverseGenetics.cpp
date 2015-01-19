/*
 * File: InverseGenetics.cpp
 * ----------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the InverseGenetics problem
 * on Assignment #3.
 * [TODO: extend the documentation]
 */
#include <iostream>
#include <string>
#include <fstream>
#include "set.h"
#include "map.h"
#include "vector.h"
//#include "console.h"
using namespace std;

/* Function: listAllRNAStrandsFor(string protein,
 *                                Map<char, Set<string> >& codons);
 * Usage: listAllRNAStrandsFor("PARTY", codons);
 * ==================================================================
 * Given a protein and a map from amino acid codes to the codons for
 * that code, lists all possible RNA strands that could generate
 * that protein
 */
void listAllRNAStrandsFor(string protein, Map<char, Set<string> >& codons);

/* Function: loadCodonMap();
 * Usage: Map<char, Lexicon> codonMap = loadCodonMap();
 * ==================================================================
 * Loads the codon mapping table from a file.
 */
Map<char, Set<string> > loadCodonMap();
Vector<string> listAll(string protein, Map<char, Set<string> >& codons);
int main() {
	/* Load the codon map. */
	Map<char, Set<string> > codons = loadCodonMap();
	listAllRNAStrandsFor("LSKW", codons);
	return 0;
}

void listAllRNAStrandsFor(string protein, Map<char, Set<string> >& codons){
  Set<string> protSet = codons[protein[0]];
  if(protein.length()==1){
    foreach(string str in protSet){
      cout<<str<<endl;
    }
  }
  else{
    foreach(string str in protSet){
      cout<<str;
      listAllRNAStrandsFor(protein.substr(1), codons);
    }
  }
}

Vector<string> listAll(string protein, Map<char, Set<string> >& codons){
  Vector<string> result;
  if(protein.length()==1){
    Set<string> protSet = codons[protein[0]];
    foreach(string str in protSet)
      result += str;
    return result;}
  else{
    Set<string> protSet = codons[protein[0]];
    foreach(string str in protSet){
      foreach(string str1 in listAll(protein.substr(1), codons)){
	  result += str+str1;
	}
	}
    }
}


/* You do not need to change this function. */
Map<char, Set<string> > loadCodonMap() {
	ifstream input("codons.txt");
	Map<char, Set<string> > result;
    
	/* The current codon / protein combination. */
	string codon;
	char protein;
	
	/* Continuously pull data from the file until all data has been
	 * read.
	 */
	while (input >> codon >> protein) {
		result[protein] += codon;
	}
	
	return result;
}

