import scala.collection.mutable

object RansomNote {
  def checkMagazine(magazine: Array[String], note: Array[String]): Unit = {
    val table = mutable.HashMap.empty[String, Int]

    for (w <- magazine) {
      if (!(table contains w)) {
        table(w) = 0
      }
      table(w) += 1
    }
    // println(table.mkString(" "))

    for (w <- note) {
      if (!(table contains w)) {
        println("No")
        return
      }
      table(w) -= 1
      if (table(w) == 0) {
        table.remove(w)
      }
    }
    println("Yes")
  }

  def main(args: Array[String]): Unit = {
    checkMagazine(Array("one", "two", "two", "Three"), Array("one"))
    checkMagazine(Array("one", "two", "two", "Three"), Array("one", "one"))
    checkMagazine(Array("one", "two", "two", "Three"), Array("oneone"))
    checkMagazine(Array("one", "two", "two", "Three"), Array("three"))
  }
}
