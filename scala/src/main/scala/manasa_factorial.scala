import scala.collection.mutable

object manasa_factorial {

  def solve(nzeroes: Long): Long = {
    // n is the number of zeroes.  need to find smallest m such that m! has at least that many zeroes at the end.
    val upper_bound = 5 * math.pow(10, 16).toLong

    val powers_of_5_buf = mutable.ArrayBuffer[Long]()

    var p: Long = 5
    while (p <= upper_bound) {
      powers_of_5_buf += p
      p *= 5
    }
    // put one more in.  this will give us the smallest power of 5 > upper_bound, which we need to give us a 0 quotient
    // in count_zeroes_helper.
    powers_of_5_buf += p

    val powers_of_5 = powers_of_5_buf.toArray

    def count_zeroes_helper(powers: Array[Long], n: Long): Long = {
      // this will give us the number of zeroes for some n!
      val quotient = (n / powers.head)
      if (quotient == 0) 0
      else quotient + count_zeroes_helper(powers.tail, n)
    }

    def count_zeroes(n: Long): Long = count_zeroes_helper(powers_of_5, n)

    def search(left: Long, right: Long): Long = {
      val mid = (left + right) / 2
      if (right <= left) {
        var check = left
        while (count_zeroes(check) < nzeroes) {
          check += 1
        }
        return check
      }
      val candidate_nzeroes = count_zeroes(mid)
      if (candidate_nzeroes == nzeroes) {
        // scan left to find a smaller m
        var m = mid
        while (m - 1 > 0 && count_zeroes(m - 1) == nzeroes) {
          m -= 1
        }
        m
      }
      else if (candidate_nzeroes > nzeroes) {
        search(left, mid - 1)
      }
      else {
        search(mid + 1, right)
      }
    }

    search(1, upper_bound)
  }

  def main(args: Array[String]): Unit = {

    println(solve(23))
    println(solve(22))
    println(solve(24))
    println(solve(1))   // 5
    println(solve(2))   // 10
    println(solve(3))   // 15

    println(solve(629)) // 2525
    println(solve(236)) // 950
    println(solve(183))  // 740

    println(solve(4264777785391999L))  // 17059111141568050
  }


}
