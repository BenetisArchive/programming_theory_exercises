doubleMe x = x + x
tripleMe x = doubleMe x + x

doubleSmallNumbers x = if x < 100
                          then doubleMe x
                          else x

boomBang xs = [if x < 10 then "Boom" else "Bang" | x <- xs, odd x]

tmp :: Int->Int

tmp x = x * 4

lucky :: (Integral a) => a -> String
lucky 7 = "LUCKY NUMBER SEVEN!"
lucky x = "Sorry, you're out of luck, pal!"

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial(n - 1)

pie "pi" = "Pie is delicious"
pie "ab" = "This is not right"

addVector :: (Num a) => (a,a) -> (a,a) -> (a,a)
addVector (a1, b1)(a2, b2)  = (a1 + a2, b1 + b2)

headAlt :: [a] -> a
headAlt [] = error "Cannot call head on empty list"
headAlt (x:_) = x

lengthAlt :: (Num b) => [a] -> b
lengthAlt [] = 0
lengthAlt (_:xs) = 1 + lengthAlt xs
bmiTell bmi
  | bmi <= 18.5 = "God damn emo!"
  | bmi <= 25.0 = "Normal? Boring"
  | bmi <= 30.0 = "OVERWEIGHT!"
  | otherwise = "WHALE"

divideByTen :: (Floating a) => a -> a
divideByTen = (/10)

isUpperAlphanum :: Char -> Bool
isUpperAlphanum = (`elem` ['A'..'Z'])

quick :: (Ord a) => [a] -> [a]
quick [] = []
quick (x:xs) =
  let smallBound = quick [a | a <- xs, a <= x]
      bigBound = quick [a | a <- xs, a > x]
   in smallBound ++ [x] ++ bigBound
