% Raskite k-tąjį sąrašo narį, kai sąrašas m pradedamas nuo 1 (indeksas)
element_at(X, List, Pos) :-
    element_at(X, List, 1, Pos).
element_at(X, [X|_], Pos, Pos).
element_at(X, [_|T], Acc, Pos) :-
    Acc1 is Acc + 1,
    element_at(X, T, Acc1, Pos).
% element_at([1,2,3,4],2).