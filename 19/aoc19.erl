-module(aoc19v2).
-export([check/3, read/1, partone/1, test/2, parttwo/1]).

partone(Filename) ->
    {Rules, Messages} = read(Filename),
    length(lists:filter(fun({B,R}) -> B and (R=="") end, 
        lists:map(fun(M) -> aoc19v2:check(M, dict:fetch(0, Rules), Rules) end, 
            Messages))).

parttwo(Filename) ->
    {Rules, Messages} = read(Filename),
    length(lists:filter(fun(M) -> parttwocheck(M, Rules) end, Messages)).

parttwocheck(S,Rules) ->
    {N42, Rest1} = count(42,S,Rules,0),
    {N31, Rest2} = count(31,Rest1,Rules,0),
    if 
        N42 >= 2, N31 >=1, N42 > N31, Rest2 == "" ->
            true;
        true ->
            false
    end.

count(Rnr,S,Rules,N) ->
    case check(S, dict:fetch(Rnr, Rules), Rules) of
        {true, Rest} ->
            count(Rnr,Rest,Rules,N+1);
        {false, _} ->
            {N, S}
    end.

test(Filename, Start) ->
    {Rules, Messages} = read(Filename),
        lists:map(fun(M) -> aoc19v2:check(M, dict:fetch(Start, Rules), Rules) end, 
            Messages).

read(Filename) ->
    {ok, File} = file:open(Filename,[read]),
    Rules = readlines(File, rules, dict:new()),
    Messages = readlines(File, messages, []),
    {Rules, Messages}.

readlines(File, rules, Acc) ->
    % Acc är en dict
    Apa = file:read_line(File),
    case Apa of
        eof -> 
            Acc;
        {ok, [10]} ->
            Acc;
        {ok, Line} ->
            {N, V} = readrule(Line),
            readlines(File, rules, dict:store(N, V, Acc));
        {error, read_line} -> 
            error
    end;
readlines(File, messages, Acc) ->
    Apa = file:read_line(File),
    case Apa of
        eof -> 
            lists:reverse(Acc);
        {ok, "~n"} ->
            lists:reverse(Acc);
        {ok, Line} ->
            readlines(File, messages, [string:chomp(Line) | Acc]);
        {error, What} -> 
            {error, What}
    end.

readrule(Line) ->
    [Nrstr | [Rulestr]] = string:split(string:chomp(Line), ":"),
    {N, _} = string:to_integer(string:trim(Nrstr)),
    S = string:strip(Rulestr),
    case S of
        [$", C|  _] -> 
            {N, {char, C}};
        _ -> 
            {N, orsplit(S)}
    end.

orsplit(Rulestr) ->
    case
         string:split(string:trim(Rulestr), "|") of
        [] -> 
            [];
        [S] -> [andsplit(S)];
        [H, T] ->
            [andsplit(H)| orsplit(T)]
    end.

andsplit(Str) ->    
    case string:to_integer(string:trim(Str)) of
        {N, []} -> 
            [N];
        {N, T} ->
            [N| andsplit(T)]
    end.

check("", _, _) ->
    {false, ""};
check(S, Rule, Rules) ->
    case Rule of
        {char, C} ->
            case C == hd(S) of
                true ->
                    {true, tl(S)};
                false ->
                    {false, S}
            end;
        [] ->
            {false, S};
        [[]] ->
            {true, S};
        [OH| OT] ->
            case andcheck(S, OH, S, Rules) of
                {true, Rest} ->
                    {true, Rest};
                {false, _} ->
                    check(S, OT, Rules)
            end
    end.

andcheck([], [], _, _) ->
    {true, ""};
andcheck([], [_], _, _) ->
    {false, ""};
andcheck(S, [], _, _) ->
    {true, S};
andcheck(S, [Rnr| RT], Smem, Rules) ->
    {Match, Rest} = check(S, dict:fetch(Rnr, Rules), Rules),
    case Match of
        true ->
            andcheck(Rest, RT, Smem, Rules);
        false ->
            {false, Smem}
    end.




            





