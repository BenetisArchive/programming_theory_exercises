% Patikrinkite ar du skaičiai yra kopirminiai (bendras didžiausias daliklis yra 1)
gcd(X, Y, Z) :-
    X < 0, !,
    gcd(-X, Y, Z).
gcd(X, Y, Z) :-
    Y < 0, !,
    gcd(X, -Y, Z).
gcd(X, 0, X) :- X > 0.
gcd(0, Y, Y) :- Y > 0.
gcd(X, Y, Z) :-
    X > Y, Y > 0,
    X1 is X - Y,
    gcd(Y, X1, Z).
gcd(X, Y, Z) :-
    X =< Y, X > 0,
    Y1 is Y - X,
    gcd(X, Y1, Z).

coprime(X, X) :- fail.
coprime(X, Y) :- gcd(X, Y, 1).
