#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

# define N 8110 // total number of temperatures existing in the file

// separate functions used for mean, standard deviation and variance calculation each

// mean function

double mean(double t[N]){
    
    double mn;
    int i;
    int sum = 0;
    
    // for-loop
    
    for(i=0; i<=N; i++){
        sum = sum + t[N];
    }
    
    mn = sum/N;
    return mn;
}

// variance function

double variance(double t[N]){
    
    double vnc;
	int i;
	int sum = 0;
	
	double m;
	double sqdiff = 0;
	
	for (i=0; i<=N; i++){
		
		sum = sum + t[i];
		m = mean(t);
		
		sqdiff = sqdiff + (t[i] - m) * (t[i] - m);
	}
	
	
	vnc = sqdiff/N;
	return vnc;
}

// standard deviation function

double stddev(double t[N]){
	
	double vnc;
	
	vnc = variance(t);
	double sdv = sqrt(vnc);
	return sdv;
	
}

int main(int argc, char** argv){
    
    FILE *fp;
    fp = fopen("temp-dataset.csv", "r");
    
    double t[N];
    int i, n;
    
    //function variable declarations
	
	double m; //mean
	double v; //variance
	double sd; //standard deviation
	
    // we read the second column of the file, consisting of temperatures in total.

    while (!feof(fp)) {
        
        char line[1024];
        fgets(line, 1024, fp);
        sscanf(line, "%*d,%lf", & t[i]);
        i++;
        
    }
    
    
    m = mean(t);
	printf("%f\n", m);
	
	v = variance(t);
	printf("%f\n", v);
	
	sd = stddev(t);
	printf("%f\n", sd);
	
    fclose(fp);
   
    return 0;
}
