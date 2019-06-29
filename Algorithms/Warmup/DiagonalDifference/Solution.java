package Algorithms.Warmup.DiagonalDifference;

import java.util.ArrayList;
import java.util.List;

public class Solution {

    public static void main(String[] args) {
        int n = 3;

        // Here aList is an ArrayList of ArrayLists
        List<List<Integer> > aList =
                new ArrayList<>(n);

        // Create n lists one by one and append to the
        // master list (ArrayList of ArrayList)
        ArrayList<Integer> a1 = new ArrayList<Integer>();
        a1.add(1);
        a1.add(2);
        a1.add(3);
        aList.add(a1);

        ArrayList<Integer> a2 = new ArrayList<Integer>();
        a2.add(4);
        a2.add(5);
        a2.add(6);
        aList.add(a2);

        ArrayList<Integer> a3 = new ArrayList<Integer>();
        a3.add(9);
        a3.add(8);
        a3.add(9);
        aList.add(a3);
        int result = diagonalDifference(aList);
        System.out.printf(String.valueOf(result));
    }
    /*
     * Complete the 'diagonalDifference' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY arr as parameter.
     */

    private static int diagonalDifference(List<List<Integer>> aList) {
        // Write your code here
        int leftDiagonal, rightDiagonal;
        leftDiagonal = rightDiagonal= 0;

        for (int i = 0; i < aList.size(); i++) {
            leftDiagonal += aList.get(i).get(i);
            rightDiagonal += aList.get(i).get((aList.size()-1)-i);
        }
        return Math.abs(leftDiagonal-rightDiagonal);

    }
}
