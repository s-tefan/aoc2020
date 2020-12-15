-module(aoc15).
-export([partone/0]).

build([A| []]) -> [0, A];
build([A, A| T]) -> [1, A, A| T];
build([A, B | T]) -> 
    F = build([A| T]),
    case F of
        [0, A | _] -> [0, A, B| T];
        [N, A | _] -> [N+1, A, B| T]
    end.

make(A, N) ->
    case N - length(A) of
        0 -> A;
        _ -> make(build(A), N)
    end.

partone() ->
    Input = lists:reverse([0,6,1,7,2,19,20]),
    Test = lists:reverse([0,3,6]),
    hd(make(Input, 2020)).

