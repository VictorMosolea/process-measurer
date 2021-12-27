import java.io.*;
import java.util.*;

class radix_sort {
	static int getMax(int arr[], int n){
		int mx = arr[0];
		for (int i = 1; i < n; i++)
			if (arr[i] > mx)
				mx = arr[i];
		return mx;
	}

	static void countSort(int arr[], int n, int exp){
		int output[] = new int[n]; 
		int i;
		int count[] = new int[10];
		Arrays.fill(count, 0);

		for (i = 0; i < n; i++)
			count[(arr[i] / exp) % 10]++;

		for (i = 1; i < 10; i++)
			count[i] += count[i - 1];

		for (i = n - 1; i >= 0; i--) {
			output[count[(arr[i] / exp) % 10] - 1] = arr[i];
			count[(arr[i] / exp) % 10]--;
		}

		for (i = 0; i < n; i++)
			arr[i] = output[i];
	}

	static void radixsort(int arr[], int n){
		int m = getMax(arr, n);

		for (int exp = 1; m / exp > 0; exp *= 10)
			countSort(arr, n, exp);
	}

	static void print(int arr[], int n){
		for (int i = 0; i < n; i++)
			System.out.print(arr[i] + " ");
	}
	public static void main(String[] args) throws FileNotFoundException{
        Scanner scanner = new Scanner(new File("../data/radix_sort_data.txt"));
        int N = 0;
        if(scanner.hasNextInt()){
            N = scanner.nextInt();
        }

        int [] arr = new int [N];
        int i = 0;

        while(scanner.hasNext()){
            String temp = scanner.next();
            arr[i++] = Integer.parseInt(temp);
        }

		int start_time, end_time;
		start_time = timing.time_in_microsec();
		radixsort(arr, N);
		end_time = timing.time_in_microsec();
		System.out.println(end_time - start_time);
	}
}
