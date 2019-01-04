object Pairs {

  def pairs(k: Int, arr: Array[Int]): Int = {
    // turn arr into a set A.  create another set B whose elements are arr[i] - k.
    // from B filter out everything < 1.  compute size of set intersection of A and B.

    val bigA = arr.toSet
    val bigB = bigA.map(x => x - k).filter(x => x > 0)
    bigA.intersect(bigB).size
  }

  def main(args: Array[String]): Unit = {
    println(pairs(2, Array(1,3,5,4,2)))
  }
}
