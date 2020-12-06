-module(aoc06).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt",[read]),
    Glist = read_lines_to_groups(File, [], []),
    file:close(File),
    Ulist = lists:map(fun sets:union/1, Glist),
    Ilist = lists:map(fun sets:intersection/1, Glist),
    U = lists:sum(lists:map(fun sets:size/1, Ulist)),
    I = lists:sum(lists:map(fun sets:size/1, Ilist)),
    {U,I}.

read_lines_to_groups(File, A, Acc) ->
    % Returns a list of lists of sets of characters
    Apa = file:read_line(File),
    case Apa of
    eof -> 
        case Acc of
            [] -> lists:reverse(A);
            _ -> lists:reverse([Acc | A])
        end;
    {ok, Line} ->
        S = sets:from_list(string:chomp(Line)),
        case sets:is_empty(S) of
            true -> 
                case Acc of
                    [] -> read_lines_to_groups(File, A, []);
                    _  -> read_lines_to_groups(File, [Acc | A], [])
                end;
            false ->
                read_lines_to_groups(File, A, [S|Acc])
        end;
    {error, What} -> 
        io:format("io:fread error: ~w~n", [What]),
        A
    end.