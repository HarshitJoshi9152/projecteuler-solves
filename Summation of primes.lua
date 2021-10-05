--[[

Summation of primes
-- Problem 10

-- The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
-- Find the sum of all the primes below two million.
--]]

function isPrime(n)
    -- if n == 3 or n == 2 or n == 5 then
    --     return true
    -- end

    -- these % filters shreaded another 50 ms !
    if n%3 == 0 then
        return false
    end
    -- these % filters shreaded another 50 ms !
    if n%5 == 0 then
        return false
    end

    if n%2 == 0 then
        return false
    end

    -- not checking even numbers because we already tried 2 (but we already tried 3, 5 too)
    for i = 3, math.sqrt(n), 2 do
        if n % i == 0 then
            return false
        end
    end
    return true
end

limit = 2000000

primes = {2,3,5 }
sum = 2 + 3 + 5

for i=2, limit do
    if isPrime(i) then
        table.insert(primes, i)
        sum = sum + i
    end
end
print(sum)

--[[
________________________________________________________
Executed in    3.47 secs   fish           external 
   usr time    3.47 secs  565.00 micros    3.47 secs 
   sys time    0.00 secs  263.00 micros    0.00 secs 
   
]]
