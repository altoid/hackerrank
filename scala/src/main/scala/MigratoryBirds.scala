object MigratoryBirds {
  def result(arr: Array[Int]): Int = {
    val s = arr.groupBy(identity).mapValues(_.size)
    //val maxVal = s.valuesIterator.reduceLeft(_ max _)
    val maxVal = s.values.max
    val result = s.filter(_._2 == maxVal)
    // println(result)

    result.keys.min
  }

  def main(args: Array[String]): Unit = {
    val a: Array[Int] = Array(1,4,4,4,5,3)

    println(result(a))

    println(result(Array(1,2,3,4,5,4,3,2,1,3,4)))
  }
}
