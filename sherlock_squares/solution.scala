import io._

object Solution {

    def squares(a: Int, b: Int): Int =  {
		math.sqrt(b).toInt - math.ceil(math.sqrt(a)).toInt + 1
    }

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var q = sc.nextInt();
        var a0 = 0;
        while(a0 < q){
            var a = sc.nextInt();
            var b = sc.nextInt();
            val result = squares(a, b);
            println(result)
            a0+=1;
        }
    }
}
