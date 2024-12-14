#include <stdio.h>

void increment_quadrant_idx(int width, int height, int x, int y, int *quadrant_arr) {
    if (x < width / 2) {
        if (y < height /2 ){
            quadrant_arr[0] += 1;
            }
        else if (y > height / 2) {
            quadrant_arr[2] += 1;
            }
                
        }
    else if (x > width /2) {
            if (y < height /2 ){
                    quadrant_arr[1] += 1;
            }
            else if (y > height / 2) {
                        quadrant_arr[3] += 1;
                    }
            }
}

int main() {
    FILE *fptr;
    // Open file
    fptr = fopen("input.txt", "r");


    const int WIDTH = 101;
    const int HEIGHT = 103;
    const int N_LINES = 500;

    // Create empty of size n_lines * 4
    int input_arr[N_LINES][4];
    int quadrant_arr[4];

    quadrant_arr[0] = 0;
    quadrant_arr[1] = 0;
    quadrant_arr[2] = 0;
    quadrant_arr[3] = 0;
    // Read each line
    char line[256];
    int x;
    int y;
    int vx;
    int vy;


    int i = 0;
    while (fgets(line, sizeof(line), fptr)) {
        // Retrieve coordinates 
        if (sscanf(line, "p=%d,%d v=%d,%d", &x, &y, &vx, &vy)==4) {
            input_arr[i][0] = x;
            input_arr[i][1] = y;
            input_arr[i][2] = vx;
            input_arr[i][3] = vy;
        }
        i +=1;
    }

    
    for (i=0; i < N_LINES; i+=1) {
        x = input_arr[i][0];
        y = input_arr[i][1];
        vx = input_arr[i][2];
        vy = input_arr[i][3];

        int x_after = (x +( vx * 100)) % WIDTH;
        int y_after = (y + (vy * 100)) % HEIGHT;

        if (x_after < 0) {
            x_after = WIDTH + x_after;
        }
        if (y_after < 0) {
            y_after = HEIGHT + y_after;
        }    

        printf("X after: %d Y after: %d \n", x_after, y_after);
        increment_quadrant_idx(WIDTH,HEIGHT,x_after, y_after, quadrant_arr);
        printf("Quadrant %d %d %d %d\n",quadrant_arr[0],  quadrant_arr[1], quadrant_arr[2] ,quadrant_arr[3]);

    }    

    int part1 = quadrant_arr[0] * quadrant_arr[1] * quadrant_arr[2] * quadrant_arr[3];
    printf("Result Part 1: %d \n", part1);

    }



