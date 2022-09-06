object Solution extends App {

	   def coin_change(amount: Int, coins: List[Int]): Int = {
	   	   val ncoins = coins.length

		   val key = List(amount, ncoins)

		   if (prior_solutions.contains(key)) {
		   	  return prior_solutions(key)
			  }

		   if (ncoins == 0) 0
		   else if (amount == 0) 1
		   else if (amount < 0) 0
		   else {
		   		val total1 = coin_change(amount, coins.tail)
				val total2 = coin_change(amount - coins.head, coins)

				val result = total1 + total2
				prior_solutions(key) = result
				result
		   }
	   }

	   def solve(amount: Int, coins: List[Int]): Unit = {
	   	   prior_solutions.clear
	   	   println(s"amount = $amount")
		   println(s"coins = $coins")
		   val result = coin_change(amount, coins)
		   println(s"solution:  $result")
	   }

   	   var prior_solutions = scala.collection.mutable.Map[List[Int], Int]()
	   solve(4, List(1,2,3))
	   solve(10, List(2,3,5,6))
	   solve(100, List(1,5,10,25))
	   solve(50, List(1,5,10,2))  // 341
	   solve(250, List(1,2, 5,10,20, 50)) // 177863

//    check(50, List(1, 2, 5, 10), 341)
//    check(250, List(1, 2, 5, 10, 20, 50), 177863)

}
