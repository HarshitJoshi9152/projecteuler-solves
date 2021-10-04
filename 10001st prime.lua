
function isPrime(n)
    for i = 2, n//2 do
        if n % i == 0 then
            return false
        end
    end
    return true
end

primes = {2, 3}

-- no of iterations => 10000 - 2 + 1 => 9999 (coz lua)
-- so we already have 2 vals in primes table so + 9999 values = 10001 th value !
for i = 2, 10000 do
    -- starting from where we left!
    j=primes[#primes] + 2
    while true do
        if isPrime(j) then
            table.insert(primes, j)
            print("found", j, "\t no: ", i)
            break
        end
        -- we dont want to test even numbers !
        j = j + 2
    end
end

print(primes[#primes])