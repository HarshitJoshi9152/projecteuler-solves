--[[A Pythagorean triplet is a set of three natural numbers, a &lt; b &lt; c, for which

 a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product `abc`
--]]


-- hmmm it works but it takes a lot of time and its not the best (bad complexity !)

--checkout : https://projecteuler.net/overview=009
p = math.pow

exp_sum = 1000

a = 0
while a < 1000 do
    b = 0
    while b < 1000 do
        if b < a then
            while b < a do
                b = b + 1
            end
        else 
            c = 0
            while c < 1000 do
                if c < b then
                    while c < b do
                        c = c + 1
                    end
                else 
                    s = a+ b+ c
                    print("trying", a, b, c, s)
                    if s == 1000 then
                        if c == math.sqrt(p(a, 2) + p(b, 2)) then
                            print("FOUND IT, ", a, b, c)
                            os.exit()   
                            break
                        end
                    end
                end
                c = c + 1
            end
            b = b + 1
        end
    end
    a = a + 1
end
