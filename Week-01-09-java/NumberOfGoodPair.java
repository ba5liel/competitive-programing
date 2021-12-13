/**
 *
 * @author Basliel
 */
public class NumberOfGoodPair {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    
        System.out.println(getNumberOfGoodPair(new int[] {1,2,1,1,2,2}));
    }

    public static int getNumberOfGoodPair(int[] A) {
        int count[] = new int[101];
        int result = 0;
        for (int a : A) {
           result = result + count[a]++;
           System.out.println(String.format("new result %s",result));
        }
        return result;
    }

}