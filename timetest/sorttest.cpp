#include<iostream>

using namespace std;

int partition(int list[], int low, int high);
void quicksort(int list[], int low, int high);

void merge(int list[], int first, int mid, int last);
void mergesort(int list[], int fisrt, int last);

void heapsort(int list[]);
void heapify(int list[], int n, int i);
void swap(int list[], int a, int b);

int arr[] = {3,5,7,8,4,3,3,6,7,89,34,23,4,2};

int main(){

  // bubble sort 

  // for(int i = 0; i < 14; ++i){
  //   for(int j = 0; j < 14-i; ++j){
  //     if(arr[j] < arr[j-1]){
  //       int tmp = arr[j];
  //       arr[j] = arr[j-1];
  //       arr[j-1] = tmp;
  //     }
  //   }
  // }
  

  // insertion sort

  // for(int i = 1; i < 14; ++i){
  //   int key = arr[i];
  //   int j = i - 1;
  //   while(j >= 0 && arr[j] > key){
  //     arr[j+1] = arr[j];
  //     arr[j] = key;
  //     --j;
  //   }
  // }


  // selection sort

  // for(int i = 0; i < 14; ++i){
  //   int smallest = i;
  //   for(int j = i+1; j < 14; ++j){
  //     if(arr[smallest] > arr[j]){
  //       smallest = j;
  //     } 
  //   }
  //   int tmp = arr[i];
  //   arr[i] = arr[smallest];
  //   arr[smallest] = tmp;
  // }

  
  //quick sort

  // quicksort(arr, 0, 13);


  //merge sort

  // mergesort(arr, 0, 13);


  //heap sort

  heapsort(arr);


  for(int i = 0; i < 14; ++i){
    cout << arr[i] << ' ';
  }

}

void quicksort(int list[], int low, int high){

  if(high > low){
    int pivot =  partition(list, low, high);
    quicksort(list, low, pivot-1);
    quicksort(list, pivot+1, high);
  }
}

int partition(int list[], int low, int high){
  int left = low, right = high;
  int pivot_element = list[left];
  while(left < right){
    while(list[left] <= pivot_element) left++;
    while(list[right] > pivot_element) right--;
    if(left < right){
      int tmp = list[left];
      list[left] = list[right]; 
      list[right] = tmp; 
    }
  }
  list[low] = list[right];
  list[right] = pivot_element;
  return right;
}

void mergesort(int list[], int first, int last){
  if(first < last){
    int mid = (first+last)/2;
    mergesort(list, first, mid);
    mergesort(list, mid+1, last);
    merge(list, first, mid, last);
  }
}

void merge(int list[], int first, int mid, int last){
  int i = first, j = mid+1, k = first;
  int sortlist[14] = {};

  while (i <= mid && j <= last){
    if(list[i] <= list[j]) sortlist[k++] = list[i++];
    else sortlist[k++] = list[j++];
  }

  if(i > mid){
    for(int w = j; w <= last; ++w){
      sortlist[k++] = list[w];
    }
  }
  else{
    for(int w = i; w <= mid; ++w){
      sortlist[k++] = list[w];
    }
  }

  for(int w = first; w <= last; ++w){
    list[w] = sortlist[w];
  }
 
}

void heapsort(int list[]){
  int n = 14;

  for(int i = n/2 - 1; i >= 0; --i){
    heapify(arr, n, i);
  }

  for(int i = n - 1; i > 0; --i){
    swap(list, 0, i);
    heapify(list, i, 0);
  }
}

void heapify(int list[], int n, int i){
  int p = i;
  int l = i*2 + 1;
  int r = i*2 + 2;
  
  if(l < n && list[p] < list[l]){
    p = l;
  }

  if(r < n && list[p] < list[r]){
    p = r;
  }

  if(i != p){
    swap(list, p, i);
    heapify(list, n, p);
  }
}

void swap(int list[], int a, int b){
  int tmp = list[a];
  list[a] = list[b];
  list[b] = tmp;
}