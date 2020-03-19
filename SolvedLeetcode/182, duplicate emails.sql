/* Write a SQL query to find all duplicate emails in a table named Person.

# Write your MySQL query statement below */
select Email 
from Person
GROUP BY Email 
HAVING COUNT(*)> 1;