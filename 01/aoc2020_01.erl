-module(aoc).
-export([
    start/0,
    lcheck/1,
    read_int/2
]).

list_print([A|B]) ->
    io:format("~w, ", [A]),
    list_print(B);
list_print([]) ->
    io:format("~n", []).



start() ->
    {ok, File} = file:open("input.txt",[read]),
    A = read_int(File, []),
    file:close(File),
    list_print(A),
    lcheck(A).



read_int(File, A) ->
    Apa = io:fread(File, "", "~d"),
    io:format("~w~n", [Apa]),
    case Apa of
    eof -> 
        io:fwrite("Nu är det slut~n"),
        A;
    {ok, [N]} ->
        io:format("Läst: ~w~n", [N]),
        read_int(File, [N | A]);
    {ok, _} ->
        io:format("Tomt",[]),
        read_int(File, A);
    {error, What} -> 
        io:format("io:fread error: ~w~n", [What]),
        A
    end.

lcheck_first([A|[B|_]]) when A + B == 2020 -> A * B;
lcheck_first([A|[_|C]]) -> lcheck([A|C]);
lcheck_first([_|[]]) -> false.

lcheck([A|B]) ->
    case lcheck_first([A|B]) of
        false -> lcheck(B);
        C -> C
    end;
lcheck([]) -> false.

