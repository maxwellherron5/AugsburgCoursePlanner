package course;

import java.util.ArrayList;

/**
 * This class is a course list of all courses at augsburg.
 */
public class CourseList {

    ArrayList<Course> listOfCourses = new ArrayList<>();                                //Entire list of courses offered at Augsburg
    ArrayList<String> listOfDepartmentNames = new ArrayList<>();                        //Entire list of departments at Augsburg

    /**Constructors */
    public CourseList(){
        CourseListTextScanner.ScanCourseList(this);                                     //Populates course list with course list and list of departments
    }

    /**
     * . Empty constructor for testing
     * @param test if a boolean is sent, this constructor is run
     */
    public CourseList(boolean test){

    }

    /**Getters*/
    public ArrayList<Course> getListOfCourses(){
        return this.listOfCourses;
    }

    public ArrayList<String> getListOfDepNames(){
        return this.listOfDepartmentNames;
    }

    /**
     * This method adds a course to the array list "listOfCourses"
     * @param course course to add to list of courses
     */
    public void addToCourses(Course course){
        this.listOfCourses.add(course);
    }

    /**
     * This method adds a course to the array list "listOfDepartments"
     * @param department department to add to list of department
     */
    public void addToDepartment(String department){ this.listOfDepartmentNames.add(department); }

    /**@author Beteab Gebru
     * This method takes in a string(name) of a course and returns the index to the object if found in search
     * @param NameOfCoursetoSearch: string name of course will be passed to search array_list of courses
     *@return integer index  to an array element 
     */
    public int SearchByCourseName(String NameOfCoursetoSearch) {

        boolean found = false;
        int index = 0;
        int x = 0;

        while(!found || index < listOfCourses.size()){

            if (listOfCourses.get(x).getName().equals(NameOfCoursetoSearch)){
                found = true;
            }
            index++;
        }

        if(found)
            return index;//returns a course object found
        else
            return -1;//indicating not found
    }

}


