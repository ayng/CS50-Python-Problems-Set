
* Every try statement needs an except statement!*

Keyword	    Meaning	                            Common Saying
pass	    Do nothing, placeholder only	    🧘 “Do nothing and keep going”
continue	Skip to next loop cycle	            ⏩ “Skip this one, go to next”
break	    Exit the loop entirely	            🛑 “Stop the loop completely”
return	    Exit the current function	        🔚 “Stop and send back a result”

- pass 
- does nothing at all. It’s literally a placeholder.
Example:
for i in range(3):
    if i == 1:
        pass
    print(i)

Output:
0
1
2

- continue
- skip the rest of the current lopp and jump to the next one
Example:
for i in range(5):
    if i == 2:
        continue
    print(i)

Output:
0
1
3
4

- break
- completely stop the loop and exit it
Example:
for i in range(5):
    if i == 2:
        break
    print(i)

Output:
0
1

