namespace CSharp.Problems;

public static class Problem3
{
    public static long Solve(long n)
    {
        for (var i = 2; i < n; i++)
        {
            if (n % i != 0) continue;
            while (n % i == 0)
                n /= i;
        }

        return n;
    }
    
    
}