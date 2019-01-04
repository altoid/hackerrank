import scala.collection.mutable

object SherlockAndAnagrams {
  // itemize every substring.  for |s| = 100 this will be 10100 substrings, not too bad.
  // then sort the chars in each substring and use these as the keys in a map.
  // the will be the number of times we encounter that sorted substring.
  // count the number of keys with value > 1.
  // since the problem asks for the number of pairs of substrings that are anagrams,
  // then we count C(count, 2) and add them up.

  def totalByLength(s: String, substring_length: Int): Int = {
    val m = mutable.HashMap[String, Int]()
    for (i <- 0 to s.length - substring_length) {
      val ss = s.substring(i, i + substring_length).sorted
      if (!m.contains(ss)) {
        m += (ss -> 0)
      }
      m += (ss -> (m(ss) + 1))
    }
    //println(m.mkString(" "))
    val counts = m.values
    counts.map(x => x * (x - 1) / 2).sum
  }

  def sherlockAndAnagrams(s: String): Int = {
    val x = for (i <- 1 until s.length) yield {
      totalByLength(s, i)
    }
    x.sum
  }

  def main(args: Array[String]): Unit = {
    println(sherlockAndAnagrams("spinnipspinssnip"))
    println(sherlockAndAnagrams("kkkk")) // 10
    println(sherlockAndAnagrams("ifailuhkqq")) // 3
    println(sherlockAndAnagrams("cdcd")) // 5
  }
}
