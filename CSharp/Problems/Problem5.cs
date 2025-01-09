namespace CSharp.Problems;

public static class Problem5
{
    public static long Solve()
    {
        long counter = 20;
        while (!DivisibleByRange(counter, 20))
            counter += 2;
        return counter;
    }

    private static bool DivisibleByRange(long num, long max)
    {
        for (var i = 2; i <= max; i++)
        {
            if (num % i != 0) return false;
        }
        
        return true;
    }
}