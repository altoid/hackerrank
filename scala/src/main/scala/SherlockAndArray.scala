object SherlockAndArray {

  def balancedSums(arr: Array[Int]): String = {
    val leftSums = Array.fill(arr.length)(0)
    val rightSums = Array.fill(arr.length)(0)

    for (i <- 1 until arr.length) {
      leftSums(i) = leftSums(i - 1) + arr(i - 1)
    }

    for (i <- arr.length - 2 to 0 by -1) {
      rightSums(i) = rightSums(i + 1) + arr(i + 1)
    }

    for (i <- 0 until arr.length) {
      if (rightSums(i) == leftSums(i)) {
        return "YES"
      }
    }
    "NO"
  }


  def main(args: Array[String]): Unit = {
    println(balancedSums(Array(2,1,8,1,1,1,5,3))) // NO
    println(balancedSums(Array(4))) // YES
    println(balancedSums(Array(2,0,0,0))) // YES
  }
}
