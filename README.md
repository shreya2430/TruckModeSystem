# Vehicle Truck Record System

## Overview
The Vehicle Truck Record System is designed to manage and track truck entries and exits at a warehouse. Each truck has a unique identifier and a counter that keeps track of how many times it enters or leaves the warehouse. The system helps the warehouse manager track the number and status of open and closed orders and identify which trucks have reached their delivery limit for the day.

## Key Features
- **Track truck entries and exits**: Records the unique truck IDs and maintains a counter to reflect the number of times a truck enters or exits.
- **Open and closed order tracking**: Determines the current state of a truck's order based on its counter.
- **Truck availability**: Identifies trucks that are currently available for deliveries.
- **High-frequency truck identification**: Lists trucks that have moved in/out of the warehouse more than a specified number of times.
- **Maximum delivery check**: Lists trucks that have completed their maximum number of deliveries for the day.
- **BST-based data structure**: Utilizes a Binary Search Tree (BST) for efficient data storage and retrieval.

## Classes and Methods
### `TruckNode`
- Represents a unique truck with properties:
  - `Uid`: Unique Truck ID
  - `chkoutCtr`: Counter to track the number of entries and exits

### `BSTNode` (inherits from `TruckNode`)
- Manages the warehouse operations using a BST structure.
- **Key Methods**:
  - `_readTruckRec(Uid)`: Reads and inserts truck IDs into the BST and updates the counter.
  - `_checkTruckRec(Uid)`: Checks the status of a specific truck.
  - `_printTruckRec(Uids)`: Prints the list of truck IDs and their counters.
  - `_updateTruckRec(Uid)`: Updates the BST with a new truck entry or increments the counter of an existing truck.
  - `calculateSum()`: Calculates the sum of open and closed orders.
  - `_printOrderStatus(targetorders)`: Prints the number of open, closed, and yet-to-be-fulfilled orders.
  - `_highFreqTrucks_Uids(frequency, Uids)`: Identifies trucks that moved more than a specified frequency.
  - `_maxDeliveries(Uids)`: Lists trucks that completed their maximum deliveries.
  - `_availTrucks(Uids)`: Lists trucks currently available for deliveries.

## System Design
The data structure is implemented using a Binary Search Tree (BST) to allow efficient traversal and data insertion. The BST structure supports recursive traversal and performs insertion and updates without using external libraries.

### Complexity Analysis
- **Insertion/Search**:
  - Average case: `O(log n)`
  - Worst case (degenerated tree): `O(n)`
- **Traversal**:
  - `O(n)` for in-order traversal

## Input/Output
- **Input Files**:
  - `inputPS2.txt`: Contains truck IDs for initial data loading.
  - `promptsPS2.txt`: Contains instructions for operations like status checks and updates.
- **Output**:
  - `outputPS2.txt`: Records the results of operations as specified.

## Running the Program
To execute the program, run the `main()` function, which reads inputs from `inputPS2.txt` and processes prompts from `promptsPS2.txt`.

## Example Operations
- **Read and insert trucks**:
  ```python
  bst._readTruckRec(101)
