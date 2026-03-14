#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::ifstream file("data.csv");
    std::string line;

    std::vector<std::string> open;
    std::vector<std::string> high;
    std::vector<std::string> low;
    std::vector<std::string> close;
    std::vector<std::string> volume;

    while (std::getline(file, line)) {
        std::string cell;
        std::stringstream ss(line);
        std::vector<std::string> row;

        while (std::getline(ss, cell, ',')) {
            row.push_back(cell);
            std::cout << cell << " ";

            for (int i = 1; i <= 5; i++) {
                switch(i) {
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
            }
        }
    }
    for (int i = 0; i < volume.size(); i++)
        std::cout << volume[i] << std::endl;
}