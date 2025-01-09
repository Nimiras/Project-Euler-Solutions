namespace CSharp.Problems;

public static class Problem1
{
    public static int Solve(int max)
    {
        var sum = 0;
        for (var i = 3; i < max; i++)
        {
            if (i % 3 == 0 || i % 5 == 0)
            {
                sum += i;
            }
        }
        return sum;
    }
}