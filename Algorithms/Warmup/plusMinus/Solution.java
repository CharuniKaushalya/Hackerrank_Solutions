package Hackerrank_Solutions.Algorithms.Warmup.plusMinus;

public class Solution {
    public static void main(String[] args) {

        int[] array = new int[]{1,1,0,-1,-1};
        plusMinus(array);
    }

    // Complete the plusMinus function below.
    static void plusMinus(int[] array) {
        int postiveCount, negativeCount, zeroCount;
        postiveCount= negativeCount = zeroCount = 0;
        for (int i = 0; i < array.length; i++) {
            if(array[i]>0){
                postiveCount++;
            }
            if(array[i]<0){
                negativeCount++;
            }
            if(array[i]==0){
                zeroCount++;
            }
        }
        System.out.println( (double)postiveCount/array.length);
        System.out.println( (double)negativeCount/array.length);
        System.out.println((double)zeroCount/array.length);


    }

}
