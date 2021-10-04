--[[
Smallest multiple


Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
]]


--[[
n = 2
while true do
    local f = false
    print("trying " .. n)

    for i = 1, 20 do
        if n % i ~= 0 then
            f = false
            break
        end
        f = true
    end

    if f then
        print(n)
        break
    end

    n = n + 1
end
]]



function isPrime(n)
    for i=2, n - 1 do
        -- print(i, n, n % i)
        if n % i == 0 then
            return false
        end
    end
    return true
end

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

for i=2, 20 do
    findPrimeFactors(i, 2)
end

res = 1
done = {}
for k,v in pairs(p_factors) do
    print(k, v)
    if not done[v] then
        res = res * v
    end
    done[v] = true
end

print(res)

for i=1, 20 do
    if res % i ~= 0 then
        print(false)
    end
end
