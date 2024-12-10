# Bookstore Inventory Management

The Bookstore Inventory Management is a simple Java application that simulates an online bookstore using object-oriented programming. It allows users to purchase books, leave reviews, control inventory, and process payments. It only uses the Java standard library, so no external dependencies are required.

## Table of Contents

- [Bookstore Inventory Management](#bookstore_inventory_management)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Usage](#usage)

## Features

- **Inventory Management:** Admin can add and manage books in the inventory.
- **User Accounts:** Users can create accounts and log in.
- **Book Purchases:** Users can browse books and purchase them.
- **Order Management:** Orders are created for each user with details of their purchases.
- **Review System:** Users can leave reviews for books.
- **Average Ratings:** The application calculates and displays average ratings for books.
- **Payment Processing:** Users can process payments for their orders.

## Getting Started

To run the Bookstore Inventory Management, you need to have Java installed on your machine. Follow these steps to get started:

1. Navigate to the project directory:

```bash
cd bookstore_inventory_management/src/bookstore
```

2. Compile the Java source code:

```bash
javac *.java
```

3. Run the application:

```bash
java Bookstore
```

1. **Adding Books to Inventory:**
- Login as an admin with the username "admin" and password "admin123".
- Add books to the inventory.

2. **User Registration and Login:**
- Users can create accounts with unique usernames and passwords.
- Log in with your username and password to start shopping.

3. **Purchasing Books:**
- Browse the available books and select the ones you want to purchase.
- Complete the order to finalize your purchase.

4. **Leaving Reviews:**
- After purchasing a book, you can leave a review and rate it.

5. **Viewing Average Ratings:**
- The application calculates and displays average ratings for each book.

6. **Payment Processing:**
- Users can process payments for their orders, and the application rounds payment amounts to two decimal places.
