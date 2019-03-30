import scala.collection.mutable

object MissingNumbers {

  def missingNumbers(with_missing: Array[Int], orig: Array[Int]): Array[Int] = {
    val orig_counts = orig.groupBy(x => x).mapValues(_.length)

    val missing_counts = with_missing.groupBy(x => x).mapValues(_.length)

    // now give me all the elements in orig_counts whose keys also are in missing_counts
    val orig_keys = orig_counts.keySet
    val missing_keys = missing_counts.keySet
    val result = mutable.ArrayBuffer[Int]()

    for (c <- orig_keys) {
      if (!missing_keys.contains(c)) {
        result += c
      }
      else if (orig_counts(c) > missing_counts(c)) {
        result += c
      }
    }
    result.toArray.sorted
  }

  def main(args: Array[String]): Unit = {
    println(missingNumbers(Array(), Array(1,1,1,2,3,5,5,5,5)).mkString(" "))

    println(missingNumbers(Array(1,2,2,3,5,6), Array(1,1,1,2,3,5,5,5,5,7,7)).mkString(" "))
  }
}
