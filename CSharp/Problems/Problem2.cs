namespace CSharp.Problems;

public static class Problem2
{
    public static int Solve(int max)
    {
        var nums = CalcFib(max);
        return nums.Where(n => n % 2 == 0).Sum();
    } 
    
    private static List<int> CalcFib(int max)
    {
        List<int> fibNums = [1, 2];
        while (fibNums.Last() <= max)
        {
            fibNums.Add(fibNums[^2] + fibNums.Last());
        }
        return fibNums;
    }
    
}