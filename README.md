# Order

A program that prompts the user to place an order and provides the total bill upon each addition of items from the menu.


## Implementation

In a file called `order.py`, there's a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, the program displays the total cost of all items inputted thus far, prefixed with a dollar sign (`$`) and formatted to two decimal places. It also treats the user’s input case insensitively. Ignoring any input that isn’t an item. The program assumes that every item on the menu will be `titlecased`.
## Usage/Examples



```
$ python taqueria.py                                                            
Item: burrito                                                                   
Total: $7.50                                                                    
Item: large quesadilla                                                          
Item: super quesadilla                                                          
Total: $17.00                                                                   
Item:                                                                           
$ 
```

```
$ python taqueria.py                                                            
Item: nachos                                                                    
Total: $11.00                                                                   
Item: taco                                                                      
Total: $14.00                                                                   
Item: taco                                                                      
Total: $17.00                                                                   
Item: taco                                                                      
Total: $20.00                                                                   
Item:                                                                           
$                                                                               
```

