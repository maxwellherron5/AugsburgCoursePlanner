package course;

/**
 * This class represents a course at Augsburg University. It's attributes describe one of these courses.
 */
public class Course {

    String name = "";                    //Name of course
    int credits;                    //Number of credits for the course
    String[] prereq;                //List of prereqs for the course
    String prereqIn = "";                //Input of prereq from file
    String coursenumber = "";            //Course number
    Enum OfferedIn;                   //Semesters class is offered- Spring Summer Fall...
    String description = "";             //Description of the course
    String department = "";              //What department the course is a part of
    String coreCurriculum = "";

    /** Constructors */
    public Course(String name, int credits, String[] prereq, String coursenumber, Enum offeredIn, String description, String department) {
        this.name = name;
        this.credits = credits;
        this.prereq = prereq;
        this.coursenumber = coursenumber;
        OfferedIn = offeredIn;
        this.description = description;
        this.department = department;
    }

    public Course(String name, String coursenumber, String description, String[] prereq, int credits){

    }

    public Course(){

    }

    /** Getters*/
    public String getName() {
        return name;
    }

    public int getCredits() {
        return credits;
    }

    public String[] getPrereq() {
        return prereq;
    }

    public String getCoursenumber() {
        return coursenumber;
    }

    public Enum getOfferedIn() {
        return OfferedIn;
    }

    public String getDescription() {
        return description;
    }

    public String getDepartment() {
        return department;
    }

    /**
     * Setter for Enum Only
     */
    public void setOfferedIn(Enum offeredIn) {
        OfferedIn = offeredIn;
    }

    /**
     * These enums are used by the Course object to specify what semesters the course is offered.
     */
    private enum OfferedIn {

        SPRING, SUMMER, FALL, ALL, FALLANDSPRING

    }

}
