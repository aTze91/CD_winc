# _CD REPORT_

##  **Three components of your solution:**
- **ssh :**  
 *ssh is an important tool in my implementation.It can give me acces  
to the Digital ocean droplet from both my local machine and github runners in relative security* 

- **Github actions :**  
*Github actions is a perfect tool to execute various tasks automatically, saving time and energy.  
The fact that I dont have to connect into my droplet every time I need to make a change in my  
code is a great deal*

- **sh script :**  
*I have used a .sh file to put together all the commands that my github action needed to execute  
in the droplet, even if in this case is not a complex script I believe this was the most easy  
and clean solution*

## **Three problems that I encountered along the way and how I solved them:** 
1. **Shh autentication :**  
*I have been stuck trying to connect the github runner and my droplet for a couple of days,  
not understanding why the droplet was refusing the connection.  
After reading documentations and different tutorials, I decided to ask help, finding that  
I wasn't using the full private key thinking that two of the lines were just comments and  
not part of the key. I learned that to ask for help sometimes is the best solution.  
You never know if you are just doing some kind of typo, and 4 eyes are always better than 2  
if you want to find it.*

2. **Understanding github runners :**  
 *While I was trying to fix problem 1, I encountered one more problem.  
 I could't reach the .ssh folder in my runner, my first thought was that ssh wasn't installed into  
 the runner but reading the documentation I discovered that the runner I was using has ssh installed   
 by default. I decided to run the command 'find .ssh' on the runner, discovering that .ssh is under  
  a different user that deny acces at the runner. The sulution was to create a new .shh directory   
  containing all the needed files into the runner home. Now I still don't know if that was the best solution,   
  but it worked out smoothly.*

3. **Executing commands on the droplet via github actions :**  
 *Solved problem 1 and 2, I was able to connect the runner to the droplet, but still I couldn't  
  execute any command on it, the solution was, passing  a .sh file containing all the commands   
  I wanted to execute in the droplet via shh.*


 