import java.util.*;

// ==================== Base Class ====================
class Account {
    private String accountNumber;
    private String ownerName;
    private double balance;

    // Constructor 1 (default)
    public Account() {
        this("0000", "Unknown", 0.0); // constructor chaining
    }

    // Constructor 2 (parameterized)
    public Account(String accountNumber, String ownerName, double balance) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        if (balance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative");
        }
        this.balance = balance;
    }

    // Getters and Setters (Encapsulation)
    public String getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    public double getBalance() {
        return balance;
    }

    protected void setBalance(double balance) {
        this.balance = balance;
    }

    // Deposit method
    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit must be positive");
        }
        balance += amount;
    }

    // Withdraw method
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdraw must be positive");
        }
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient balance");
        }
        balance -= amount;
    }

    // Display method
    public void display() {
        System.out.println("Account No: " + accountNumber);
        System.out.println("Owner: " + ownerName);
        System.out.println("Balance: " + balance);
    }
}

// ==================== Savings Account ====================
class SavingsAccount extends Account {
    private double interestRate;

    public SavingsAccount(String accNo, String name, double balance, double interestRate) {
        super(accNo, name, balance); // calling parent constructor
        this.interestRate = interestRate;
    }

    public double calculateInterest() {
        return getBalance() * interestRate / 100;
    }

    @Override
    public void display() {
        super.display(); // reuse parent display
        System.out.println("Interest Rate: " + interestRate + "%");
        System.out.println("Interest Amount: " + calculateInterest());
    }
}

// ==================== Current Account ====================
class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount(String accNo, String name, double balance, double overdraftLimit) {
        super(accNo, name, balance);
        this.overdraftLimit = overdraftLimit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdraw must be positive");
        }

        if (amount > getBalance() + overdraftLimit) {
            throw new IllegalArgumentException("Overdraft limit exceeded");
        }

        setBalance(getBalance() - amount);
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Overdraft Limit: " + overdraftLimit);
    }
}

// ==================== Main Class ====================
public class BankingSystem {
    public static void main(String[] args) {

        // Polymorphism: storing different accounts in same list
        List<Account> accounts = new ArrayList<>();

        accounts.add(new SavingsAccount("SA101", "Piyush", 1000, 5));
        accounts.add(new CurrentAccount("CA201", "Rahul", 2000, 1000));

        // Operations
        for (Account acc : accounts) {
            acc.deposit(500);

            try {
                acc.withdraw(1200);
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
            }

            System.out.println("\n--- Account Details ---");
            acc.display(); // polymorphic call
        }
    }
}