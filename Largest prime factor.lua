
--[[
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
--]]

-- Fri Oct 1, 2021 [11:49 PM]
-- https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python

function isPrime(n)
    for i=2, n - 1 do
        -- print(i, n, n % i)
        if n % i == 0 then
            return false
        end
    end
    return true
end

-- results = isPrime(13)
-- print(results)
-- function fact(n)
--     local max_factor = 0
--     local limit = n//2
--     for i = 1, limit do
--         print('progress (' .. tostring(i) .. ' of ' .. tostring(limit) .. ' completed ' .. tostring(i//limit * 100) .. '% completed')
--         if n % i == 0 and i > max_factor then
--             max_factor = i 
--         end
--     end
--     return max_factor
-- end
-- print(fact(600851475143))

p_factors = {}

function findPrimeFactors(n, k )
    for i = k, n - 1 do
        if n % i == 0 then
            if isPrime(i) then
                table.insert(p_factors, i)
                return findPrimeFactors(n // i, i)
            end
        end
    end
    table.insert(p_factors, n)
    return #p_factors
end

-- findPrimeFactors(13195, 2)

findPrimeFactors(600851475143, 2)

max_val = 0
for i=1, #p_factors do
    if p_factors[i] > max_val then
        max_val = p_factors[i]
    end
end

print(max_val)

