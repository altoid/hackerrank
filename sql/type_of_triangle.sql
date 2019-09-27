use hackerrank;

select
case
when a + b <= c then 'not a triangle'
when b + c <= a then 'not a triangle'
when c + a <= b then 'not a triangle'
when a = c and a = b then 'equilateral'
when a = b or a = c or b = c then 'isoceles'
else 'scalene'
end ttype, a, b, c
from triangle
;
