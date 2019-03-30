/*

a ^ b == 0  iff  a == 0
otherwise 1

so we eliminate quadruples where all elements are same.

for 3000, 3000, 3000, 3000

there are 3000 non-beautiful quads

and 3000 ** 4 - 3000 beautiful quads

but now we have to eliminate dups

how many quads have unique numbers?   C(3000, 4)
how many have 2 the same?  C(3000, 3)
3 the same?  C(3000, 2)
4 the same?  C(3000, 1)


for 2000, 2400, 2700, 3000

4 the same?  C(min(w x y z), 4)

4 unique?  2000 * 2399 * 2698 * 2997 / 4!

3 the same?
    odd column is 2000:  C(2000, 2) + 2000 * 400
    odd column is 2400:  C(2000, 2) + 2000 * 400
    odd column is 2700:  C(2000, 2) + 2000 * 700
    odd column is 3000:  C(2000, 2) * 2000 * 1000

2 the same?


 */
object BeautifulQuadruples {

}
