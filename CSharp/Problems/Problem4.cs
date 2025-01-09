namespace CSharp.Problems;

public static class Problem4
{
    public static int Solve()
    {
        var max = 0;
        for (var i = 100; i < 1000; i++)
        {
            for (var j = 100; j < 1000; j++)
            {
                var prod = i * j;
                if (IsPalindrome(prod) && prod > max)
                    max = prod;
            }
        }

        return max;
    }

    private static bool IsPalindrome(int n)
    {
        var number = n.ToString();
        var charArray =  number.ToCharArray();
        Array.Reverse(charArray);
        return number == new string(charArray);
    }
}