-module(aoc19v0).
-export([partone/1, partone/2, check/3, readlines/3]).

partone(Filename) -> partone(Filename, false).

partone(Filename, Verbose) ->
    {Rules, Messages} = read(Filename),
    nr(evaluate(Rules, Messages, Verbose)).

evaluate(_, [], _) ->
    [];
evaluate(Rules, [H| T], Verbose) ->
    {B, _} = check(Rules, {start, 0}, H),
    case Verbose of 
        V when V == true; V == verbose ->
            io:format("~w ~s~n", [B, H]); 
        _ -> ok 
    end,
    [B| evaluate(Rules, T, Verbose)].

nr([]) -> 0;
nr([B| T]) ->
    case B of
        true -> 1 + nr(T);
        false -> nr(T)
    end.

% Functions for reading a file into a rule structure,
% a dict of integer keyed rules, where a rule is a tuple of rules
% {char, char()} | {orlist, [{andlist, [integer()]}] 
% 

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
            readlines(File, rules, dict:append(N, V, Acc));
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
            {N, {orlist, orsplit(S)}}
    end.

orsplit(Rulestr) ->
    case string:split(string:trim(Rulestr), "|") of
        [] -> 
            [];
        [S] -> [{andlist,andsplit(S)}];
        [H, T] ->
            [{andlist, andsplit(H)}| orsplit(T)]
    end.

andsplit(Str) ->
    case string:to_integer(string:trim(Str)) of
        {N, []} -> 
            [N];
        {N, T} ->
            [N| andsplit(T)]
    end.


% Functions for checking if a string follows a set of rules,
% a dict of integer keyed rules, where a rule is a tuple of rules
% {char, char()} | {orlist, [{andlist, [integer()]}] 
% 

% check(Rules, Rule, Mess) -> {Result :: boolean(), MessRest :: string()}

check(Rules, {start, N}, M) ->
    {B, M1} = check(Rules, hd(dict:fetch(N, Rules)), M),
    {B and (M1 == ""), M1};
check(_, {andlist, []}, M) -> 
    {true, M};
check(Rules, {andlist, [AH| AT]}, M) ->
    {B1, M1} = check(Rules, hd(dict:fetch(AH, Rules)), M),
    case B1 of
        true -> 
            check(Rules, {andlist, AT}, M1);
        false ->
            {false, M1}
    end;
check(_, {orlist, []}, M) -> 
    {false, M};
check(Rules, {orlist, [OH| OT]}, M) ->
    {B, M1} = check(Rules, OH, M),
    case B of
        true -> {true, M1};
        false -> check(Rules, {orlist, OT}, M)
    end;
check(_, {char, _}, []) ->
    {false, []};
check(_, {char, C}, [MH| MT]) ->
    {C == MH, MT}.


