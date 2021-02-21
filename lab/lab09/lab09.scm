;; Scheme ;;

(define (over-or-under a b)
  (if (> a b)
      1
      (if (= a b)
          0
          (- 1))))

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

(define (filter-lst fn lst)
  (filter fn lst)
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (make-adder n)
  (define (helper m)
      (+ m n))
  helper
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13

;; Extra questions

(define lst
  (list '(1) 2 '(3 4) 5)
)

(define (composed f g)
  (define (helper x)
      (f (g x)))
  helper
)

(define (remove item lst)
  (filter (lambda (x) (not (= x item))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  (if (null? s)
      s
      (append (list (car s)) 
              (no-repeats (filter (lambda (x) (not (= x (car s)))) (cdr s)))))
)

(define (substitute s old new)
  (if (null? s)
      s
      (if (pair? (car s))
          (append (list (substitute (car s) old new)) (substitute (cdr s) old new))
          (if (eq? (car s) old)
              (append (list new) (substitute (cdr s) old new))
              (append (list (car s)) (substitute (cdr s) old new)))))
)


(define (sub-all s olds news)
    (if (null? olds)
        s
        (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
)