#include <stdio.h>
#include <string.h>

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


    const long WIDTH = 101;
    const long HEIGHT = 103;
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
    long x;
    long y;
    long vx;
    long vy;


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
    const int N_MOVES = 10000;

    //int picture[HEIGHT][WIDTH];
    long quadrant_diff[N_MOVES][2]; 
    for (int n_moves = 0; n_moves < N_MOVES; n_moves +=1) {    
        //printf("Starting moves %d", n_moves);

        for (i=0; i < N_LINES; i+=1) {
            x = input_arr[i][0];
            y = input_arr[i][1];
            vx = input_arr[i][2];
            vy = input_arr[i][3];
            //printf("We are here %d \n", i);

            long x_after = (x +( vx * n_moves)) % WIDTH;
            long y_after = (y + (vy * n_moves)) % HEIGHT;
            //printf("x after %ld \n", x_after);
            //printf("y after %ld \n", y_after);
            //printf("core reached");

            if (x_after < 0) {
                x_after = WIDTH + x_after;
            }
            if (y_after < 0) {
                y_after = HEIGHT + y_after;
            }
            //printf("Did I dumb the core");
            //picture[y_after][x_after] = 1;
            increment_quadrant_idx(WIDTH,HEIGHT,x_after, y_after, quadrant_arr);
        }
        //printf("This is the diff with the max variance %d", quadrant_arr[0]*quadrant_arr[1]* quadrant_arr[2]*quadrant_arr[3]);

        quadrant_diff[n_moves][0] = (quadrant_arr[0] - quadrant_arr[1]);
        quadrant_diff[n_moves][1] = (quadrant_arr[2] - quadrant_arr[3]);

        quadrant_arr[0] = 0;
        quadrant_arr[1] = 0;
        quadrant_arr[2] = 0;
        quadrant_arr[3] = 0;       

    }  
    long min_test = 1000000;
    int min_test_idx = 0;
    for (int i=0; i< N_MOVES; i+=1) {
        if (quadrant_diff[i][0] - quadrant_diff[i][1] < min_test){
            min_test = quadrant_diff[i][0] - quadrant_diff[i][1];
            min_test_idx = i;

        }
    }
    int max_var_idx = min_test_idx;
    printf("Bottom and top left right quadrants are most similar %d", max_var_idx);

    int picture[HEIGHT][WIDTH];
    for (i=0; i < N_LINES; i+=1) {
        x = input_arr[i][0];
        y = input_arr[i][1];
        vx = input_arr[i][2];
        vy = input_arr[i][3];

        int x_after = (x +( vx * max_var_idx)) % WIDTH;
        int y_after = (y + (vy * max_var_idx)) % HEIGHT;

        if (x_after < 0) {
            x_after = WIDTH + x_after;
        }
        if (y_after < 0) {
            y_after = HEIGHT + y_after;
        }
        picture[y_after][x_after] += 1;
        }

  

        // Write the 2D array to the file (row by row)
        for (int img_i = 0; img_i < HEIGHT; img_i++) {
            for (int img_j = 0; img_j < WIDTH; img_j++) {   
                if (picture[img_i][img_j] > 0){
                    printf("%d ", picture[img_i][img_j]);  // Write pixel value

                }
                else {
                }                    printf("");  // Write pixel value


                }
            printf("\n");  // Newline at the end of each row
            }
}




