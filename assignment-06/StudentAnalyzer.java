import java.util.*;
import java.util.stream.*;

class Student {
    int id;
    String name;
    List<String> courses;
    Map<String, Integer> scores;

    Student(int id, String name, List<String> courses, Map<String, Integer> scores) {
        this.id = id;
        this.name = name;
        this.courses = courses;
        this.scores = scores;
    }

    double getAverageScore() {
        return scores.values()
                .stream()
                .mapToInt(Integer::intValue)
                .average()
                .orElse(0.0);
    }
}

public class StudentAnalyzer {

    public static List<Student> getTopNStudents(List<Student> students, int n) {
        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getAverageScore).reversed())
                .limit(n)
                .toList();
    }

    public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {

        Map<String, List<Integer>> courseMarks = new HashMap<>();

        for (Student s : students) {
            for (String course : s.courses) {
                int score = s.scores.getOrDefault(course, 0);
                courseMarks.computeIfAbsent(course, k -> new ArrayList<>()).add(score);
            }
        }

        Map<String, Double> avgMap = new HashMap<>();

        for (String course : courseMarks.keySet()) {
            double avg = courseMarks.get(course)
                    .stream()
                    .mapToInt(Integer::intValue)
                    .average()
                    .orElse(0.0);

            avgMap.put(course, avg);
        }

        return avgMap;
    }

    public static Set<String> getAllUniqueCourses(List<Student> students) {

        Set<String> uniqueCourses = new HashSet<>();

        for (Student s : students) {
            uniqueCourses.addAll(s.courses);
        }

        return uniqueCourses;
    }

    public static void main(String[] args) {

        List<Student> students = new ArrayList<>();

        Map<String,Integer> s1 = new HashMap<>();
        s1.put("Math",85);
        s1.put("Java",90);

        Map<String,Integer> s2 = new HashMap<>();
        s2.put("Math",80);
        s2.put("Java",70);
        s2.put("DBMS",75);

        Map<String,Integer> s3 = new HashMap<>();
        s3.put("Math",95);
        s3.put("Java",88);

        students.add(new Student(51,"Piyush",Arrays.asList("Math","Java"),s1));
        students.add(new Student(52,"Rahul",Arrays.asList("Math","Java","DBMS"),s2));
        students.add(new Student(53,"Aman",Arrays.asList("Math","Java"),s3));

        int inputSize = students.size();

        // Start execution time
        long startTime = System.nanoTime();

        List<Student> topStudents = getTopNStudents(students,2);
        Map<String,Double> courseAvg = getAverageScorePerCourse(students);
        Set<String> uniqueCourses = getAllUniqueCourses(students);

        long endTime = System.nanoTime();
        long executionTime = endTime - startTime;

        // -------- Output Section --------

        System.out.println("Input Size (n): " + inputSize);
        System.out.println("Execution Time : " + executionTime + " nanoseconds");

        System.out.println("\nTop Students:");
        for(Student s : topStudents){
            System.out.println(s.name + " Avg Score: " + s.getAverageScore());
        }

        System.out.println("\nAverage Score Per Course:");
        for(String c : courseAvg.keySet()){
            System.out.println(c + " : " + courseAvg.get(c));
        }

        System.out.println("\nAll Unique Courses:");
        for(String c : uniqueCourses){
            System.out.println(c);
        }

        System.out.println("\nWhere:");
        System.out.println("n = number of students (input size)");
        System.out.println("m = average number of courses per student");

        System.out.println("\nTime Complexity Analysis:");
        System.out.println("1. Computing Course Averages : O(n * m)");
        System.out.println("2. Sorting Top N Students    : O(n log n)");
    }
}