/*
traverse the list, looking at each item that is bigger than its array index.  if any of these differences
is greater than two, 'too chaotic.'  otherwise, min bribes is the sum of these differences.

 */
object NewYearChaos {
  def minimumBribes(q: Array[Int]): Unit = {
    println("============================== " + q.mkString(" "))

    // add 1 to each index
    var q_with_indices = q.zipWithIndex.map(t => (t._1, t._2 + 1))
    println(q_with_indices.mkString(" "))
    val q_with_indices_map = q_with_indices.toMap
    val displacements = q_with_indices.map(t => (t._1, (t._1 - t._2)))
    println(displacements.mkString(" "))

    var upto: Option[Int] = None

    for (i <- 0 until displacements.length - 1) {
      if (displacements(i)._2 > displacements(i + 1)._2) {
        upto = Some(i + 1)
      }
    }

    // we don't need to look at every number.  we can stop looking when we know the rest of the array is sorted.
    // this is true when the displacements do not decrease.  so we look for a nondecreasing subarray of displacements
    // that continues to the end.

    upto match {
      case None => {
        println("the whole list is sorted")
        q_with_indices = Array[(Int, Int)]()
      }
      case Some(p) => {
        println(s"upto: ${p}")
        q_with_indices = q_with_indices.take(p)
      }
    }

    println(q_with_indices.mkString(" "))
    // for each number, get its index.  then count the number of smaller numbers
    // with larger indices.
    val chaotic = displacements.find(_._2 > 2)
    chaotic match {
      case Some(_) => println("Too chaotic")
      case None => {
        val e = for (d <- q_with_indices) yield {
          // println(s"number ${d._1}, displacement ${d._2}")
          val filtered = q_with_indices_map.filter(t => {
            t._1 < d._1 && t._2 > d._2
          })
          println("filtered: " + filtered.mkString(" "))
          filtered.size
        }
        println(e.sum)
      }
    }

  }

  def main(args: Array[String]): Unit = {
    minimumBribes(Array(2,1,5,3,4)) // 3
    minimumBribes(Array(2,5,1,3,4)) // too chaotic

    minimumBribes(Array(1, 2, 5, 3, 7, 8, 6, 4)) // 7
  }
}
