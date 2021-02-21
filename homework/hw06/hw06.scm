;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond ((< x 0) -1) ((= x 0) 0) ((> x 0) 1))
)

(define (square x) (* x x))

(define (pow b n)
  (if (= n 1)
      (* b n)
      (if (even? n)
          (square (pow b (/ n 2)))
          (* b (square (pow b (/ (- n 1) 2))))
          )
      )
)


(define (unique s)
    (if (= (length s) 0)
        s
        (append 
                (list (car s)) 
                (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))
                )
        )
)


