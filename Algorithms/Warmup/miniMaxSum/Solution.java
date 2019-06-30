package Hackerrank_Solutions.Algorithms.Warmup.miniMaxSum;

public class Solution {
    public static void main(String[] args) {
        int[] arr = new int[]{1,3,5,7,9};
        miniMaxSum(arr);
    }

    // Complete the miniMaxSum function below.
    static void miniMaxSum(int[] arr) {
        long min = Long.MAX_VALUE;
        long max = 0;
        long sum = 0;
        for(int i=0; i<5; i++)
        {
            long curr = arr[i];
            if(max < curr)
            {
                max = curr;
            }
            if(min > curr)
            {
                min = curr;
            }

            sum += curr;
        }
        long minSum = sum - max;//Removes the largest of the 5 numbers to get the min sum
        long maxSum = sum - min;//Removes the smallest of the 5 numbers to get the max sum
        System.out.println(minSum + " " + maxSum);

    }



}
