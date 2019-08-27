object CaesarCipher {
  def roll(c: Char, r: Int): Char = {
    if (c >= 'a' && c <= 'z') {
      var delta = c.toInt - 'a'.toInt
      delta = (delta + r) % 26
      ('a'.toInt + delta).toChar
    }
    else if (c >= 'A' && c <= 'Z') {
      var delta = c.toInt - 'A'.toInt
      delta = (delta + r) % 26
      ('A'.toInt + delta).toChar
    }
    else {
      c
    }
  }

  def cipher(s: String, r: Int): String = {
    s.toList.map(c => roll(c, r)).mkString
  }

  def main(args: Array[String]): Unit = {
    println('a'.toInt)  // 97
    println('A'.toInt)  // 65

    val b = 66
    println(b.toChar)

    println(roll('a', 0))
    println(roll('A', 20))
    println(roll('A', 26))
    println(roll('A', 27))
    println(roll('#', 13))

    val test = "There's gold in them thar hills"

    val result = test.toList.map(c => roll(c, 31)).mkString
    println(result)
    println(result.toList.map(c => roll(c, 21)).mkString)
  }
}
