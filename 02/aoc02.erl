-module(aoc02).
-export([
    count_letter/2
]).

% To be completed ...

start() ->
    {ok, File} = file:open("input.txt",[read]),
    A = read_lines(File, []),
    file:close(File)
    .


splitter(S) ->
    [A,B,C] = string:split(string:trim(S), " "),
    [Min, Max] = list:map(list_to_integer, string:split(A)),
    Letter = string:slice(B, 1, 1)
    .

count_letter([], C) -> 0;
count_letter([C|B], C) -> 1 + count_letter(B, C);
count_letter([_|B], C) -> count_letter(B, C).





read_lines(File, A) ->
    Apa = io:read_line(File),
    case Apa of
    eof -> 
        list:reverse(A);
    {ok, Line} ->
        read_lines(File, [Line | A]);
    {error, What} -> 
        io:format("io:fread error: ~w~n", [What]),
        A
    end.