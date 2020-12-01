import System.IO( isEOF )


main :: IO()
main = do {line <- getLine; putStrLn line}


plupp lista = do 
    end <- isEOF
    line <- getline
    if line