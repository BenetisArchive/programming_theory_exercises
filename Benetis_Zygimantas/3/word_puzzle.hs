import System.IO
import Data.List.Split
import Data.List
import Data.Char
import Control.Monad


main = do
    contents <- readFile "895"
--    putStrLn $ show contents
    let input = splitOn "\n" contents
    let wordsEnd = fromJust $ elemIndex "#" input
    let inputSize = length input
    let dictionarySize = (inputSize-wordsEnd+1)
    let dictionary = take dictionarySize input
    let casesWithSpaces = take (inputSize-dictionarySize-3) $ drop (dictionarySize+1) input
    let cases = map (\(x) -> filter (/=' ') x) casesWithSpaces
    let allSets = map conseqPower cases
    print dictionary
    print cases
    print allSets
    print $ map (\(set)-> compareSets dictionary set) allSets

fromJust :: Maybe a -> a
fromJust Nothing = error "Maybe.fromJust: Nothing"
fromJust (Just x) = x

conseqPower = ([] :) . concatMap (tail . inits) . tails

compareSets words set = foldl (\iAcc setItem -> compareSetItemToDictionary words setItem + iAcc) 0 set

compareSetItemToDictionary words setItem = if any (==setItem) words
												then 1
												else 0
