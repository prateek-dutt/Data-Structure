import java.util.Scanner;

public class Sorting {
    
    public static int[] bubbleSort(int[] arr, int len)
    {
        int hold=0;
        int pass=0;
        boolean switched= true;
        while(pass<len-1 && switched==true)
        {
            switched = false;

            for(int j=0;j<len-pass-1;j++)
            {
                if(arr[j]>arr[j+1])
                {
                    switched = true;
                    hold=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=hold;
                }

            }
            pass++;

        }
        return arr;
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        int[] arr=new int[len];
        for(int i=0;i<len;i++)
        {
            arr[i]=sc.nextInt();
        }
        Sorting obj= new Sorting();
        int []s_arr=obj.bubbleSort(arr,len);
        for (int i : s_arr) {
            System.out.println(i);
        }
    }
}
