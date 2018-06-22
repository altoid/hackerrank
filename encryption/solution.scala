import java.io._
import java.math._
import java.security._
import java.text._
import java.util._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._

object Solution {

    // Complete the encryption function below.
    def encryption(s: String): String = {

		println(s)
		val stripped = s.filter(c => c != ' ').toString
		println(stripped)

		val l = stripped.length
		val r = math.floor(math.sqrt(l)).toInt
		val c = math.ceil(math.sqrt(l)).toInt

		println(s"l = $l, r = $r, c = $c")

		val y = 
		for (i <- 0 to r) yield {
			val x = (i to l by c).filter(n => n < l).map(stripped.charAt(_)).mkString
			x
		}

		println(y)

		"unimplemented"
    }

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val s = stdin.readLine

        val result = encryption(s)

        println(result)
    }
}
