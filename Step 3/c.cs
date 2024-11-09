using System;

class Program
{
    static void Main(string[] args)
    {
        string[] dimensions = Console.ReadLine().Split(' ');
        int n = int.Parse(dimensions[0]);
        int m = int.Parse(dimensions[1]);
        string[] candlePosition = Console.ReadLine().Split(' ');
        int x = int.Parse(candlePosition[0]);
        int y = int.Parse(candlePosition[1]);
        double result = AreaDifference(n, m, x, y);
        Console.WriteLine($"{result:F3}");
    }

    static double AreaDifference(int n, int m, int x, int y)
    {
        double totalArea = n * m;
        double part1_1 = (x * y) / 2.0;
        double part1_2 = totalArea - part1_1;
        double diff1 = Math.Abs(part1_1 - part1_2);
        double part2_1 = ((n - x) * y) / 2.0;
        double part2_2 = totalArea - part2_1;
        double diff2 = Math.Abs(part2_1 - part2_2);
        double part3_1 = ((n - x) * (m - y)) / 2.0;
        double part3_2 = totalArea - part3_1;
        double diff3 = Math.Abs(part3_1 - part3_2);
        double part4_1 = (x * (m - y)) / 2.0;
        double part4_2 = totalArea - part4_1;
        double diff4 = Math.Abs(part4_1 - part4_2);
        return Math.Min(Math.Min(diff1, diff2), Math.Min(diff3, diff4));
    }
}
