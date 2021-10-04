
function isPrime(n)
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

--[[
    without isPrime no even opt

    Executed in  230.20 millis    fish           external 
    usr time  177.60 millis  486.00 micros  177.11 millis 
    sys time   40.45 millis  198.00 micros   40.25 millis 

    after isPrime no even opt

    Executed in  234.77 millis    fish           external 
    usr time  108.55 millis    0.00 micros  108.55 millis 
    sys time   67.69 millis  891.00 micros   66.80 millis 

]]


-- hmm i removed the prime numbers allocation/storage in a table
-- and performace didnot increase a lot.

-- primes = {2, 3}

-- no of iterations => 10000 - 2 + 1 => 9999 (coz lua)
-- so we already have 2 vals in primes table so + 9999 values = 10001 th value !
last = 3
for i = 2, 10000 do
    -- starting from where we left!
    -- j=primes[#primes] + 2
    j=last + 2
    while true do
        if isPrime(j) then
            -- table.insert(primes, j)
            last = j
            print("found", j, "\t no: ", i)
            break
        end
        -- we dont want to test even numbers !
        j = j + 2
    end
end

print(last)
-- print(primes[#primes])



-- result before math.sqrt(n) optimisation in isPrime function

-- ________________________________________________________
-- Executed in   10.22 secs   fish           external 
--    usr time   10.09 secs    0.00 micros   10.09 secs 
--    sys time    0.08 secs  933.00 micros    0.08 secs 


-- result after math.sqrt(n) optimisation in isPrime function

-- ________________________________________________________
-- Executed in  244.40 millis    fish           external 
--    usr time  198.35 millis    0.00 micros  198.35 millis 
--    sys time   45.66 millis  1128.00 micros   44.53 millis 


-- WOW SUCH DRASTIC CHANGE



--[[
check: ->  https://projecteuler.net/thread=7&page=8#last

Barandis: 889823

I wanted to have a lazy sequence of infinitely many prime numbers, and to do so I adapted the Haskell implementation on page 6 of this PDF. 
[https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf]
Once you have the infinite sequence, it's just a matter of looking up the proper index.

# Clojure

(ns barandis.euler.p7)

(def primes
  ((fn sieve [table x]
     (let [reinsert (fn [table prime] (update table (+ prime x) conj prime))]
       (if-let [factors (get table x)]
         (recur (reduce reinsert (dissoc table x) factors) (inc x))
         (lazy-seq (cons x (sieve (assoc table (* x x) (list x)) (inc x)))))))
   {} 2))

(defn- nth-prime [n] (nth primes (dec n)))

(defn solve
  ([] (solve {}))
  ([data] (-> (get data :input 10001)
              nth-prime
              println
              time)))


# Result

clj꞉barandis.euler.p7꞉> 
(solve)
104743
"Elapsed time: 0.952275 msecs"
nil


Factor already has a lazy list of primes defined, so the solution is trivial.

# Factor

USING: lists math math.primes.lists prettyprint tools.time ;
IN: barandis.euler.p7

: nth-prime ( n -- p ) 1 - lprimes lnth ;
: solve ( -- ) [ 10001 nth-prime . ] time ;

MAIN: solve


# Result

IN: scratchpad "barandis.euler.p7" run
104743
Running time: 0.003164879 seconds

]] 