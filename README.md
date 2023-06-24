# Week7_Profiler
This assignment shows how code can be optimized with the help of cProfiler.

Using the original code that was uploaded to this repository, the cProfiler produced the following results:
![image](https://github.com/MedeirosPereiraRaf/Week7_Profiler/assets/136990615/119129ad-96ac-4f94-b27e-173578a92d05)

According to the cProfiler, it took a total of 135 seconds to run, and the problem function was "findPrimes". In that function, I notice a while loop, which can very much hurt performance if not used with caution. My idea is to replace the while loop with checking for if number is prime.

The code was then optimized, please refer to the commit that performs the optimization.

After the code was optimized, the cProfiler produced this result:
![image](https://github.com/MedeirosPereiraRaf/Week7_Profiler/assets/136990615/40b91200-fa94-4456-be0d-e1004fb35057)

Notice how the time went from 135 seconds down to 15 seconds after optimization.
