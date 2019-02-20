package course;

import java.io.*;
import java.util.*;


/**
 * This reads the input transcript .txt file and then outputs the relevant course information
 * into a .csv file to be used by the final comparison class
 */
public class TranscriptReader {

    public static void main(String[] args) throws Exception {

        final String inFile = "src/course/transcript.txt";

        ArrayList<String> courseList = transcriptRead(inFile);

        transcriptWrite(courseList);

    }

    public static ArrayList<String> transcriptRead(String inFile) {

        File inputFile = new File(inFile);

        ArrayList<String> courseList = new ArrayList<>();

        final String courseRegex = "[A-Z]{3}[0-9]{3}|[A-Z]{2}[0-9]{3}|[A-Z]{3}[0-9]{3}[A-Z]{2}|[A-Z]{3}[0-9]{4}[A-Z]{2}|[A-Z]{3}[0-9]{3}[L]{1}|[A-Z]{3}[0-9]{3}[P]{1}|[A-Z]{5}[0-9]{1}]";


        try {
            Scanner scan = new Scanner(inputFile);

            while(scan.hasNextLine()) {
                String temp = scan.nextLine();

                String[] tempTwo = temp.split("[\\s]+");
                for(int i = 0; i < tempTwo.length; i++) {
                    System.out.println("i is: " + tempTwo[i]);
                    if (tempTwo[i].matches(courseRegex)) {
                        courseList.add(tempTwo[i]);
                    }
                }
            }

        }
        catch (FileNotFoundException e) {
            System.out.println(e.getStackTrace());
        }



        return courseList;
    }

    public static void transcriptWrite(ArrayList<String> courseList) {

        //TODO fix pathing problem
        final String CSV_FILE_PATH = "output.csv"; //path to output file :)

        try {

            File file = new File(CSV_FILE_PATH);

            try{
                file.createNewFile();       //if file doesn't exist, create it
                System.out.println("File Created");
            }
            catch(IOException e){
                System.out.println("File Not Created");
            }



            FileWriter fr = new FileWriter(file);
            BufferedWriter br = new BufferedWriter(fr);

            //TODO fix inlist size
            for(String course : courseList) {
                br.write(course + ",");
                System.out.println("Wrote line");
            }

            br.close();
        }
        catch (IOException e) {
            System.out.println(e.getMessage());
        }

    }

}
