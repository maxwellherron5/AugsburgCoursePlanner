package course;

import java.sql.*;
import java.util.ArrayList;
import java.sql.DriverManager;

import static course.CourseListTextScanner.ScanCourseList;

/**
 * This class is used for inserting all the course data that was interpolated into the CourseList structure to a
 * MySQL database
 * @author Maxwell Herron
 */
public class DatabaseInsert {

    public static void main(String[] args) {

        //This is the Courselist Object that contains all the course objects
        CourseList temp = new CourseList();
        //Populating the CourseList with course objects
        ScanCourseList(temp);

        //Converting temp to a java ArrayList object so that I can iterate through i
        ArrayList<Course> courseList;
        courseList = temp.getListOfCourses();

        //Attempting to push course objects to the MySQL database
        try {
            final String myDriver = "com.mysql.cj.jdbc.Driver";
            final String myUrl = "jdbc:mysql://localhost:3306/test_courses";
            Class.forName(myDriver);
            Connection conn = DriverManager.getConnection(myUrl, "", "");

            /**
             * This for each loop goes iterates through each course object in the courseList
             * and creates a query to be added to the course_table.
             * It then inserts each query and closes the connection when it is finished
             */
            for(Course course: courseList) {

                String prereqString = null;
                if (course.getPrereq() != null) {
                    prereqString = "";

                    for (int i = 0; i < course.getPrereq().length; i++) {
                        prereqString.concat(course.getPrereq()[i]);
                    }
                }

                String query = " insert into course_table(name, prereq, course_number, credits, description, department)" +
                        " values(?, ?, ?, ?, ?, ?)";

                PreparedStatement statement = conn.prepareStatement(query);
                statement.setString(1, course.getName());
                statement.setString(2, prereqString);
                statement.setString(3, course.getCoursenumber());
                statement.setInt(4, course.getCredits());
                statement.setString(5, course.getDescription());
                statement.setString(6, course.getDepartment());

                //Pushing the prepared statement to the table
                statement.execute();
            }

            System.out.println("Success!");
            conn.close();
        }

        //This will occur if the connection is unable to be established with the MySQL database
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}
