-module(aoc18_2).
-export([parttwo/1, test/1]).

test(Str) ->
    domult(doadd(line_to_data(Str))).

greja(L) ->
    {number, Res} = domult(doadd(L)),
    io:format("Runs: ~w~n", [L]),
    io:format(" -> ~w~n", [Res]),
    Res.

parttwo(Filename) ->
    {ok, File} = file:open(Filename,[read]),
    ResL = lists:map(fun(L) -> greja(L) end, 
        read_lines_to_data(File, [])),
    lists:foldl(fun(A, B) -> A + B end, 0, ResL).

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

doadd([]) ->
    {[]};
doadd([{number, A}]) ->
    [{number, A}];
doadd([{open} | T]) -> 
    doadd(group(T, []));
doadd([{number, A}, {op,plus}, {number, B} | T]) ->
    doadd([{number, A + B} | T]);
doadd([{number, A}, {op,plus}, {open} | T]) ->
    doadd([{number, A}, {op,plus}| group(T, [])]);
doadd([{number, A}, {op,times} | T]) ->
    [{number, A}, {op, times} | doadd(T)].

group([{close} | T], Acc) ->
    [domult(doadd(lists:reverse(Acc))) | T];
group([ {open} | T], Acc) ->
    group(group(T, []), Acc );
group([ A | T], Acc) ->
    group(T, [A| Acc]).

domult([]) ->
    {number,1};
domult([{number,A}]) ->
    {number, A};
domult([{number, A}, {op,times}, {number,B} | T]) ->
    domult([{number, A*B} | T]).
