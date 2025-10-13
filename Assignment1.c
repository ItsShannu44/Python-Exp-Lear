#include<stdio.h>

int main() {
    printf("Size of int: %d\n",sizeof(int));
    printf("Size of float: %d\n",sizeof(float));
    printf("Size of double: %d\n",sizeof(double));
    printf("Size of char: %d \n",sizeof(char));
    printf("Size of long: %d \n",sizeof(long));
    
    return 0;
}


#include<stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int *ptr = arr;  
    
    printf("Array elements: ");
    for(int i=0; i<5; i++) {
        printf("%d ", *ptr);  
        ptr++; 
    }
    
    return 0;
}




#include<stdio.h>
int findSum(int mat[3][3]) {
    int sum = 0;
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            sum += mat[i][j];
        }
    }
    return sum;
}

int main() {
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    int total = findSum(matrix);
    printf("Sum of the matrix elements: %d\n", total);
    
    return 0;
}



#include<stdio.h>

int main() {
    int arr1D[5] = {10, 20, 30, 40, 50};
    int base1D = 2000; 
    int index = 2;
    int size = sizeof(int);
    
    int address1D = base1D + (index * size);
    printf("Address of element at index %d in 1D Array: %d\n", index, address1D);
    int arr2D[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int base2D = 3000;  
    int rows = 3, cols = 3;
    int i = 1, j = 2; 
    int address2D = base2D + ((i * cols) + j) * size;
    printf("Address of element at (%d, %d) in 2D Array: %d\n", i, j, address2D);
    
    return 0;
}


#include<stdio.h>
float calculateAverage(int arr[], int size) {
    int sum = 0;
    for(int i=0; i<size; i++) {
        sum += arr[i];
    }
    return (float)sum / size;  
}

int main() {
    int numbers[5] = {10, 20, 25, 30, 30};
    int n = 5;
    
    float avg = calculateAverage(numbers, n);
    printf("Average of the array: %.1f\n", avg);
    
    return 0;
}



#include<stdio.h>
#include<string.h>
struct Student {
    char name[50];
    int age;
    float marks;
};
float findAverageMarks(struct Student students[], int count) {
    float total = 0;
    for(int i=0; i<count; i++) {
        total += students[i].marks;
    }
    return total / count;
}
int main() {
    struct Student class[3];
    strcpy(class[0].name, "Alice");
    class[0].age = 20;
    class[0].marks = 85.5;
    
    strcpy(class[1].name, "Bob");
    class[1].age = 21;
    class[1].marks = 76.0;
    
    strcpy(class[2].name, "Charlie");
    class[2].age = 19;
    class[2].marks = 74.0;
    
    float avg_marks = findAverageMarks(class, 3);
    printf("Average marks of students: %.1f\n", avg_marks);
    
    return 0;
}