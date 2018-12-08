import scala.collection.mutable

/*
traverse the list, looking at each item that is bigger than its array index.  if any of these differences
is greater than two, 'too chaotic.'  otherwise, min bribes is the sum of these differences.

 */
object NewYearChaos {
  def minimumBribes(q: Array[Int]): Unit = {
    // we can do this in linear time.  we march through the array, keeping track of all of the possible legal values
    // that may be in each slot.  since no member of the queue may advance more than 2 spaces forward, there are
    // 3 possible legal values for each position in the queue.

    val legalValues = mutable.ArrayBuffer[Int](1, 2, 3)
    var totalBribes = 0
    var abort: Boolean = false
    var i = 0

    while (!abort && i < q.size) {
      if (q(i) == legalValues(0)) {
        legalValues(0) = legalValues(1)
        legalValues(1) = legalValues(2)
        legalValues(2) += 1
      }
      else if (q(i) == legalValues(1)) {
        // we haven't seen legalValues(0) yet, so don't change it
        legalValues(1) = legalValues(2)
        legalValues(2) += 1
        totalBribes += 1
      }
      else if (q(i) == legalValues(2)) {
        // we haven't seen legalValues(0) or (1) yet, so don't change them
        legalValues(2) += 1
        totalBribes += 2
      }
      else {
        println("Too chaotic")
        abort = true
      }
      i += 1
    }
    if (!abort) {
      println(s"$totalBribes")
    }
  }

  def main(args: Array[String]): Unit = {
    minimumBribes(Array(2,1,5,3,4)) // 3
    minimumBribes(Array(2,5,1,3,4)) // too chaotic

    minimumBribes(Array(1, 2, 5, 3, 7, 8, 6, 4)) // 7
  }
}
