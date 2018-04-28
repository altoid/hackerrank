// https://www.hackerrank.com/challenges/grading/problem

object Solution {

  def roundUp(g: Int): Int = {
    if (g < 38) g
    else {
      val rounded = ((g + 5 - 1) / 5) * 5
      if ((rounded - g) < 3) rounded else g
    }
  }

  def main(args: Array[String]) {
    val sc = new java.util.Scanner (System.in)
    var n = sc.nextInt()
    var grades = new Array[Int](n)
    for(i <- 0 to n-1) {
      val g = sc.nextInt()
      println(g + " --> " + roundUp(g))
//      grades(i) = sc.nextInt();
    }
  }
}