# gotox
# added prototype gotox interpreter



this is a small project for a interpreter library for a non programing language logical code
I made this logical code specification myself and it is intended for hobbyists

gotox is a code intednde for hobbyist neural network experimentation
the code itself serves as a logical framework for converting inputs to outputs folloing ceartain rules

this is made by a high school kid so dont take it too seriously
 i'm new to github
 THIS INTERPRETER DOSE NOT CURRENTLY MEET THE SPECIFICATION AND IS UNNFINNISHED
<h1>gotox specification:</h1>
 gotox is a logical code for converting inputs to outputs. It was made with the intention of hobbyist nural network experimentation and use. 
 
inputs are changed to ouputs dependent on a logical code entered into the interpreter
the logical code entered follows this format

the logical code itself is devided into cells each cell contains 6 values
note: all values are numeric with the ecception of output that may be of any type
1. var_write
2. var_read
3. var_cond
4. var_A
5. var_B
6. output

some other things that are essintial to the specification:
1. there is a action quene that actions can be sent to
2. there is a memory array that values are stored in
  its default is [1,2,3,4,1,2,3,4,1,2,3,4,.... continiung for the decided length of the momory array
2.there is an output quene that functions identicaly to the acction quene


order of operations
1. all inputs are sent to the top of the action quene as cell values

2. the bottom of the action que is called

3. the following operations happen to the cell that was called

a. if it has an output then send the output to the top of the output quene

b. sets value at the position in the memory array specified by var_write of the cell to

   value at the position in the memory array specified by var_read of the cell
   
c. next send sometiong to actionq dependent on the value at the memory position specified by the cell's var_cond

   if the memory reads 0 then it sends var_A of the cell to the action quene
   
   if the memory reads 1 then it sends var_B of the cell to the action quene
   if 2 then it sends both
   
   if three then sends none
   
4. waits to let host program send input and collect output

5. loops back to step two and continues untill host program stops it
