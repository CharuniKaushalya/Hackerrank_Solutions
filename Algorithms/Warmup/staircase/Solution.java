package Hackerrank_Solutions.Algorithms.Warmup.staircase;

public class Solution {
    public static void main(String[] args) {
        int n = 6;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(i >= ((n-1)-j)){
                    System.out.printf("#");
                }else{
                    System.out.printf(" ");
                }
            }
            System.out.println("");
        }
    }



}
