#include <iostream>
#include <stdio.h>
#include <unistd.h>
#include <fstream>
using namespace std;
int main(){
    for(int j=0; j<2; j++){
        string index = to_string(j);
        string filename = "./log/log"+index+".txt";
        if (remove(filename.c_str()))  std::cout << "file " << filename << " deleted.\n";
    }
    for(int j=0; j<2; j++){
        string content = "finish computing";
        ofstream file;
        string index = to_string(j);
        string filename = "./log/log"+index+".txt";
        //open file
        file.open(filename);
        if (!file.is_open()) {
                cout << "failed to open file" << filename << endl;
                return -1;
        }

        //simulate generate log file
        for(int i = 0; i < 5; i++){
            int a = 5;
            sleep(a);
            file<<"iter"<<i<<"has finished"<<endl;
        }

        //finish output log file
        file << content << endl;
        file.close();
    }
    return 0;
}

