import java.util.Scanner;
import java.io.Console;


public class Main{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String sentence = sc.nextLine();
       ntence, " ");
        int word_count=0;
        int key;
        System.out.println("Enter the key value:");
        key=sc.nextInt();
        while (tk.hasMoreTokens()) {
            String token = tk.nextToken();
            word_count += 1;
            if (word_count % 2 != 0) {
                System.out.print(" ");
                for(int i=0;i<token.length();i++){
                   char c =(char)(token.charAt(i)+key);
                    System.out.print(c);
                }
            }else{
                System.out.print(" ");
                StringBuffer temp_token=new StringBuffer(token);
                temp_token.reverse();
                token=temp_token.toString();
                for(int i=0;i<token.length();i++){
                    char c =(char)(token.charAt(i)+key);
                    System.out.print(c);
                }
            }
        }
    }
}