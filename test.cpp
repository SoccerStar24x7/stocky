#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

auto reader() {
    std::ifstream file("data.csv");
    std::string line;

    std::vector<std::string> open;
    std::vector<std::string> high;
    std::vector<std::string> low;
    std::vector<std::string> close;
    std::vector<std::string> volume;


    // go through csv and get data ----------------------

    while (std::getline(file, line)) {
        std::string cell;
        std::stringstream ss(line);
        
        int num = 1;

        while (std::getline(ss, cell, ',')) {

            if (cell == "Open" || cell == "High" || cell == "Low" || cell == "Close" || cell == "Volume")
                continue;
            
            switch(num) {
                case 1:
                    open.push_back(cell);
                    break;

                case 2:
                    high.push_back(cell);
                    break;
                
                case 3:
                    low.push_back(cell);
                    break;

                case 4:
                    close.push_back(cell);
                    break;

                case 5:
                    volume.push_back(cell);
                    break;
                };

            num++;
        }

    }
    return open, high, low, close, volume;
}

int main() {
    reader();
}