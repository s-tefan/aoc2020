-module(aoc2020_01).
-export([
    start/0,
    lcheck/1,
    read_int/2,
    lcheck2/1,
    sum_check1/2,
    sum_check2/2,
    sum_check3/2
]).


start() ->
    {ok, File} = file:open("input.txt",[read]),
    A = read_int(File, []),
    file:close(File),
    %list_print(A),
    sum_check2(A, 2020).


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
lcheck_first([A|[_|C]]) -> lcheck_first([A|C]);
lcheck_first([_|[]]) -> false.

lcheck([A|B]) ->
    case lcheck_first([A|B]) of
        false -> lcheck(B);
        C -> C
    end;
lcheck([]) -> false.


            
sum_check1(L, sum) ->
    case L of
        [A|_] when A == sum ->
            A;
        [_|T] ->
            sum_check1(T,sum);
        [] ->
            stop
    end.

sum_check2(L, sum) ->
    case L of
        [A,B|_] when A+B == sum ->
            A*B;
        [A|T] ->
            P1 = sum_check1(T, sum-A),
            if 
                P1 == stop ->
                    sum_check2(T, sum);
                true ->
                    A*P1
            end;
        [] ->
            stop
    end.


sum_check3(L, sum) ->
    case L of
        [A,B,C|_] when A+B+C == sum ->
            A*B*C;
        [A,B|T] ->
            P1 = sum_check2([B|T], sum-A),
            if 
                P1 == stop ->
                    P2 = sum_check1(T, sum-A-B),
                    if
                        P2 == stop ->
                            P3 = sum_check2(T, sum-A),
                            A * P3;
                        true ->
                            A * B * P2
                    end;
                true ->
                    A * P1 
            end;
        [_|[]] ->
            stop
    end.


%%% This has an awful complexity, O(3^n)
lcheck2(L) ->
    list_print(L),
    case L of
        [A,B,C|_] when A+B+C == 2020 -> A*B*C;
        [A,B,C|D] -> 
            E = lcheck2([A,B|D]),
            if E == stop ->
                F = lcheck2([B,C|D]),
                if F == stop ->
                    lcheck2([A,C|D]);
                true ->
                    F
                end;
            true ->
                E
            end;
        [_,_] -> stop;
        [_] -> stop;
        [] -> stop
    end.

list_print([A|[B|C]]) ->
    io:format("~w, ", [A]),
    list_print([B|C]);
list_print([A|[]]) ->
    io:format("~w~n", [A]);
list_print([]) ->
    io:format("~n", []).



