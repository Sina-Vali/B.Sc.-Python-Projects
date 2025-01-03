# Problem Statement
The Bank of Montreal, Canada, maintains a sorted list of all its customers, which is constantly being updated. 
If a person has previously opened an account with the bank and now applies for a new account, their name will already be in the list. 
However, if someone is opening an account for the first time, their name must be added to the list in the correct position to maintain the sorted order.

Until now, the bank has been using linear search to locate names and manage the list. 
However, as the number of customers grows daily, linear search has become a very time-consuming operation. 
Since the list is already sorted, binary search offers a more efficient approach to solve the problem.
The bank's manager has requested a program that leverages binary search to optimize the process of adding and managing customer names in the list.

## Input
The first line contains an integer $m$ and a string $n$, separated by a space. Here:
$m$ represents the number of current customers of the bank.
$n$ is the name of the customer whose presence in the list needs to be checked.
The next m lines contain the names of the customers, provided in sorted order.

**Note:** The maximum length of each customer name is 15 characters.

$1<=m<=55555$

## Output
If the current client's name is in the list, return their index inside the list. Otherwise:
- If their name is smaller than the first element of the list, return $-1$;
- If their name is bigger than the last element, return the index of the last element;
- Else, return the index of the largest name that is smaller than the current client's name.


