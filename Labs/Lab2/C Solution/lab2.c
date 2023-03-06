#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// mean calculation

double mean(double t[12], int n){
	
	double result;
	int i;
	int sum = 0;
	
	// loop
	
	for(i=0; i<=12; i++){
		sum = sum + t[12];
	}
	
	result = sum/n;
	return result;
	
}

// variance calculation

double variance(double t[12], int n){
	
	double s;
	int i;
	int sum = 0;
	
	double m;
	double sqdiff = 0;
	
	for (i=0; i<=12; i++){
		
		sum = sum + t[i];
		m = mean(t, 12);
		
		sqdiff = sqdiff + (t[i] - m) * (t[i] - m);
	}
	
	
	s = sqdiff/n;
	return s;
}

// standard deviation calculation

double stddev(double t[12], int n){
	
	double s;
	
	s = variance(t, 12);
	double sdv = sqrt(s);
	return sdv;
	
}

int main(int argc, char** argv){
	
	// variable declaration
	
	int n = 12;
	double t[12];
	int i;
	double result;
	
	//function variable declarations
	
	double m; //mean
	double v; //variance
	double sd; //standard deviation
	
	t[1]=4.7;
	t[2]=6.0;
	t[3]=8.8;
	t[4]=12.5;
	t[5]=17.6;
	t[6]=22.0;
	t[7]=25.0;
	t[8]=24.6;
	t[9]=19.9;
	t[10]=14.9;
	t[11]=9.8;
	t[12]=5.9;
	
	m = mean(t, 12);
	printf("%f\n", m);
	
	v = variance(t, 12);
	printf("%f\n", v);
	
	sd = stddev(t, 12);
	printf("%f\n", sd);
	
	return 0;
}
