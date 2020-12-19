-module(aoc18).
-export([partone/1]).

partone(Filename) ->
    {ok, File} = file:open(Filename,[read]),
    compute_them(read_lines_to_data(File, []), []).
    
read_lines_to_data(File, Acc) ->
    % Returns a list of lines interpreted by line_to_data/1
    Apa = file:read_line(File),
    case Apa of
    eof -> 
        lists:reverse(Acc);
    {ok, Line} ->
        read_lines_to_data(File, [line_to_data(Line) | Acc]);
    {error, What} -> 
        io:format("io:fread error: ~w~n", [What]),
        error
    end.

compute_them([], Acc) ->
    lists:reverse(Acc);
compute_them([Expr| Rest], Acc) ->
    %A = reduce(Expr),
    A = comp(Expr, none, none),
    %A = compute(Expr, []),
    io:format("~w,",[A]),
    compute_them(Rest, [A | Acc]).

line_to_data(Line) ->    
    case Line of
        %A -> A;
        [$ | S] -> line_to_data(S);
        [$\n | S] -> line_to_data(S);
        [$( | S] -> [{open} | line_to_data(S)];
        [$) | S] -> [{close} | line_to_data(S)];
        [$+ | S] -> [{op, plus} | line_to_data(S)];
        [$* | S] -> [{op, times} | line_to_data(S)];
        [C | S] -> 
            case string:to_integer([C]) of
                {error, _} -> [blä | line_to_data(S)];
                {N, _} -> [{number, N} | line_to_data(S)]
            end;
        [] -> [];
        _ -> blaj
    end.

comp([], A, none) ->
    {A, []};
comp([{number, X} | Rest], none, none) ->
    comp(Rest, X, none);
comp([{number, X} | Rest], A, Lop) ->
    comp(Rest, operate(Lop, A, X), none);
comp([{op, Op} | Rest], A, none) ->
    comp(Rest , A, Op);
comp([{open} | Rest], none, none) ->
    {B, Nrest} = comp(Rest, none, none),
    comp(Nrest, B, none);
comp([{open} | Rest], A, Lop) ->
    {B, Nrest} = comp(Rest, none, none),
    comp(Nrest, operate(Lop, A, B), none);
comp([{close} | Rest], A, none) ->
    {A, Rest}.

operate(plus, A, B) ->
    A + B;
operate(times, A, B) ->
    A * B.


