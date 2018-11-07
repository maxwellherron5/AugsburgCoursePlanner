package course;

import org.junit.Test;
import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class CourseListTest {



    @Test
    public void testSearchByCourseName(){

        Course course = new Course();
        course.name = "ACC221";

        CourseList courseList = new CourseList();
        System.out.println(courseList.SearchByCourseName("ACC221"));

    }


}
