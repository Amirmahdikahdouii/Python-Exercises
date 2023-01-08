<pre>
Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal
representations contain only the lucky digits 4 and 7.
For Example numbers: 47, 477, 4 are lucky and 5, 17, 467 are not.
Unfortunately, not all numbers are lucky. Petya calls a number nearly lucky if the number of 
lucky digits in it is a lucky number.
Input:
    the only line contains an integer n (1 <= n < 10**18)
Output:
    Print on the single line "YES" if n is a nearly lucky number, otherwise, print "No"
</pre>
<h3>Example Input:</h3>
<pre>
    400447
</pre>
<h3>Example Output:</h3>
<pre>
    YES
</pre>
<i>Because Count of lucky number in 400447 is a lucky number also (4)!</i>
<hr>
<h3>Example Input:</h3>
<pre>
    7747774
</pre>
<h3>Example Output:</h3>
<pre>
    YES
</pre>
<hr>
<h3>Example Input:</h3>
<pre>
    1000000000000000000000000000
</pre>
<h3>Example Output:</h3>
<pre>
    NO
</pre>