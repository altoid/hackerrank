object Solution extends App {

	   def coin_change(amount: Int, coins: List[Int]): Int = {
	   	   val ncoins = coins.length

		   if (ncoins == 0) 0
		   else if (amount == 0) 1
		   else if (amount < 0) 0
		   else {
		   		val total1 = coin_change(amount, coins.tail)
				val total2 = coin_change(amount - coins.head, coins)

				total1 + total2
		   }
	   }

	   def solve(amount: Int, coins: List[Int]): Unit = {
	   	   println(s"amount = $amount")
		   println(s"coins = $coins")
		   val result = coin_change(amount, coins)
		   println(s"solution:  $result")
	   }

	   solve(4, List(1,2,3))
	   solve(10, List(2,3,5,6))
}
