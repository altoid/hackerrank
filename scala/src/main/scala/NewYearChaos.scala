/*
traverse the list, looking at each item that is bigger than its array index.  if any of these differences
is greater than two, 'too chaotic.'  otherwise, min bribes is the sum of these differences.

 */
object NewYearChaos {
  def mininumBribes(q: Array[Int]): Unit = {
    println("============================== " + q.mkString(" "))

    // add 1 to each index
    val q_with_indices = q.zipWithIndex.map(t => (t._1, t._2 + 1)).toMap
    println(q_with_indices)
    val displacements = q_with_indices.map(t => (t._1, (t._1 - t._2) max 0))
    println(displacements.mkString(" "))

    // if displacement is positive, calculate the number of predecessors that come after it in the array.

    // for each number with a positive displacement, get its index.  then count the number of smaller numbers
    // with larger indices.
    val chaotic = displacements.find(_._2 > 2)
    chaotic match {
      case Some(_) => println("Too choatic")
      case None => {
        val e = for (d <- displacements if d._2 > 0) yield {
          println(s"number ${d._1}, displacement ${d._2}")
          val d_index = q_with_indices(d._1)
          val filtered = q_with_indices.filter(t => {
            t._1 < d._1 && t._2 > d_index
          })
          println(s"filtered = $filtered")
          filtered.size
        }
        println(e)
      }
    }
  }

  def main(args: Array[String]): Unit = {
    mininumBribes(Array(2,1,5,3,4)) // 3
    mininumBribes(Array(2,5,1,3,4)) // too chaotic

    mininumBribes(Array(1, 2, 5, 3, 7, 8, 6, 4)) // 7
  }
}
