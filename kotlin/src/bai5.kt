fun main(args: Array<String>) {
    var soA=10
    var soB=3

    //phep cong
    println("cach1: a+b="+(soA+soB))
    println("cach2: a.plus(b)="+(soA.plus(soB)))

    //phep tru
    println("cach1: a-b="+(soA-soB))
    println("cach2: a.minus(b)="+(soA.minus(soB)))

    //phep nhan
    println("cach1: a*b="+(soA*soB))
    println("cach2: a.times(b)="+(soA.times(soB)))

    //phep chia
    println("cach1: a/b="+(soA/soB))
    println("cach2: a.div(b)="+(soA.div(soB)))

    var kq:Float=soA.toFloat()/soB
    println("cach3: a/b="+kq)

    //chia lay du
    println("cach1: a%b="+(soA%soB))
    println("cach2: a.rem(b)="+(soA.rem(soB)))

    //toan tu tien to 1 ngoi
    var x:Float=9.2f

    // tru 1 ngoi (dao dau)
    var y=x.unaryMinus()
    println("y="+y)

    //cong 1 ngoi
    var z=x.unaryPlus()
    println("z="+z)


}