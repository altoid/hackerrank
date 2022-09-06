\W

use deutsch;

select
word
 from word
where left(word, 1) in ('a','e','i','o','u')
and
left(reverse(word), 1) in ('a','e','i','o','u')
;


