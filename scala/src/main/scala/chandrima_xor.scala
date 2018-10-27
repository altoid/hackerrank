import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer

object chandrima_xor {

  def bitsToLong(bitstring: String): Long = (bitstring.toList.map(_.asDigit) foldLeft 0L) ((b, a) => 2 * b + a)

  def longToBits(n: Long, fillTo: Int = 60): String = {
    // left pad with 0 until the string is fillTo long.  if fillTo is 0, do not pad.
    val bits = n.toBinaryString

    val padding = if (fillTo > 0) (fillTo - bits.length max 0) else 0
    Array.fill(padding)(0).mkString ++ bits
  }

  def solve(arr: Array[Long]): Long = {
    // get all fibonacci numbers up to a max
    val fib_max = math.pow(10, 18)
    val fib_numbers_buf = mutable.ArrayBuffer[Long](1, 2)
    val powers_of_2_buf = mutable.ArrayBuffer[BigInt](1, 2)

    var i = 1
    var n = fib_numbers_buf(i) + fib_numbers_buf(i - 1)
    var p: BigInt = 4
    while (n < fib_max) {
      fib_numbers_buf += n
      powers_of_2_buf += p
      i += 1
      n = (fib_numbers_buf(i) + fib_numbers_buf(i - 1))
      p *= 2
    }

    val fib_numbers = fib_numbers_buf.reverse.toArray
    val powers_of_2 = powers_of_2_buf.reverse.toArray

    def zeckendorf(n: Long): BigInt = {
      var z: BigInt = 0
      var i = 0
      var x = n
      while (i < fib_numbers.length) {
        if (x >= fib_numbers(i)) {
          z += powers_of_2(i)
          x -= fib_numbers(i)
        }
        i += 1
      }
      z
    }

    val dorfed = arr.map(zeckendorf(_))

    val t: BigInt = (dorfed foldLeft BigInt(0))((b, a) => a ^ b)
    (t % 1000000007L).toLong
  }

  def main(args: Array[String]): Unit = {

//    val x = 4321L
//
//    println(s"x = $x")
//    println(zeckendorf(x) % 1000000007L)

    println(solve(Array[Long](1,2,3)))
    println(solve(Array[Long](1,3,4)))
  }


}
