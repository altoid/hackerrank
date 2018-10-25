import scala.collection.mutable.ArrayBuffer

// max value for signed long is 9223372036854775807, which is > 10 ** 18.
// so 10 ** 18 fits in a long

object chandrima_xor {

  def solve(arr: Array[Long]): Int = {
    // for each number in arr, turn it into a list of bits.
    val a2 = arr.map(x => x.toBinaryString.toArray.map(_.asDigit))
    val maxlength = (a2 foldLeft 0)((b, a) => a.length max b)

    // pad on the left with 0s
    val a3 = a2.map(x => {
      val padding = Array.fill(maxlength - x.length)(0)
      padding ++ x
    })

    for (x <- a3) {
      println(x.mkString)
    }

    val s = a3.map(_(0))
    println(s.foldLeft(0)(_ + _))

    val counts = ArrayBuffer[Int]()
    val xors = ArrayBuffer[Int]()

    for (i <- 0 until maxlength) {
      val s = a3.map(_(i))
      counts += s.foldLeft(0)(_ + _)
      xors += s.foldLeft(0)((b, a) => a ^ b)
    }

    println(counts.toArray.mkString(" "))
    println(xors.toArray.mkString(" "))
    0
  }

  // return true iff n has no runs of consecutive 1 bits.
  def isKosher(n: Long): Boolean = (n & (n << 1)) == 0

  def bitsToLong(bitstring: String): Long = (bitstring.toList.map(_.asDigit) foldLeft 0L)((b, a) => 2 * b + a)

  def longToBits(n: Long, fillTo: Int = 0): String = {
    // left pad with 0 until the string is fillTo long.  if fillTo is 0, do not pad.
    val bits = n.toBinaryString.toArray.map(_.asDigit).mkString

    val padding = if (fillTo > 0) (fillTo - bits.length max 0) else 0
    Array.fill(padding)(0).mkString ++ bits
  }

  def successor(n: Long): Long = {
    // algorithm:
    // find the number we have to add to n to result in a number that is kosher.  if we cannot find such a number,
    // throw exception.
    //
    // need to find the next larger number that does not have consecutive 1 bits.
    //
    // to do this we need to add to the original number a value that causes its
    // 1111 substrings to roll over to 10000:
    //
    // 000000000000000010010001100001111110011100101010000000000000
    //                        ^^    ^^^^^^  ^^^
    //
    //                         1     11111   11
    //
    // we'll take n, shift it 1 to the left, then AND this with n
    //
    // 000000000000000010010001100001111110011100101010000000000000
    // 000000000000000100100011000011111100111001010100000000000000   << shifted 1 to the left
    // ------------------------------------------------------------
    //                        1     11111   11                       << a
    //                         1     11111   11                      << b
    //  a b  f
    //  1 0  0
    //  1 1  0
    //  0 1  1
    //  0 0  0
    //take the & and then shift 1 position to right.  then do !a & b.
    //this is what we add to the original number.  if the result still has
    //consecutive 11 bits, do it again.

    val shifted_n = n << 1
    val result = n & shifted_n
    val result_shifted = result >> 1

    println(longToBits(n, 60))
    println(longToBits(shifted_n, 60))
    println(longToBits(result, 60))

    val result_bits = result.toBinaryString.toArray.map(_.asDigit)
    val result_shifted_bits = result_shifted.toBinaryString.toArray.map(_.asDigit)

    val addend = ~result & result_shifted
    println(longToBits(result_shifted, 60))
    println()
    println(longToBits(n, 60))
    println(longToBits(addend, 60))
    println(longToBits(n + addend, 60))
    0
  }

  def main(args: Array[String]): Unit = {
    val arr = ArrayBuffer[Long]()
    arr += math.pow(10, 18).toLong
    arr += math.pow(10, 13).toLong
    arr += math.pow(10, 11).toLong

    val n = math.pow(10, 13).toLong
//    val bits = n.toBinaryString.toArray.map(_.asDigit)
//    val n2 = bitsToLong(n.toBinaryString)
//
//    val morebits = "000000000000000010010001100001111110011100101010000000000000"
//    println(bits.mkString +": " + isKosher(n))
//    println(morebits +": " + isKosher(bitsToLong(morebits)))

//    println(bitsToLong("011001")) // 25
//    println(bitsToLong(morebits))
//    println(bitsToLong(morebits).toBinaryString.toArray.map(_.asDigit).mkString)

    val s = successor(n)
  }

}
