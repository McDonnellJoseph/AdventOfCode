#include <array>
#include <stdio.h>
#include <stdlib.h>

std::array<typename Tp, size_t Nm>

int main() {
    FILE *fptr;
    // Open file
    fptr = fopen("input.txt", "r");


    const int WIDTH = 101;
    const int HEIGHT = 103;
    const int N_LINES = 500;

    // Create empty of size n_lines * 4
    int input_arr[N_LINES][4];

    while (fgets(line, sizeof(line), fptr)) {
        // Retrieve coordinates 
        if (sscanf(line, "p=%d,%d v=%d,%d", &x, &y, &vx, &vy)==4) {
            //printf("Coords x: %d and y: %d, velocity x: %d, y: %d \n", x,y, vx, vy);
            int x_after = (x +( vx * 100)) % WIDTH;
            int y_after = (y + (vy * 100)) % HEIGHT;

            if (x_after < 0) {
                x_after = WIDTH + x_after;
            }
            if (y_after<0) {
                y_after = HEIGHT + y_after;
            }
           // printf("Final postion x: %d and y: %d \n", x_after,y_after);

            if (x_after < WIDTH / 2) {
                if (y_after < HEIGHT /2 ){
                    quadrant_ul = quadrant_ul + 1;
                }
                else if (y_after > HEIGHT / 2) {
                        quadrant_ll = quadrant_ll + 1;
                    }
                
            }
            else if (x_after > WIDTH /2) {
                if (y_after < HEIGHT /2 ){
                    quadrant_ur = quadrant_ur + 1;
                }
                else if (y_after > HEIGHT / 2) {
                        quadrant_lr = quadrant_lr + 1;
                    }
            }
            
            }
  
        };
    
    // Read each line
    char line[256];

    const int WIDTH = 101;
    const int HEIGHT = 103;

    int x;
    int y;
    int vx;
    int vy;

    int quadrant_ul = 0;
    int quadrant_ur = 0;
    int quadrant_ll = 0;
    int quadrant_lr = 0;


    printf("Total Upper left quadrant %d \n", quadrant_ul);
    printf("Total Upper right quadrant %d \n", quadrant_ur);
    printf("Total Lower left quadrant %d \n", quadrant_ll);
    printf("Total Lower right quadrant %d \n", quadrant_lr);
    int part1 = quadrant_ul * quadrant_ur * quadrant_ll * quadrant_lr;
    printf("Result Part 1: %d \n", part1);

    }



