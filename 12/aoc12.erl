-module(aoc12).
-record(boat, {
    instructions = [] , 
    position = {0,0},
    direction = {1,0} , 
    wp = false :: true | false
}). 
-export([start/0]).

read_file(Filename) ->
    {ok, File} = file:open(Filename, [read]),
        B = #boat{instructions = read_lines(File, [])},
    file:close(File),
    B.

start() ->
    B = read_file("input.txt"),
    {navigate(B#boat{ wp = false, direction = {1,0}}),
    navigate(B#boat{ wp = true, direction = {10,1}}) }.

get_integer(S) ->
    {I, _} = string:to_integer(S),
    I.

command_from_char(C) ->
    list_to_atom(string:to_lower([C])).

read_lines(File, Instructions) ->
    % Returns a list of lists of sets of characters
    Apa = file:read_line(File),
    case Apa of
        eof -> 
            lists:reverse(Instructions);
        {ok, Line} ->
            case string:chomp(Line) of
                [H|T] ->
                    read_lines(File, [{command_from_char(H), get_integer(T)} | Instructions]);
                [] ->
                    read_lines(File, Instructions)
            end;
        {error, What} -> 
            io:format("io:fread error: ~w~n", [What])
    end.


go({l, 90}, B) ->
    {X, Y} = B#boat.direction,
    B#boat{direction = {-Y, X}};
go({l, 180}, B) ->
    {X, Y} = B#boat.direction,
    B#boat{direction = {-X, -Y}};
go({l, 270}, B) ->
    {X, Y} = B#boat.direction,
    B#boat{direction = {Y, -X}};
go({r, N}, B) ->
    go({l, 360-N}, B);
go({f, N}, B) ->
    {X, Y} = B#boat.position,
    {DX, DY} = B#boat.direction,
    B#boat{position = {X + N * DX, Y + N * DY}};
go({C, N}, B) when not(B#boat.wp)  ->
    {X, Y} = B#boat.position,
    case C of
        n -> B#boat{position = {X, Y + N}};
        s -> B#boat{position = {X, Y - N}};
        e -> B#boat{position = {X + N, Y}};
        w -> B#boat{position = {X - N, Y}}
    end;
go({C, N}, B) when B#boat.wp ->
    {X, Y} = B#boat.direction,
    case C of
        n -> B#boat{direction = {X, Y + N}};
        s -> B#boat{direction = {X, Y - N}};
        e -> B#boat{direction = {X + N, Y}};
        w -> B#boat{direction = {X - N, Y}}
    end.

navigate(B) when B#boat.instructions == [] ->
    Pos = B#boat.position,
    {finished, B, abs(element(1, Pos)) + abs(element(2, Pos))};
navigate(B) ->
    [{Command, Parameter} | Tinstr ] = B#boat.instructions, % Exception raised here
    NewB = go({Command, Parameter}, B),
    %io:format("newB = ~w~n", [B]),
    navigate(NewB#boat{instructions = Tinstr}).


