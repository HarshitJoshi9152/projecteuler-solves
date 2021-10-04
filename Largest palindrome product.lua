--[[
Largest palindrome product

Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

--]]


function isPalindrome(n)
    s = tostring(n)
    s_R = string.reverse(s)
    if s == s_R then
        return true
    end
    return false
end

m_p = 0
function getPalindrome()
    for i = 100, 999 do
        for j = 100, 999 do
            p = i * j
            if isPalindrome(p) and m_p < p then
                m_p = p
            end
        end
    end
end

getPalindrome()
print(m_p)
