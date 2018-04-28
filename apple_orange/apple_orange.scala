// https://www.hackerrank.com/challenges/apple-and-orange/problem

// problem statement implies that b is always to the right of a and
// the house is always between them.

import io._

object Solution {

    def countApplesAndOranges(s: Int, t: Int, larry_pos: Int, rob_pos: Int,
                              apple_distances: Array[Int], orange_distances: Array[Int]) {
        val apple_hits = apple_distances.map(x => x + larry_pos).filter(x => x >= s && x <= t).length
        val orange_hits = orange_distances.map(x => x + rob_pos).filter(x => x >= s && x <= t).length

        println(s"$apple_hits")
        println(s"$orange_hits")
		// the problem statement said output should be two space-separated integers on a line.
		// their checker expects the values on separate lines.  fuckers.
    }

	val lines = Source.stdin.getLines
    val house = lines.next.split("\\s+").map(x => x.toInt).toList
    val positions = lines.next.split("\\s+").map(x => x.toInt).toList
    val apples_oranges = lines.next.split("\\s+").map(x => x.toInt).toList  // unused
    val apple_distances = lines.next.split("\\s+").map(x => x.toInt).toArray
    val orange_distances = lines.next.split("\\s+").map(x => x.toInt).toArray
    
    val larry_pos = positions(0)
    val rob_pos = positions(1)
    
//    println(s"larry:  $larry_pos")
//    println(s"rob:  $rob_pos")
//    println(s"house:  $house")
//    println(s"apple_distances:  $apple_distances")
//    println(s"orange_distances:  $orange_distances")

    countApplesAndOranges(house(0), house(1), larry_pos, rob_pos, apple_distances, orange_distances)
}
