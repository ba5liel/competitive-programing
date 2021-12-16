/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package matrix;

import java.util.Random;

/**
 *
 * @author NATURE
 */
public class Matrix {

    /**
     * @param args the command line arguments
     */
   public static void main(String[] args){

		int[][]matrix = new int [4][4];
		
		for(int i=0; i<matrix.length; i++){

			for(int j=0; j<matrix[i].length; j++){

				matrix[i][j] = (int)(Math.random() * 2);
			}

		}

		for(int i=0; i<matrix.length; i++){

			for(int j=0; j<matrix[i].length; j++){

				System.out.print(matrix[i][j]);
			}

			System.out.println();
		}

		System.out.println("The largest row index: "+ largestRow(matrix));
		System.out.println("The largest column index: "+ largestColumn(matrix));
	}

	public static int largestRow(int[][] m) {

		int maxRowIndex = 0;
		int max = 0;

		for(int i=0; i<m.length; i++){

			int count=0;
			for(int j=0; j<m[i].length; j++){
				
				if(m[i][j] == 1)
					count++;
			}
			
			if(count > max){

					max = count;
					maxRowIndex = i;
				}
		}

		return maxRowIndex;
	}
	public static int largestColumn(int[][] m) {

		int maxColumnIndex = 0;
		int max = 0;

		for(int col=0; col<m[0].length; col++){

			int count=0;
			for(int row=0; row<m.length; row++){
				
				if(m[row][col] == 1)
					count++;
			}
			
			if(count > max){

					max = count;
					maxColumnIndex = col;
				}
		}

		return maxColumnIndex;
	}

}
