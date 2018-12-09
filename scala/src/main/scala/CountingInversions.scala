import scala.collection.mutable

object CountingInversions {
  def countInversions(ints: Array[Int]): Long = {
    // traverse the array, keeping track of the counts of each value.
    val valCounts = mutable.HashMap[Int, Int]()

    for (i <- ints) {
      if (!(valCounts contains i)) {
        valCounts(i) = 0
      }
      valCounts(i) += 1
    }

    println(valCounts.mkString(" "))
    // use that data to compute the first position of each unique value in the
    // sorted array

    val keez = valCounts.keys.toArray.sorted
    println(keez.mkString(" "))

    val valPositions = mutable.HashMap[Int, Int]()

    var currentPos = 0
    for (k <- keez) {
      valPositions(k) = currentPos
      currentPos += valCounts(k)
    }

    println(valPositions.mkString(" "))

    val visited = Array.fill[Boolean](ints.length)(false)
    var swapCount = 0

    // get first unvisited position
    var nextUnvisited = visited.indexOf(false)
    while (nextUnvisited != -1) {
      visited(nextUnvisited) = true
      var whatValue = ints(nextUnvisited)
      var whatValueFinalPos = valPositions(whatValue)
      while (whatValueFinalPos != nextUnvisited) {
        swapCount += 1
        visited(whatValueFinalPos) = true
        valPositions(whatValue) += 1
        whatValue = ints(whatValueFinalPos)
        whatValueFinalPos = valPositions(whatValue)
      }
      nextUnvisited = visited.indexOf(false)
    }
    swapCount
  }

  def main(args: Array[String]): Unit = {
    println(countInversions(Array(2,1,3,1,2)))
  }
}
