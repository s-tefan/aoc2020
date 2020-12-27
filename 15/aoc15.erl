-module(aoc15).
-export([partone/0, memory/1, test/1, doit/1]).


% Först version with recursion, bad complexity
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

% This will not take the big one
memory(N) ->
    Input = lists:reverse([0,6,1,7,2,19,20]),
    Test = lists:reverse([0,3,6]),
    hd(make(Test, N)).

partone() ->
    Input = lists:reverse([0,6,1,7,2,19,20]),
    hd(make(Input, 2020)).

% For test purposes
test(N) ->
    Input = lists:reverse([0,6,1,7,2,19,20]),
    Test = lists:reverse([0,3,6]),
    make(Test, N).

%%% version 2.2, akin to the python version in aoc2020_15.py, but much slower   

update(State) ->
    {Last, D, Pos} = State,
    case dict:find(Last, D) of
        error ->
            {0, dict:store(Last, Pos, D), Pos + 1};
        {ok, LastPos} -> 
            {Pos - LastPos, dict:store(Last, Pos, D), Pos + 1}
        end.

loop_update(_, N) when N < 0 -> 
    error;
loop_update(State, 0) ->
    {Last, _, _} = State,
    Last;
loop_update(State, N) ->
    loop_update(update(State), N - 1).

init_dict([N| []]) -> 
    {N, dict:new(), 1};
init_dict([N1| T]) ->
    {N, D, P} = init_dict(T),
    {N1, dict:store(N, P, D), P+1}.

doit(N) ->
    %Test = lists:reverse([0,3,6]),
    Input = lists:reverse([0,6,1,7,2,19,20]),
    {Last, D, Pos} = init_dict(Input),
    %{Last, dict:to_list(D), Pos}.
    loop_update({Last, D, Pos}, N-Pos).
