import System.IO
import Data.List.Split
main = do
    contents <- readFile "895"
--    putStrLn $ show contents
    let input = splitOn "\n" contents
    print input


