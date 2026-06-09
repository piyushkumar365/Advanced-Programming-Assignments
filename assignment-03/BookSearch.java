import java.util.ArrayList;
import java.util.Scanner;

public class BookSearch {
    public static void main(String[] args) {

        // Create ArrayList to store book titles
        ArrayList<String> books = new ArrayList<>();

        // Add at least 5 book titles
        books.add("Introduction to Algorithms");
        books.add("Operating System Concepts");
        books.add("Database Management Systems");
        books.add("Computer Networks");
        books.add("Clean Code");

        // Take search word from user
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter word to search in book titles: ");
        String searchWord = sc.nextLine().toLowerCase();

        System.out.println("\nBooks containing \"" + searchWord + "\":");

        boolean found = false;

        // Search for books containing the word
        for (String book : books) {
            if (book.toLowerCase().contains(searchWord)) {
                System.out.println(book);
                found = true;
            }
        }

        if (!found) {
            System.out.println("No matching books found.");
        }

        sc.close();
    }
}
