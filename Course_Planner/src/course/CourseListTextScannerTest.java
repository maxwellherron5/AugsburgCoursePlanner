package course;

import org.junit.Test;

import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class CourseListTextScannerTest {


    /**
     * This test will read in input from a text file that is formatted well. If it passes, that means our
     * CourseListTextScanner is reading in classes correctly.
     */
    @Test
    public void testAddListOfCourseGood(){

        //This try catch is for the scanner because the file can potentially not be found
        try {
            File file = new File("TestingTextFiles/AddListOfCourseGood.txt");       //File containing good text to read in
            Scanner scanner = new Scanner(file);
            CourseList clts = new CourseList(true);                //although sloppy, a bool in the constructor calls the empty constructor
            CourseListTextScanner.AddListOfCourse(scanner, clts);
            String expected = "Introduction to Financial Accounting, Introduction to Managerial Accounting, Topics";
            String actual = "";                                         //actual string

            for(int i = 0; i < clts.listOfCourses.size(); i++){         //for every couse in the list of courses
                actual += clts.listOfCourses.get(i).getName();          //append the name of the course
                if(i + 1 != clts.listOfCourses.size()){                 //if NOT the last course in the listOfCourses
                    actual += ", ";                                     //append this
                }
            }
            assertEquals(expected, actual);                             //Assert the test
        }
        catch(FileNotFoundException e){
            System.out.println("TestingTextFiles/AddListOfCourseGood.txt not found! Scanner can't be made for test");
        }

    }

    /**
     * This test will try and scan a course list of a bad text file. It should fail. This test will only pass
     * if the NumberFormatException is thrown.
     */
    @Test(expected = NumberFormatException.class)
    public void testAddListOfCourseBad(){

        //This try catch is for the scanner because the file can potentially not be found
        try {
            File file = new File("TestingTextFiles/AddListOfCourseBad.txt");    //File containing good text to read in
            Scanner scanner = new Scanner(file);
            CourseList clts = new CourseList(true);          //although sloppy, a bool in the constructor calls the empty constructor
            CourseListTextScanner.AddListOfCourse(scanner, clts);

        }
        catch(FileNotFoundException e){
            System.out.println("TestingTextFiles/AddListOfCourseGood.txt not found! Scanner can't be made for test");
        }

    }



}
