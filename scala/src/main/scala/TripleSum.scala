object TripleSum {
  /*
  strategy - sort each array (problem does not say whether the arrays are sorted)
  then
  for each q in b
  find the number of elements in a that is <= q
  find the number of elements in c that is <= q
  multiply these together

  add these all up
   */

  def countLessThanOrEqual(a: Array[Int], target: Int): Long = {
    // find the index of the rightmost element in a that is <= target
    /*
    look at the middle.  if a(m) > target then look at left side
     */

    def helper(from: Int, to: Int): Option[Int] = {
      if (to < from) {
        None
      }
      else {
        val m = (from + to) / 2

        if (a(m) <= target) {
          // there might be an element to the right of a(m) that still meets the criterion
          val result = Some(m)
          val hedge = helper(m + 1, to)
          hedge match {
            case None => result
            case Some(h) => hedge
          }
        }
        else {
          // a(m) > target, look in the left side
          helper(from, m - 1)
        }
      }
    }

    val result = helper(0, a.length - 1)
    result match {
      case Some(x) => x + 1
      case None => 0
    }
  }

  def triplets(a: Array[Int], b: Array[Int], c: Array[Int]): Long = {
    val a_cleaned = a.toSet.toArray.sorted
    val b_cleaned = b.toSet.toArray.sorted
    val c_cleaned = c.toSet.toArray.sorted

    val x: Array[Long] = b_cleaned.map(countLessThanOrEqual(a_cleaned, _))
    println(x.mkString(" "))

    val y: Array[Long] = b_cleaned.map(countLessThanOrEqual(c_cleaned, _))
    println(y.mkString(" "))

//    (x, y).zipped.map(_ * _).sum

    val z: Array[Long] = (x, y).zipped.map(_ * _)
    println((x zip y).mkString(" "))
    println(z.mkString(" "))
    println(z.sum)
    z.sum
  }
}