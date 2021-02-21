(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define les (length s))
  (define (helper s L)
      (if (eq? s nil)
          '()
          (cons (cons (- L (length s)) (list (car s))) (helper (cdr s) L)))) 
  (helper s les))
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (if (eq? list1 nil)
      list2
      (if (eq? list2 nil)
          list1
          (if (comp (car list1) (car list2))
              (cons (car list1) (merge comp (cdr list1) list2))
              (cons (car list2) (merge comp list1 (cdr list2))))))
  )
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
    (define (helper result per s)
        (if (= 1 (length s))
            (append result (list (append per (list (car s)))))
            (if (<= (car s) (cadr s))
                (helper result (append per (list (car s))) (cdr s))
                (helper (append result (list (append per (list (car s))))) '() (cdr s)))))
    (helper '() '() s)
    )
    ; END PROBLEM 17


