fun main(args: Array<String>) {
    //gan bang
    var x=8
    var y=4
    println("type of x:"+x::class.java.typeName)
    println("x="+x)

    //gan cong bang
    println()
    x=x+5
    println("x="+x)
    x+=5
    println("x="+x)

    //gan tru bang
    println()
    x=x-5
    println("x="+x)
    x-=5
    println("x="+x)

    //gan nhan bang
    println()
    x=x*2
    println("x="+x)
    x*=2
    println("x="+x)

    //gan chia bang
    println()
    x=x/4
    println("x="+x)
    x/=4
    println("x="+x)

    //gan phan tram bang
    x=5
    println()
    //x=x%3
    x%=3
    println("x="+x)

}