(define result 0)
(define (count s n)
    (if (null? s)
        0
        (if (= (car s) n)
            (+ 1 (count (cdr s) n))
            (+ 0 (count (cdr s) n))
            )
        )
    )
    
(define (add a)
    (define (helper b)
        (+ a b)
        )
    helper
    )

(define (test s)
    (if (= (length s) 0)
        s
        (append 
                (list (car s)) 
                (test (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))
                )
        )
    )
(define (repate k fn)
    (fn)
    (if (> k 0)
        (repate (- k 1) fn)
        )
    )

