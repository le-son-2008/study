using System.Text;

namespace Bai2_2;

class Program
{
    static void Main(string[] args)
    {
    Console.OutputEncoding=Encoding.UTF8;

    string hoTen;
    float diemToan;
    float diemVan;

    System.Console.WriteLine("Mời nhập họ tên:");
    hoTen=Console.ReadLine();

    System.Console.WriteLine("Mời nhập điểm toán:");
    diemToan=float.Parse(Console.ReadLine());

    System.Console.WriteLine("Mời nhập điểm văn:");
    diemVan=float.Parse(Console.ReadLine());

    System.Console.WriteLine("Bạn {0} có điểm toán là {1}, điểm văn là {2}",hoTen,diemToan,diemVan);
    }
}
