#include <iostream>
#include <cstring>
#include <fstream>

long getMax(long arr[], int n){
    long mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx)
            mx = arr[i];
    return mx;
}
 
void countSort(long arr[], int n, int exp){
    int output[n]; 
    int i, count[10] = { 0 };
 
    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
 
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
 
    for (i = n - 1; i >= 0; i--){
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
 
    for (i = 0; i < n; i++)
        arr[i] = output[i];
}
 
void radixsort(long arr[], int n){
    long m = getMax(arr, n);
 
    for (int exp = 1; m / exp > 0; exp *= 10)
        countSort(arr, n, exp);
}
 
void print(long arr[], int n){
    for (int i = 0; i < n; i++)
        std::cout << arr[i] << " ";
}
  
int main() 
{ 
    std::fstream input_file("../data/quick_sort_data.txt", std::ios_base::in);
    long N, number;
    input_file >> N;
    
    long arr[N];
    int i = 0;
    while (input_file >> number) {
        arr[i++] = number;
    }
    input_file.close();

    radixsort(arr, N); 
    std::cout << "Sorted array: \n"; 
    print(arr, N);
    return 0; 
} 