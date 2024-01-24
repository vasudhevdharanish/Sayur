import java.util.Scanner;
import java.util.StringTokenizer;
//Problem 2
public class Exercise {
        public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            String sentence = sc.nextLine();
            int word_count=0;
            String[] words=sentence.toLowerCase().split(" ");
            for(int i=0;i<words.length-2;i++){
                if(words[i].equals("the") && words[i+1].equals("a") && words[i+2].equals("the")){
                    word_count+=1;
                }
            }
            System.out.print(word_count);
        }
}
